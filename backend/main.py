import os
from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
BACKEND_TITLE = os.getenv("BACKEND_TITLE")
BACKEND_REPLY_URL = os.getenv("BACKEND_REPLY_URL")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get(BACKEND_REPLY_URL)
def reply():
    return {"message": "Hello, have you eaten?"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=BACKEND_HOST, port=BACKEND_PORT)