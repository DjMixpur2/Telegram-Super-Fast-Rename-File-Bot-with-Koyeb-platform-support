import os

class Config:
    BOT_TOKEN = os.getenv("7994263128:AAE7dWuOWMjZSgr6C2XIODltb0ZOQ5laVQQ")  # Telegram bot token
    API_ID = int(os.getenv("12850056"))  # Telegram API ID
    API_HASH = os.getenv("15564ec4a1a2cbef87c99a9aa9e40b34")  # Telegram API hash
    KOYEB_WEBHOOK = os.getenv("https://repulsive-gussy-kdbhai-b2e6c353.koyeb.app")  # Koyeb Webhook URL
    WATERMARK_TEXT = "@KrBackup"  # Customize this text for watermark
    THUMBNAIL_PATH = os.getenv("THUMBNAIL_PATH", "thumbnail.jpg")  # Custom thumbnail path
