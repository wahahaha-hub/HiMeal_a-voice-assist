# main.py

import os
import base64
from fastapi import FastAPI, Request
from dotenv import load_dotenv

from pipelines.audio_answer import generate_answer_from_audio

load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
BACKEND_REPLY_URL = os.getenv("BACKEND_REPLY_URL")  # e.g. "/audio-chat"

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post(BACKEND_REPLY_URL)
async def reply(request: Request):
    data = await request.json()

    # 1. Read base64 audio string
    audio_b64 = data.get("audio")
    if not audio_b64:
        return {"error": "audio field missing"}

    audio_bytes = base64.b64decode(audio_b64)

    # 2. Process audio → Whisper → LLM answer
    user_text, result = await generate_answer_from_audio(audio_bytes)

    return {
        "user_text": user_text,
        "assistant_text": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=BACKEND_HOST, port=BACKEND_PORT)
