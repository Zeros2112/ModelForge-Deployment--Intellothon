# Import necessary libraries
import gradio as gr
from flask import Flask, render_template, request
import os
import io
import base64
from PIL import Image

import requests
from requests.exceptions import RequestException, JSONDecodeError
import json

from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file
hf_api_key = os.environ['HF_API_KEY']

# Hugging Face API endpoints
TTI_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
ITT_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

# Define a function to make a query to the Hugging Face API
def query(payload, api_url, api_headers):
    headers = {
        "Authorization": f"Bearer {api_headers}" if api_headers else "",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Check if the response has content
        return response.json()

    except RequestException as e:
        print(f"Request error: {e}")
    except JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None  # Return None if there's an error in the request or JSON decoding

# Define a function to convert a PIL image to a base64-encoded string
def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))

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

# Define a function for image captioning using the Hugging Face API
def captioner(image):
    base64_image = image_to_base64_str(image)
    result = query({"inputs": base64_image}, ITT_API_URL, hf_api_key)
    return result[0]['generated_text']

# Define a function to generate an image based on a prompt using the Hugging Face API
def generate(prompt):
    output = query({"inputs": prompt}, TTI_API_URL, hf_api_key)
    result_image = base64_to_pil(output)
    return result_image

# Define a function to perform captioning and image generation
def caption_and_generate(image):
    caption = captioner(image)
    image_result = generate(caption)
    return [caption, image_result]

# Create a Gradio Interface using blocks
with gr.Blocks() as iface:
    gr.Markdown("# Describe-and-Generate game 🖍️")
    image_upload = gr.Image(label="Your first image", type="pil")
    btn_all = gr.Button("Caption and generate")
    caption = gr.Textbox(label="Generated caption")
    image_output = gr.Image(label="Generated Image")

    # Set the click function for the button to perform captioning and generation
    btn_all.click(fn=caption_and_generate, inputs=[image_upload], outputs=[caption, image_output])

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page with handling of POST requests
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file:
            pil_image = Image.open(uploaded_file)
            result = caption_and_generate(pil_image)
            return render_template('index.html', caption=result[0], image=result[1])
    return render_template('index.html')

# Run the Gradio Interface and Flask web application
if __name__ == '__main__':
    # Launch the Gradio Interface with sharing enabled, and use the specified port or default to 5000
    iface.launch(share=True, server_port=int(os.environ.get('PORT3', 5000)))
    
    # Run the Flask web application with debugging enabled
    app.run(debug=True)

