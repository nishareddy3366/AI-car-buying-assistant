from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from reteriver.retriever import search_cars
from generator.generator import generate_answer
from guardrails.guardrails import is_safe_input, is_safe_output

app = FastAPI(title="AI Car Buying Assistant")

# For storing simple chat history (in-memory)
history = []

# Request schema
class Query(BaseModel):
    message: str

# Response schema (optional but clean)
class ChatResponse(BaseModel):
    response: str
    # top_matches: list[str] = []
    # metadata: list[dict] = []
    # flagged: bool = False

@app.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(query: Query):
    user_input = query.message.strip()

    if not user_input:
        raise HTTPException(status_code=400, detail="Empty message.")

    if not is_safe_input(user_input):
        return ChatResponse(
            response="❌ Your message was flagged as unsafe or off-topic. Please ask a car-related and respectful question.",
            flagged=True
        )

    history.append({"user": user_input})

    results = search_cars(user_input)
    top_docs = results["documents"][0]
    metadata = results["metadatas"][0]

    if not top_docs:
        fallback_message = (
            "Sorry, I couldn't find any matching cars in the inventory for your request.\n"
            "You can try rephrasing your query or ask about a different make, model, or price range."
        )
        history.append({"assistant": fallback_message})
        return ChatResponse(response=fallback_message)

    context = "\n".join(top_docs)
    structured_response = generate_answer(user_input, context)
    final_output = structured_response.content

    if not is_safe_output(final_output):
        final_output = "⚠️ This response was filtered due to safety or quality issues. Please try rephrasing your query."

    history.append({"assistant": final_output})

    return ChatResponse(
        response=final_output
        # top_matches=top_docs,
        # metadata=metadata
    )
