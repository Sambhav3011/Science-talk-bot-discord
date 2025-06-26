# 🧪 Science Talk Discord Bot

A simple, AI-powered Discord bot that answers science-related questions using Groq's LLaMA-3 model. Just ask a question with `!ask`, and the bot will respond like a helpful science expert.

---

## 🚀 Features

- 🤖 Powered by Groq's blazing-fast LLaMA 3 70B model
- 🧠 Intelligent and informative science responses
- 💬 Easy-to-use `!ask` command
- 🔒 Secure configuration using environment variables

---

## 🛠️ Setup Instructions

### 1. Clone or Download the Repository

You can either clone it using Git or download it manually from GitHub.

```bash
git clone https://github.com/yourusername/science-talk-bot.git
cd science-talk-bot
```
### 2. Install Dependencies

Make sure you have Python 3.8+ installed. Then install required packages:

```bash
pip install -r requirements.txt
```

### 3. Create a .env File

Create a .env file in the project root with the following content:

```env
DISCORD_BOT_TOKEN=your-discord-bot-token-here
GROQ_API_KEY=your-groq-api-key-here
```

Never upload this .env file to GitHub. It contains sensitive keys.

### 4. Run the Bot

```bash
python bot.py
```

### 💬 Usage

In any Discord server where the bot is added, use the command:

```csharp
!ask What is quantum entanglement?
```

The bot will respond with an intelligent, AI-generated explanation.

NOTE: Due to some issue it only works in DMs and not in server.
