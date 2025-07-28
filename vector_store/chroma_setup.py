
# import pandas as pd
# import chromadb
# from google import generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from google import generativeai as genai

# # --- Setup Gemini Embedding Model ---
# api_key = "AIzaSyC6_BxvOzwB24K2tj7c70CHr220kpnswjY"
# genai.configure(api_key=api_key)
# # embed_model = genai.GenerativeModel("gemini-embedding-001")

# # --- Setup ChromaDB ---
# client = chromadb.PersistentClient(path="chroma_storage")
# collection = client.get_or_create_collection("car_inventory")

# # --- Load and Embed CSV Rows ---
# def row_to_text(row):
#     return f"{row['make']} {row['model']}, {row['year']} {row['condition']} {row['body_style']}, ${row['price']}, {row['mileage']} miles"

# def get_embedding(text: str) -> list:
#     response = genai.embed_content(
#         model="models/embedding-001",
#         content=text,
#         task_type="retrieval_document"
#     )
#     return response["embedding"]



# def populate_chromadb(csv_path="data\car_inventory.csv"):
#     df = pd.read_csv(csv_path)
#     docs = [row_to_text(row) for _, row in df.iterrows()]
#     embeddings = [get_embedding(doc) for doc in docs]
#     collection.add(
#         documents=docs,
#         embeddings=embeddings,
#         ids=[str(i) for i in range(len(docs))],
#         metadatas=df.to_dict(orient="records")
#     )
#     print("✅ Vector DB populated with Gemini embeddings.")

# # --- Search via Gemini embedding ---
# def search_cars(query, top_k=3):
#     query_embedding = get_embedding(query)
#     results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
#     return results


# # # ---------------------
# # # LangChain Prompt & Chain Setup

# # # Gemini LLM wrapper from LangChain
# # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# # # Prompt template with context
# # prompt_template = PromptTemplate(
# #     input_variables=["question", "context"],
# #     template="""
# # You are an AI car assistant. A user asked: "{question}"

# # Based on the car listings below, recommend the best option(s) and explain briefly.

# # Car Listings:
# # {context}

# # Your response:
# # """
# # )

# # # LangChain LLMChain
# # chain = LLMChain(llm=llm, prompt=prompt_template)


# # --- Test Flow ---
# if __name__ == "__main__":
#     import os
#     if not os.path.exists("chroma/"):
#         populate_chromadb()

#     query = input("What kind of car are you looking for? ")
#     results = search_cars(query)

#     print("\n🔍 Top Matches:")
#     for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
#         print(f"✅ {doc}")
#         print(f"ℹ️  Metadata: {meta}")
#         print("---")



import os
import pandas as pd
import chromadb
from google import generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# -------------------------------
# 🔐 1. Configuration
API_KEY = "AIzaSyC6_BxvOzwB24K2tj7c70CHr220kpnswjY" 
CSV_PATH = "data/car_inventory.csv"
CHROMA_PATH = "chroma_storage"

# -------------------------------
# 🔧 2. Gemini Embedding Setup
genai.configure(api_key=API_KEY)

def get_embedding(text: str) -> list:
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    # return response.embeddings[0].values
    return response["embedding"][0]

# -------------------------------
# 🧠 3. ChromaDB Setup
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("car_inventory")

def row_to_text(row):
    return f"{row['make']} {row['model']}, {row['year']} {row['condition']} {row['body_style']}, ${row['price']}, {row['mileage']} miles"

def populate_chromadb(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path)
    docs = [row_to_text(row) for _, row in df.iterrows()]
    embeddings = [get_embedding(doc) for doc in docs]
    collection.add(
        documents=docs,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(docs))],
        metadatas=df.to_dict(orient="records")
    )
    print("✅ Vector DB populated with Gemini embeddings.")

def search_cars(query, top_k=3):
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results

# -------------------------------
# 💬 4. LangChain Generation Setup
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=API_KEY  # ✅ Explicitly pass API key
)

prompt_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""
You are an AI car assistant. A user asked: "{question}"

Based on the car listings below, recommend the best option(s) and explain briefly.

Car Listings:
{context}

Your response:
"""
)

chain = LLMChain(llm=llm, prompt=prompt_template)

# -------------------------------
# 🤖 5. Main Chat Flow
history = []
def run_chat():
    global history
    query = input("user")
    history.append(f"user:{query}")
    results = search_cars(history)

    print("\n🔍 Top Matches:")
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(f"✅ {doc}")
        print(f"ℹ️  Metadata: {meta}")
        print("---")

    # Generate explanation with LangChain
    context = "\n".join(results["documents"][0])
    response = chain.run({"question": history, "context": context})
    history.append(f"AI response:{response}")

    print("\n🤖 AI Car Assistant Suggestion:\n")
    print(response)

# -------------------------------
# 🚀 Entry Point
if __name__ == "__main__":
    if not os.path.exists(CHROMA_PATH):
        populate_chromadb()
    while True:
        run_chat()

