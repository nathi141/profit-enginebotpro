import os
import asyncio
from telegram import Bot
from datetime import datetime

# ================= CONFIG =================
# Bot token from BotFather (set as environment variable in Render)
TOKEN = os.getenv("8576428135:AAETVabaVegIoC4gnOEiRVlmdbJ3T8i4BpE")  

# Channels and group info
CHANNEL_1 = "@DigitalAdCentral"   # Replace with your first channel username
CHANNEL_2 = "@GlobalAds_Hub"   # Replace with your second channel username

# Messages and images
messages = [
    "💸 Ready to make money online? Stay active!",
    "🚀 Your breakthrough is closer than you think!",
    "🔥 Smart people are earning daily—why not you?",
    "💼 Turn your phone into a money machine!",
]

images = [
    "https://picsum.photos/600/400",
    "https://picsum.photos/600/401",
    "https://picsum.photos/600/402",
]

# ================= BOT SETUP =================
bot = Bot(token=TOKEN)

async def post_content():
    i = 0
    while True:
        try:
            msg = messages[i % len(messages)]
            img = images[i % len(images)]
            caption = f"{msg}\n\n⏰ {datetime.now().strftime('%H:%M')}"

            # Send to channels
            await bot.send_photo(CHANNEL_1, img, caption=caption)
            await bot.send_photo(CHANNEL_2, img, caption=caption)

            # Send to group
            await bot.send_photo(GROUP_ID, img, caption=caption)

            print(f"[{datetime.now().strftime('%H:%M:%S')}] Posted successfully!")

            i += 1

        except Exception as e:
            print(f"Error: {e}")

        # Wait 1 hour before posting next
        await asyncio.sleep(3600)

# Run the bot
if __name__ == "__main__":
    print("🚀 ProfitEngineBot is starting...")
    asyncio.run(post_content())
