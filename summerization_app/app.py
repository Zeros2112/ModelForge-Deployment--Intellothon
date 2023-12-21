# Import necessary libraries
import gradio as gr
from flask import Flask, render_template
import os

# Create a Flask web application
app = Flask(__name__)

# Import the summarization pipeline from the transformers library
from transformers import pipeline

# Instantiate the summarization pipeline using the BART model
get_completion = pipeline("summarization", model="facebook/bart-large-cnn")

# Define a function for text summarization using the pipeline
def summarize(input):
    # Use the pipeline to generate a summary for the input text
    output = get_completion(input)
    return output[0]['summary_text']

# Define a Gradio Interface for text input and output
iface = gr.Interface(fn=summarize, 
                    inputs=[gr.Textbox(label="Text to summarize", lines=6)],
                    outputs=[gr.Textbox(label="Result", lines=3)],
                    title="Text summarization with distilbart-cnn",
                    description="Summarize any text using the `shleifer/distilbart-cnn-12-6` model under the hood!"
                   )

# Define a route for the home page
@app.route('/')
def home():
    # Render the HTML template for the home page
    return render_template('index.html')

# Run the Gradio Interface and Flask web application
if __name__ == '__main__':
    # Launch the Gradio Interface with sharing enabled, and use the specified port or default to 5000
    iface.launch(share=True, server_port=int(os.environ.get('PORT2', 5000)))
    
    # Run the Flask web application with debugging enabled
    app.run(debug=True)

# import requests
# import gradio as gr
# from flask import Flask, render_template, request
# from dotenv import load_dotenv
# import os

# load_dotenv()  # Load environment variables from .env file

# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"}  # Use the API key from the environment variable

# def summarize(input_text):
#     payload = {"inputs": input_text}
#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     result = response.json()
#     return result[0]['generated_text']



# iface = gr.Interface(fn=summarize,
#                     inputs=[gr.Textbox(label="Text to summarize", lines=6)],
#                     outputs=[gr.Textbox(label="Result", lines=3)],
#                     title="Text summarization with facebook/bart-large-cnn",
#                     description="Summarize any text using the Hugging Face API with the `facebook/bart-large-cnn` model."
#                    )

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         text_to_summarize = request.form['text']
#         result = summarize(text_to_summarize)
#         return render_template('index.html', result=result)
#     return render_template('index.html')

# if __name__ == '__main__':
#     iface.launch(share=True, server_port=int(os.environ.get('PORT2', 5000)))
#     app.run(debug=True)
