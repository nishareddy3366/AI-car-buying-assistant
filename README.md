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
2. **Create Virtual Environment**   
    ```bash
   python -m venv venv
   venv\Scripts\activate
    ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the dataset is present and API key is configured**

   - The file `data/car_inventory.csv` is required for car retrieval.
   - Replace any placeholder API key in the code with your actual API key (if applicable).

---

## Running the App

### 1. Start the FastAPI backend
```bash
uvicorn main:app --reload
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
- **Shelve (dbm-based)** – for simple file-based chat history persistence



---

## Data
- The app uses `data/car_inventory.csv` as the car database.
- You can add/update data by modifying the CSV file.

---

## Approach

This assistant uses a modular pipeline combining:

1. **Retriever** – Filters relevant vehicles from a structured dataset (`car_inventory.csv`) based on the user query using basic semantic or keyword search.

2. **Generator** – Uses a language model to create conversational, human-like responses using LangChain's prompt engineering techniques.

3. **Guardrails** – Ensures safe input and output using basic heuristics and filtering (e.g., avoiding offensive, harmful, or irrelevant content). Greetings like “Hi” or “Hello” are still processed as valid queries.

4. **Persistence** – Chat history is stored using Python’s built-in shelve module, which saves messages in a simple file-based key-value store. It creates files like .dat, .dir, and .bak to manage session data on disk.

5. **Frontend/Backend** – A lightweight FastAPI backend powers the assistant, and a simple Streamlit UI presents the chat interface to users.

The result is a user-friendly, responsive system that offers personalized car-buying advice with a small dummy dataset.

---

## Sample Conversation

```text
User: I need to buy a car

Assistant: 
Welcome! I can certainly help you with that. I understand you're looking to buy a car.

Based on our current listings, we have several new Tesla Model Y SUVs available, all with 0 miles. This is a popular choice for those looking for a modern, electric SUV.

Here are the options we have:

Tesla Model Y, 2021 New SUV: Priced at $23,043
Tesla Model Y, 2020 New SUV: Priced at $28,625
Tesla Model Y, 2022 New SUV: Priced at $39,962
The 2021 Tesla Model Y at $23,043 stands out as an excellent value for a new SUV, especially compared to the other model years. It seems to offer a significant discount for a brand-new vehicle.

To help me recommend the best fit for you, could you tell me a bit more about what you're looking for? For example:

What's your approximate budget?
Are you interested in a specific model year or looking for the best possible value?
Are there any specific features or priorities you have in mind for your new car?
---

User: I want something under 30,000

Assistant: 
That's a great starting point! We have a couple of excellent options for you under $30,000 from our current listings:

Tesla Model Y, 2021 New SUV for $23,043
Tesla Model Y, 2020 New SUV for $28,625
Both of these are brand new Tesla Model Y SUVs and fit comfortably within your budget. The 2021 model offers the lowest price point, while the 2020 model is still well under your limit.

To help me narrow it down further for you, could you tell me:

Are you looking for the absolute lowest price, or is there a preference for a slightly newer model year if it's still within budget?
Are you specifically interested in an SUV, or are you open to other body styles?

---
User: I prefer SUVs

Assistant: 
Great! You're looking for an SUV. We have a few excellent options that might fit your needs.

Based on our current inventory, here are a couple of SUVs to consider:

2021 Toyota RAV4 (Used): Priced at $27,093 with 60,099 miles. This is a very popular and reliable compact SUV, known for its fuel efficiency and practicality. It's a great option if you're looking for a dependable used vehicle that offers solid value.
2020 Tesla Model Y (New): Priced at $28,625 with 0 miles. If you're open to an electric vehicle, this is an exceptional opportunity to get a brand new Tesla Model Y at a very competitive price. It offers cutting-edge technology, impressive performance, and zero emissions.
To help me narrow down the best fit for you, could you tell me a bit more about what you're looking for? For example:

What's your approximate budget?
Are you leaning towards a new or used vehicle?
Do you have a preference for gasoline, hybrid, or electric?
Are there any specific features or brands you prefer?

---

User: no nothing specifically

Assistant:
It sounds like you're open to exploring options, which is great! To help me narrow down the best fit for you, could you tell me a little more about what you're looking for?

For example, are you:

Thinking about a specific budget?
Interested in a particular body style (like an SUV, which is what we currently have listed)?
Looking for a new or used vehicle? (All our current listings are new.)
Once I have a better idea of your preferences, I can suggest the best Tesla Model Y for your needs!

---

User: below 30k give me one best car

Assistant:
That's a great budget to work with! Based on our current listings, for under $30,000, the 2021 Tesla Model Y New SUV at $23,043 is an excellent choice.

It's brand new with 0 miles, offering you the latest technology and electric performance without breaking your budget. This is a fantastic opportunity to get a new Tesla Model Y at a significantly reduced price, as it's the only option available below your $30,000 limit.

Would you like to know more about its features, or perhaps explore other criteria like specific body styles or brands for future options?

```
## Maintainer
**M N Nisha**  
For suggestions or collaborations, feel free to:  
- [Connect on LinkedIn](https://www.linkedin.com/in/nishareddy030399)  
- Raise an [Issue](https://github.com/nishareddy3366/AI-car-buying-assistant/tree/main) or submit a PR
