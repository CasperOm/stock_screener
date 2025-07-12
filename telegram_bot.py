import os, requests

def send_telegram_message(message):
    token = "8122215745:AAEBaDZNqNPv4siv3sIKOrZj5GBishSJz5E"
    chat_id = "690837316"
    if not token or not chat_id:
        raise Exception("Missing BOT_TOKEN or CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    r = requests.get(url, params=payload)
    return r.status_code