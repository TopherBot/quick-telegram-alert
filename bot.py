import os
import sys
import json
import urllib.request

# ---------------------------------------------------------------------
# Configuration – read from environment variables
# ---------------------------------------------------------------------
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not TOKEN or not CHAT_ID:
    sys.stderr.write('Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in the environment.\n')
    sys.exit(1)

# ---------------------------------------------------------------------
# Helper to send a message via Telegram Bot API
# ---------------------------------------------------------------------
def send_message(text: str) -> None:
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    data = json.dumps(payload).encode('utf-8')
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        resp_data = resp.read().decode('utf-8')
        # Optional: print response for debugging
        # print('Telegram response:', resp_data)

# ---------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------
if __name__ == '__main__':
    message = '🚀 Service started!'
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    send_message(message)
    print('✅ Notification sent to Telegram.')
