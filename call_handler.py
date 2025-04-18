from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.exceptions import GroupCallNotFoundError

from pyrogram import Client
from config import API_ID, API_HASH, SESSION

# Create Pyrogram Client and PyTgCalls instance
app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

# Dictionary to track current chats and their stream status
active_chats = {}

@pytgcalls.on_stream_end()
async def on_stream_end_handler(client: PyTgCalls, update: Update):
    chat_id = update.chat_id
    print(f"Stream ended in chat {chat_id}")
    active_chats.pop(chat_id, None)
    # You can add logic to play next track here if using a queue system

async def start_stream(chat_id: int, audio_file: str):
    """
    Start streaming an audio file in the given voice chat.
    :param chat_id: Telegram group voice chat ID
    :param audio_file: Local path to audio file (must be raw PCM .raw or use ffmpeg with pipe)
    """
    try:
        await pytgcalls.join_group_call(
            chat_id,
            InputAudioStream(audio_file),
        )
        active_chats[chat_id] = audio_file
        print(f"Started streaming in chat {chat_id}")
    except GroupCallNotFoundError:
        print(f"Group call not found in chat {chat_id}")

async def stop_stream(chat_id: int):
    """
    Stops the current stream in the given chat.
    """
    if chat_id in active_chats:
        await pytgcalls.leave_group_call(chat_id)
        active_chats.pop(chat_id, None)
        print(f"Stopped streaming in chat {chat_id}")

def get_active_chats():
    return active_chats

