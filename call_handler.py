from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.quality import HighQualityAudio
from config import API_ID, API_HASH, SESSION  # Make sure config.py contains these variables

# Initialize Pyrogram client
app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)

# Initialize PyTgCalls client
pytgcalls = PyTgCalls(app)

# Function to start the stream
async def start_stream(chat_id: int, audio_file: str):
    await pytgcalls.join_group_call(
        chat_id,
        InputAudioStream(
            audio_file,
            HighQualityAudio()
        )
    )

# Function to stop the stream
async def stop_stream(chat_id: int):
    await pytgcalls.leave_group_call(chat_id)
