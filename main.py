import os
from vector_store.retriever import populate_chromadb, search_cars, CHROMA_PATH
from generator.generator import generate_answer

history = []

def run_chat():
    query = input("\n🧑 User: ").strip()
    if not query:
        print("❗ Please enter a valid query.")
        return
    history.append({"user": query})

    results = search_cars(query)
    top_docs = results["documents"][0]

    # ✅ Fallback when no relevant cars are found
    if not top_docs:
        fallback_message = (
            "Sorry, I couldn't find any matching cars in the inventory for your request.\n"
            "You can try rephrasing your query or ask about a different make, model, or price range."
        )
        print(f"\n🤖 AI Car Assistant: {fallback_message}")
        history.append({"assistant": fallback_message})
        return

    print("\n🔍 Top Matches:")
    for doc, meta in zip(top_docs, results["metadatas"][0]):
        print(f"✅ {doc}")
        print(f"ℹ️  Metadata: {meta}")
        print("---")

    context = "\n".join(top_docs)
    structured_response = generate_answer(query, context)

    print("\n🤖 AI Car Assistant Suggestion:")
    print(f"🚗 Recommendation: {structured_response.content}")
    # print(f"💡 Reason: {structured_response.reason}")

    history.append({"assistant": structured_response.model_dump()})

if __name__ == "__main__":
    while True:
        try:
            run_chat()
        except KeyboardInterrupt:
            print("\n👋 Exiting assistant. Bye!")
            break
