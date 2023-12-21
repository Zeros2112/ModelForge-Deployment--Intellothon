# Import necessary libraries
import gradio as gr
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Define the Hugging Face API URL and headers with authorization
API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"}  # Use the API key from the environment variable

# Define a function to merge tokens in the NER result for better readability
def merge_tokens(tokens):
    merged_tokens = []
    for token in tokens:
        if 'entity' in token and merged_tokens and token['entity'].startswith('I-') and merged_tokens[-1].get('entity', '').endswith(token['entity'][2:]):
            # If current token continues the entity of the last one, merge them
            last_token = merged_tokens[-1]
            last_token['word'] += token.get('word', '').replace('##', '')
            last_token['end'] = token.get('end', last_token['end'])
            last_token['score'] = (last_token.get('score', 0) + token.get('score', 0)) / 2
            last_token['entity'] = last_token.get('entity', '')  # Use entity from the last token
        else:
            # Otherwise, add the token to the list
            merged_tokens.append(token)

    return merged_tokens

# Define a function for named entity recognition (NER) using the Hugging Face API
def ner(input_text):
    payload = {"inputs": input_text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()
    merged_tokens = merge_tokens(result)
    return {"text": input_text, "entities": merged_tokens}

# Define a Gradio Interface for NER with text input and highlighted text output
iface = gr.Interface(fn=ner,
                    inputs=[gr.Textbox(label="Text to find entities", lines=2)],
                    outputs=[gr.HighlightedText(label="Text with entities")],
                    title="NER with dslim/bert-base-NER",
                    description="Find entities using the `dslim/bert-base-NER` model under the hood!",
                    allow_flagging="never",  # Disable user flagging for simplicity
                    examples=["My name is Zeros, I'm studying in USF and I live in Florida",
                              "My name is Hy, I live in Vietnam and my dream is to work at Tensorflow"])

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page with handling of POST requests
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text_to_ner = request.form['text']
        result = ner(text_to_ner)
        return render_template('ner_index.html', result=result)
    return render_template('ner_index.html')

# Run the Gradio Interface and Flask web application
if __name__ == '__main__':
    # Launch the Gradio Interface with sharing enabled, and use the specified port or default to 5000
    iface.launch(share=True, server_port=int(os.environ.get('PORT4', 5000)))
    
    # Run the Flask web application with debugging enabled
    app.run(debug=True)
