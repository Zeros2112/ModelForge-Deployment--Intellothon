# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Create a Flask web application
app = Flask(__name__)

# Set the logging verbosity of transformers to error to suppress unnecessary warnings
transformers.logging.set_verbosity_error()

# Define the pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for handling incoming messages
@app.route('/send_message', methods=['POST'])
def send_message():
    # Retrieve the user's message from the JSON payload
    user_message = request.json['message']
    
    # Encode the user's message and generate a response using the model
    input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=0,
        temperature=0.2,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode the model's response and remove special tokens
    bot_response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # Return the response in JSON format
    return jsonify({'response': bot_response})

# Run the Flask web application
if __name__ == '__main__':
    app.run(debug=True)
