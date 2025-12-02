import os
from dotenv import load_dotenv


load_dotenv()


class LLMConfig:
    LLM_TYPE = os.getenv("LLM_TYPE")
    LLM_URL = os.getenv("LLM_URL")
    LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")
    
