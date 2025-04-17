import asyncio
import os
from client import bot, user
from call_handler import pytgcalls
from pyrogram import idle

# Import handlers to register them
import handlers.start
import handlers.play

async def main():
    if not os.path.exists("downloads"):
        os.mkdir("downloads")

    await bot.start()
    await user.start()
    pytgcalls.client = user
    await pytgcalls.start()

    print("✅ Music Bot is running...")
    await idle()

    await bot.stop()
    await user.stop()
    await pytgcalls.stop()

if __name__ == "__main__":
    asyncio.run(main())


