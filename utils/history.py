import shelve
from typing import List
from utils.config import DB_PATH

# Function to retrieve chat history for a given session
def get_history(session_id: str) -> List[str]:
    """Fetch chat history for a session."""
    with shelve.open(DB_PATH) as db:
        return db.get(session_id, [])

# Function to store a new message into chat history
def save_to_history(session_id: str, role: str, content: str):
    """Append a message to chat history for a session."""
    with shelve.open(DB_PATH, writeback=True) as db:
        history = db.get(session_id, [])
        history.append(f"{role}: {content}")
        db[session_id] = history
