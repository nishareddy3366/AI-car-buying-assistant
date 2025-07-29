
from google import generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


# API Key
API_KEY = "AIzaSyC6_BxvOzwB24K2tj7c70CHr220kpnswjY" 
CHROMA_PATH = "chroma_storage"
CSV_PATH = "data/car_inventory.csv"
genai.configure(api_key=API_KEY)

# 🔧 LLM Setup
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=API_KEY
)