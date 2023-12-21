# Import necessary libraries
import gradio as gr
from flask import Flask, render_template, request
import os
import base64
from PIL import Image
import io

# Import the image-to-text pipeline from the transformers library
from transformers import pipeline

# Instantiate the image-to-text pipeline using the BLIP model
get_completion = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Define a function to convert a PIL image to a base64-encoded string
def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))

# Define the captioner function using the image-to-text pipeline
def captioner(image):
    # Convert the PIL image to a base64-encoded string
    base64_image = image_to_base64_str(image)
    
    # Use the image-to-text pipeline to generate a caption
    result = get_completion(base64_image)
    return result[0]['generated_text']

# Define a Gradio Interface for image input and text output
iface = gr.Interface(fn=captioner,
                    inputs=[gr.Image(label="Upload image", type="pil")],
                    outputs=[gr.Textbox(label="Caption")],
                    title="Image Captioning with BLIP",
                    description="Caption any image using the BLIP model",
                    allow_flagging="never",  # Disable user flagging for simplicity
                    examples=["./images/congchua.png", "./images/lego-ninjago.jpg"])

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page with handling of POST requests
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded image file from the form
        uploaded_file = request.files['image']
        
        if uploaded_file:
            # Open the uploaded image as a PIL image
            pil_image = Image.open(uploaded_file)
            
            # Generate a caption for the image
            caption = captioner(pil_image)
            
            # Render the result using the HTML template
            return render_template('index.html', caption=caption)
    
    # Render the home page template
    return render_template('index.html')

# Run the Gradio Interface and Flask web application
if __name__ == '__main__':
    # Launch the Gradio Interface with sharing enabled, and use the specified port or default to 5000
    iface.launch(share=True, server_port=int(os.environ.get('PORT1', 5000)))
    
    # Run the Flask web application with debugging enabled
    app.run(debug=True)
