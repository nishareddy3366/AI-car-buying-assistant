from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from retriever.retriever import search_cars
from generator.generator import generate_answer
from utils.guardrails import is_safe_input, is_safe_output
from utils.history import get_history, save_to_history 

app = FastAPI(title="AI Car Buying Assistant")

# For storing simple chat history (in-memory)
history = []

# Request schema
class Query(BaseModel):
    message: str
    session_id: str | None=None

@app.post("/chat")
async def chat_with_assistant(query: Query):
    user_input = query.message.strip()

    if not query.session_id:
        session_id = str(uuid4().hex)
    else:    
        session_id = query.session_id

    save_to_history(session_id, "user", user_input)      

    # history.append(f"user: {user_input}")

    current_history = "\n".join(get_history(session_id))
    if not is_safe_input(current_history):
        response = "Please ask a car-related and respectful question."
        save_to_history(session_id, "assistant", response)
        return {"response": response, "history": get_history(session_id)}

    results = search_cars(current_history)
    top_docs = results["documents"][0]

    context = "\n".join(top_docs)
    final_output = generate_answer(current_history, context)
    

    if not is_safe_output(final_output):
        final_output = "This response was filtered due to safety or quality issues. Please try rephrasing your query."

    save_to_history(session_id, "assistant", final_output)
    
    return {
        "response":final_output,
        "history": get_history(session_id)
        }