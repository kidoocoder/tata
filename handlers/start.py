
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("👋 Welcome! Use /play <song name> in a group to play music.")
