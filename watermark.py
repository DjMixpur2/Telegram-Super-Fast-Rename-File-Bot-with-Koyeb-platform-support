from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_path, output_path, text="Your Watermark"):
    """Add watermark text to the bottom-left corner of an image."""
    with Image.open(input_path) as img:
        # Set watermark font and size
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)

        # Position watermark at the bottom-left corner
        width, height = img.size
        position = (10, height - text_height - 10)

        # Apply watermark
        draw.text(position, text, font=font, fill=(255, 255, 255, 128))  # White text with transparency

        # Save the image with watermark
        img.save(output_path)

def add_watermark_to_video(input_video_path, output_video_path, text="Your Watermark"):
    """Add watermark to a video."""
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

    video = VideoFileClip(input_video_path)
    watermark = TextClip(text, fontsize=24, color='white', font="Arial-Bold")
    watermark = watermark.set_pos(('left', 'bottom')).set_duration(video.duration)

    final = CompositeVideoClip([video, watermark])
    final.write_videofile(output_video_path, codec='libx264')
