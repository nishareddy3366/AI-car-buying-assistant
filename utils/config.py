
from google import generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


# API Key
API_KEY = "YOUR-API-KEY" 
CHROMA_PATH = "chroma_storage"
CSV_PATH = "data/car_inventory.csv"
genai.configure(api_key=API_KEY)
DB_PATH = "utils/chat_history.db" 

# 🔧 LLM Setup
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=API_KEY
)