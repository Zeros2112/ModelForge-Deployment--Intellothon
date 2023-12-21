# Chatbot using DialoGPT

This is a simple Flask web application that implements a chatbot using the DialoGPT-large model from Microsoft. Users can interact with the chatbot by sending messages through the web interface.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/chatbot-dialoGPT.git
    ```

2. Change into the project directory:

    ```bash
    cd chatbot-dialoGPT
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a message in the chatbox and press "Send." The chatbot will respond with a generated message.

## Dependencies

- Flask: Web framework for building the application.
- transformers: Hugging Face library for accessing the DialoGPT model.
- torch: PyTorch library for handling deep learning functionalities.

Install the dependencies using the following:

```
pip install flask transformers torch
```

## Model 
The chatbot uses the microsoft/DialoGPT-large model from the Hugging Face Model Hub. This model is a large-scale generative language model fine-tuned for dialogue generation.

For more information on DialoGPT, refer to the official repository.

## Contributing 
Contributions are welcome!

## License
This project is licensed under the MIT License. 



