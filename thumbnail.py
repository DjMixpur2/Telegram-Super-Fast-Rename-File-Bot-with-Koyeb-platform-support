from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(input_path, output_path, text="Custom Thumbnail"):
    """Create a custom thumbnail for an image or video."""
    with Image.open(input_path) as img:
        # Create a new image for thumbnail
        thumbnail = img.copy()
        thumbnail.thumbnail((300, 300))  # Resize the image to fit a thumbnail

        # Add text to the thumbnail
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(thumbnail)
        text_width, text_height = draw.textsize(text, font)
        position = (10, thumbnail.height - text_height - 10)
        draw.text(position, text, font=font, fill=(255, 255, 255))

        # Save the thumbnail
        thumbnail.save(output_path)
