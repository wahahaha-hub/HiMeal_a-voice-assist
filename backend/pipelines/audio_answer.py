from pipelines.audio_to_text import process_audio_to_text
from pipelines.simple_answer import generate_answer


async def generate_answer_from_audio(audio_input: bytes):
    user_text = process_audio_to_text(audio_input)
    answer = await generate_answer(user_text)
    return user_text, answer