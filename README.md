# quick-telegram-alert

A tiny, zero‑dependency Python project that posts a message to a Telegram chat as soon as you run it.

## Features
- One‑file implementation (`bot.py`).
- Uses only the built‑in `urllib` library (no external packages required).
- Configurable via environment variables.
- Ideal for CI/CD pipelines, cron jobs, or any quick‑fire notification.

## Setup
1. **Create a Telegram Bot**
   - Talk to [@BotFather](https://t.me/BotFather) and get a *Bot Token*.
2. **Get the Chat ID**
   - Add the bot to a group or start a private chat with it, then use the `getUpdates` method or a simple script to retrieve the `chat_id`.
3. **Export environment variables**
   ```bash
   export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
   export TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
   ```
4. **Run the script**
   ```bash
   python3 bot.py "Your launch message here"
   ```

If you omit the message argument, a default *"🚀 Service started!"* will be sent.

## License
MIT – see the `LICENSE` file if you add one later.
