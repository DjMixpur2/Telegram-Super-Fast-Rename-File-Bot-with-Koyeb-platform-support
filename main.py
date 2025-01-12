import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from watermark import add_watermark, add_watermark_to_video
from thumbnail import create_thumbnail
import requests

app = Client(
    "rename_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text("Hello! Send me any file, and I'll rename it for you. You can also add a custom thumbnail and watermark.")

@app.on_message(filters.document & filters.private)
async def rename_file(client, message: Message):
    file = message.document
    await message.reply_text("Send me the new file name (with extension).")

    # Wait for the user to reply with the new file name
    reply = await client.listen(message.chat.id)
    new_file_name = reply.text

    # Download the file
    file_path = await client.download_media(file)
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # Add watermark and custom thumbnail based on file type
    if file.mime_type.startswith("video/"):
        # Add watermark and create a thumbnail for video
        add_watermark_to_video(file_path, new_file_path, text=Config.WATERMARK_TEXT)
        create_thumbnail(file_path, "thumbnail.jpg", text="Video Thumbnail")
    else:
        # Add watermark for image
        add_watermark(file_path, new_file_path, text=Config.WATERMARK_TEXT)
        create_thumbnail(file_path, "thumbnail.jpg", text="Image Thumbnail")

    # Send the renamed file with watermark and custom thumbnail
    await client.send_document(
        chat_id=message.chat.id,
        document=new_file_path,
        caption=f"Renamed to {new_file_name}",
        thumb="thumbnail.jpg"  # Custom thumbnail
    )

    # Clean up the files
    os.remove(file_path)
    os.remove(new_file_path)
    os.remove("thumbnail.jpg")

if __name__ == "__main__":
    app.run()
