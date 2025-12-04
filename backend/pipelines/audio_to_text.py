from pathlib import Path
from typing import Union
from haystack.components.audio import LocalWhisperTranscriber
from haystack.dataclasses import ByteStream


# Audio transcription function: converts audio into text
def process_audio_to_text(input_data: Union[str, Path, bytes]) -> str:
    
    # Initialize the LocalWhisperTranscriber for audio-to-text conversion
    transcriber = LocalWhisperTranscriber(model="small")
    transcriber.warm_up()

    # Convert bytes input to ByteStream, leave Path/str as is
    if isinstance(input_data, bytes):
        input_data = ByteStream(input_data)
    
    # Run transcription
    transcription = transcriber.run(sources=[input_data])
    
    # Extract the text content from the transcription result
    text = transcription["documents"][0].content

    return text
