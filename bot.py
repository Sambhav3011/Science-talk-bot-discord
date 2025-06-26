import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command(name="ask")
async def ask_science(ctx, *, question):
    print(f"📩 Received question from {ctx.author}: {question}")
    await ctx.send("Thinking...")

    try:
        print("📡 Sending request to Groq...")
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": "You are a helpful science bot."},
                    {"role": "user", "content": question}
                ],
                "temperature": 0.7
            }
        )

        print(f"📥 Response status: {response.status_code}")
        data = response.json()

        if response.status_code == 200:
            answer = data['choices'][0]['message']['content']
            if len(answer) > 2000:
                await ctx.send("⚠️ Answer too long to display.")
            else:
                await ctx.send(f"**AI:** {answer}")
        else:
            error_msg = data.get("error", {}).get("message", "Unknown error")
            await ctx.send(f"❌ Error: {response.status_code} - {error_msg}")

    except Exception as e:
        print(f"❌ Exception: {e}")
        await ctx.send(f"❌ An error occurred: {e}")

@ask_science.error
async def ask_error(ctx, error):
    print(f"❌ Command error: {error}")
    await ctx.send("❌ Something went wrong. Make sure I'm allowed to see your messages and try again.")

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
