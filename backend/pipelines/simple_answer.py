# services/llm_service.py

from haystack import Pipeline
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage

from util.config import LLMConfig


# Create your generator only once (good for performance)
qwen_generator = OpenAIChatGenerator(
    model=LLMConfig.LLM_MODEL_NAME,
    api_base_url=LLMConfig.LLM_URL,
)

# Create pipeline only once
simple_answer_pipeline = Pipeline()
simple_answer_pipeline.add_component("llm", qwen_generator)


async def generate_answer(user_text: str) -> str:
    messages = [ChatMessage.from_user(user_text)]

    # Haystack run() is sync → run in a thread
    from anyio.to_thread import run_sync
    result = await run_sync(
        simple_answer_pipeline.run,
        {"llm": {"messages": messages}},
    )

    return result["llm"]["replies"][0].text
