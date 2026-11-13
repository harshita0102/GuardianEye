from io import BytesIO

def image_to_bytes(pil_image, image_format="PNG"):
    buffer = BytesIO()
    pil_image.save(buffer, format=image_format)
    return buffer.getvalue()
