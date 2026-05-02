# Discord Chat Filter

A Discord bot that automatically deletes messages containing **custom keywords** (e.g., profanity) and reposts them to another channel using a **webhook** – preserving the original user’s username and avatar.

## ✨ Features

- 🔍 **Keyword detection** – case‑insensitive, fully configurable word list  
- 🗑️ **Automatic deletion** – removes the offending message instantly  
- 🕒 **1‑second delay** – avoids Discord rate limits  
- 🧵 **Webhook mirroring** – reposts the message as if the user sent it elsewhere  
- 👤 **Preserves identity** – uses the original user’s name and avatar  
- 🔒 **Permission aware** – checks for `Manage Messages` before deletion  

## 🚀 How it works

1. User sends a message in a monitored channel.  
2. If the message contains any word from `CUSTOM_WORDS` (e.g., `fuck`, `shit`), the bot deletes it.  
3. After 1 second, the bot sends the original content via a **webhook** in your target channel, using the user’s name and avatar.  

## ⚙️ Configuration

Edit the following variables in the script:

```python
SOURCE_CHANNEL_ID = 1234567890            # Channel ID to monitor words
WEBHOOK_URL = "https://discord.com/..."   # Your webhook URL
CUSTOM_WORDS = ["fuck", "shit", "damn"]   # Words that trigger the filter
