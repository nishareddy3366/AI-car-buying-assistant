
import streamlit as st
import requests

st.set_page_config(page_title="Car Chat Assistant", layout="wide")
st.title("Car Assistant Chatbot")

API_URL = "http://localhost:8000/chat"

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.subheader("🔧 Controls")
    if st.button("Clear Conversation"):
        st.session_state.chat_history.clear()
        st.rerun()
    st.caption("Backend: `/chat` endpoint")

# Display conversation
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input field
query = st.chat_input("Type your car-related question...")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.chat_history.append({"role": "user", "content": query})

    with st.spinner("Generating response..."):
        try:
            response = requests.post(API_URL, json={"message": query}, timeout=30)
            if response.status_code == 200:
                result = response.json()
                reply = result.get("response", "⚠️ Empty response received.")
                st.chat_message("assistant").markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
            else:
                try:
                    error_detail = response.json().get("detail", response.text)
                except Exception:
                    error_detail = response.text
                st.chat_message("assistant").markdown(f"⚠️ Error {response.status_code}: {error_detail}")
        except Exception as ex:
            st.chat_message("assistant").markdown(f"⚠️ Exception: {ex}")
