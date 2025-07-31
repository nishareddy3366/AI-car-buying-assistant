# AI-car-buying-assistant

An AI-powered car-buying assistant that helps users find the right car based on preferences.  
It uses **FastAPI** for the backend, **Streamlit** for the frontend, and integrates a retriever, generator, and guardrails pipeline.

---

## Project Structure

```
AI-car-buying-assistant/
│── main.py              # FastAPI backend
│── streamlit.py         # Streamlit frontend UI
│── requirements.txt     # Python dependencies
│
├── data/
│   ├── car_inventory.csv # Car dataset
│   └── data.py
│
├── retriever/
│   └── retriever.py     # Retrieves relevant cars from the dataset
│
├── generator/
│   └── generator.py     # Generates answers from retrieved data
│
├── utils/
│   ├── guardrails.py    # Input/output validation
│   ├── history.py       # Persistent chat history
│   └── config.py
│
├── prompts/
│   └── prompt.py        # AI prompts used in the pipeline
│
└── chroma_storage/      # Vector database (Chroma DB)
```

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd AI-car-buying-assistant-main
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the dataset is present**  
   - `data/car_inventory.csv` is required for car retrieval.

---

## Running the App

### 1. Start the FastAPI backend
```bash
python uvicorn main:app --reload
```
- Runs on: `http://localhost:8000`

### 2️. Start the Streamlit frontend
```bash
streamlit run streamlit.py
```
- Opens at: `http://localhost:8501`

---

## Features
- AI-powered **car search** with natural language queries.
- **Retriever-Generator pipeline** for accurate recommendations.
- **Guardrails** to filter unsafe inputs & outputs.
- **Persistent chat history** for user sessions.
- Uses **ChromaDB** for vector storage.

---

## Tech Stack
- **Python 3.10+**
- **FastAPI** (Backend)
- **Streamlit** (Frontend)
- **ChromaDB** (Vector storage)
- **LangChain** (Prompt & guardrails)
- **SQLite** (Chat history)

---

## Data
- The app uses `data/car_inventory.csv` as the car database.
- You can add/update data by modifying the CSV file.

