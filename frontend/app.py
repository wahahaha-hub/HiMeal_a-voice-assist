# frontend/app.py

import os
import streamlit as st
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = os.getenv("BACKEND_PORT")
BACKEND_REPLY_URL = os.getenv("BACKEND_REPLY_URL")
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}{BACKEND_REPLY_URL}"


st.set_page_config(
    page_title="HiMeal | Voice Assistant",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ HiMeal - Voice Assistant")
st.subheader("“您吃了吗?” — Your AI meal assistant & friendly helper")


if "messages" not in st.session_state:
    st.session_state.messages = []


# Display history
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.write(content)


# -----------------------------
# Voice input
# -----------------------------

audio_file = st.audio_input("Speak now", label_visibility="collapsed")

if audio_file is not None:
    st.info("Processing your voice...")

    # Convert to bytes
    try:
        audio_bytes = audio_file.read()
    except Exception:
        audio_bytes = audio_file

    # Encode to Base64
    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")

    payload = {
        "audio": audio_b64,
        "history": [
            {"role": r, "content": c} for r, c in st.session_state.messages
        ]
    }

    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=60)
        if response.status_code == 200:
            data = response.json()

            user_text = data.get("user_text", "")
            assistant_text = data.get("assistant_text", "")

            if user_text:
                st.session_state.messages.append(("user", user_text))
                with st.chat_message("user"):
                    st.write(user_text)

            if assistant_text:
                st.session_state.messages.append(("assistant", assistant_text))
                with st.chat_message("assistant"):
                    st.write(assistant_text)

        else:
            st.error(f"Backend error: {response.text}")

    except Exception as e:
        st.error(f"Failed to contact backend: {e}")


# -----------------------------
# Reset conversation
# -----------------------------

if st.button("🧹 Clear Conversation"):
    st.session_state.messages = []
    st.experimental_rerun()
