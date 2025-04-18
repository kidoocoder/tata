from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pyrogram import Client
from config import API_ID, API_HASH, SESSION

# Create the Pyrogram client and PyTgCalls instance
app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

# Start a stream
async def start_stream(chat_id, audio_file_path):
    await pytgcalls.join_group_call(
        chat_id,
        InputAudioStream(
            audio_file_path,
            HighQualityAudio()
        )
    )

# Stop a stream
async def stop_stream(chat_id):
    await pytgcalls.leave_group_call(chat_id)
