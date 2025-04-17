from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.exceptions import AlreadyJoinedError

from pyrogram import Client
import asyncio

# Create the PyTgCalls client using your main Pyrogram client
pytgcalls = PyTgCalls(Client("user_session"))

# A simple dictionary to track active group calls and queues (if needed)
active_chats = {}

@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: StreamAudioEnded):
    chat_id = update.chat_id
    print(f"Stream ended in chat {chat_id}")
    await pytgcalls.leave_group_call(chat_id)
    if chat_id in active_chats:
        del active_chats[chat_id]

async def join_and_play(client, message, audio_path: str):
    chat_id = message.chat.id

    try:
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(audio_path),
        )
        active_chats[chat_id] = audio_path
        await message.reply_text("🎵 Playing now in voice chat.")
    except AlreadyJoinedError:
        await pytgcalls.change_stream(
            chat_id,
            AudioPiped(audio_path)
        )
        await message.reply_text("🎵 Stream changed successfully.")

async def leave_call(chat_id: int):
    if chat_id in active_chats:
        await pytgcalls.leave_group_call(chat_id)
        del active_chats[chat_id]
