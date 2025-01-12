import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram bot token
    API_ID = int(os.getenv("API_ID"))  # Telegram API ID
    API_HASH = os.getenv("API_HASH")  # Telegram API hash
    KOYEB_WEBHOOK = os.getenv("KOYEB_WEBHOOK")  # Koyeb Webhook URL
    WATERMARK_TEXT = "Your Watermark"  # Customize this text for watermark
    THUMBNAIL_PATH = os.getenv("THUMBNAIL_PATH", "thumbnail.jpg")  # Custom thumbnail path
