from pyrogram import Client, filters
from pyrogram.types import Message
from downloader import download_audio
from call_handler import join_and_play

@Client.on_message(filters.command("play") & filters.group)
async def play_handler(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Provide a song name. Example: /play tum hi ho")

    query = " ".join(message.command[1:])
    msg = await message.reply("🔍 Searching for the song...")

    try:
        file_path, title = download_audio(query)
        await join_and_play(message.chat.id, file_path)
        await msg.edit(f"🎶 Now Playing: **{title}**")
    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

