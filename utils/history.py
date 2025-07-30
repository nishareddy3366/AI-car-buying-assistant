import shelve
from typing import List
from utils.config import DB_PATH

def get_history(session_id: str) -> List[str]:
    """Fetch chat history for a session."""
    with shelve.open(DB_PATH) as db:
        return db.get(session_id, [])

def save_to_history(session_id: str, role: str, content: str):
    """Append a message to chat history for a session."""
    with shelve.open(DB_PATH, writeback=True) as db:
        history = db.get(session_id, [])
        history.append(f"{role}: {content}")
        db[session_id] = history
