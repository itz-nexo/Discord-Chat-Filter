import discord
from discord.ext import commands
import aiohttp
import asyncio

# ====================== CONFIGURATION ======================

intents = discord.Intents.default()
intents.message_content = True   

bot = commands.Bot(command_prefix="!", intents=intents)

SOURCE_CHANNEL_ID = 1234567890
WEBHOOK_URL = "https://discord.com/..."

CUSTOM_WORDS = ["fuck", "shit", "damn"]

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != SOURCE_CHANNEL_ID:
        return

    content = message.content.strip().lower()  # lowercase for case-insensitive matching
    user_id = message.author.id

    # Check if any custom word appears in the message
    should_mirror = any(word in content for word in CUSTOM_WORDS)

    if not should_mirror:
        return  # Ignore messages without any custom word


    try:
        await message.delete()
    except discord.Forbidden:
        print(f"❌ Missing 'Manage Messages' permission to delete {message.author.name}'s message.")
        return
    except Exception as e:
        print(f"❌ Delete failed: {e}")
        return

    await asyncio.sleep(1)


    try:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await webhook.send(
                content=message.content,  
                username=message.author.name,
                avatar_url=message.author.display_avatar.url,
                allowed_mentions=discord.AllowedMentions.none()
            )
    except Exception as e:
        print(f"❌ Webhook send failed: {e}")

bot.run("BOT TOKEN") # replace with your bot token