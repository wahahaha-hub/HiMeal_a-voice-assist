import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv

from pipelines.simple_answer import generate_answer


load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
BACKEND_TITLE = os.getenv("BACKEND_TITLE")
BACKEND_REPLY_URL = os.getenv("BACKEND_REPLY_URL")


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post(BACKEND_REPLY_URL)
async def reply(request: Request):
    data = await request.json()
    reply = await generate_answer(data['query'])
    return {"message": reply}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=BACKEND_HOST, port=BACKEND_PORT)