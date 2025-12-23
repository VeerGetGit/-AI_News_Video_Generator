
import asyncio
from edge_tts import Communicate

async def generate_audio(script, output_file="audio.mp3", voice="en-US-GuyNeural"):
    communicate = Communicate(script, voice)
    await communicate.save(output_file)
