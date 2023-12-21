import io
import base64
from PIL import Image
# Define a function to convert a base64-encoded string to a PIL image
def base64_to_pil(img_base64):
    if img_base64 is None:
        print("Error: img_base64 is None.")
        return None  # Handle the case where img_base64 is None

    try:
        base64_decoded = base64.b64decode(img_base64)
        byte_stream = io.BytesIO(base64_decoded)
        pil_image = Image.open(byte_stream)
        return pil_image
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return None
