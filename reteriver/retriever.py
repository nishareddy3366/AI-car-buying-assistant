
import pandas as pd
import chromadb
from config import CHROMA_PATH, CSV_PATH, genai



def get_embedding(text: str) -> list:
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return response["embedding"]

# Initialize ChromaDB
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("car_inventory")

def row_to_text(row):
    return f"{row['make']} {row['model']}, {row['year']} {row['condition']} {row['body_style']}, ${row['price']}, {row['mileage']} miles"

def populate_chromadb():
    df = pd.read_csv(CSV_PATH)
    docs = [row_to_text(row) for _, row in df.iterrows()]
    embeddings = [get_embedding(doc) for doc in docs]
    collection.add(
        documents=docs,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(docs))],
        metadatas=df.to_dict(orient="records")
    )
    print("✅ Vector DB populated with Gemini embeddings.")

def search_cars(query: str, top_k=3):
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results


