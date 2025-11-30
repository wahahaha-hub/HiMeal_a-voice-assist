import streamlit as st
import requests
import base64
import json

# -----------------------------
# Config
# -----------------------------
BACKEND_URL = "http://localhost:8000/api/voice"  # Update when deployed

st.set_page_config(
    page_title="HiMeal | Voice Assistant",
    page_icon="🎙️",
    layout="centered"
)

# -----------------------------
# UI Layout
# -----------------------------
st.title("🎙️ HiMeal - Voice Assistant")
st.subheader("“您吃了吗?” — Your AI meal assistant & friendly helper")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show message history in chat format
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.write(content)

# -----------------------------
# Voice Input UI
# -----------------------------
audio_bytes = st.audio_input("Speak now", label_visibility="collapsed")

if audio_bytes is not None:
    st.info("Processing your voice...")

    # FIX: Read the bytes content from the UploadedFile object
    # audio_bytes is an UploadedFile object, so we must call .read() to get the bytes
    try:
        audio_bytes_data = audio_bytes.read()
    except AttributeError:
        # Handle case where it might be a bytes-like object directly (e.g., from recording)
        audio_bytes_data = audio_bytes
        
    # Encode audio to Base64 for API
    audio_base64 = base64.b64encode(audio_bytes_data).decode("utf-8")

    payload = {
        "audio": audio_base64,
        "history": [
            {"role": r, "content": c} for r, c in st.session_state.messages
        ]
    }

    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=60)
        if response.status_code == 200:
            result = response.json()
            user_text = result.get("user_text", "")
            assistant_text = result.get("assistant_text", "")

            # Update UI history
            if user_text:
                st.session_state.messages.append(("user", user_text))
                with st.chat_message("user"):
                    st.write(user_text)

            if assistant_text:
                st.session_state.messages.append(("assistant", assistant_text))
                with st.chat_message("assistant"):
                    st.write(assistant_text)

        else:
            st.error(f"Error from backend: {response.text}")

    except Exception as e:
        st.error(f"Request failed: {e}")

# -----------------------------
# Reset Conversation
# -----------------------------
if st.button("🧹 Clear Conversation"):
    st.session_state.messages = []
    st.experimental_rerun()
