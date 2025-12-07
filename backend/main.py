# main.py

import os
import base64
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from pipelines.audio_answer import generate_answer_from_audio
from pipelines.simple_answer import generate_answer

load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
VOICE_REPLY_URL = os.getenv("VOICE_REPLY_URL") 
TEXT_REPLY_URL = os.getenv("TEXT_REPLY_URL")

app = FastAPI()

# ✅ Add CORS here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],        # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],        # Allow all headers
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post(VOICE_REPLY_URL)
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
    
@app.post(TEXT_REPLY_URL)
async def reply_text(request: Request):
    data = await request.json()
    user_text = data.get("text")
    result = await generate_answer(user_text)
    return {"user_text": user_text, "assistant_text": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=BACKEND_HOST, port=BACKEND_PORT)
