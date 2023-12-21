# Named Entity Recognition (NER) with Hugging Face API

This project utilizes the Hugging Face Model Hub to perform Named Entity Recognition (NER) using the `dslim/bert-base-NER` model. Gradio is used to create an interactive web interface for users to input text and visualize identified entities.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Named Entity Recognition (NER) with Hugging Face API project allows users to input text, and the system identifies and visualizes named entities using the `dslim/bert-base-NER` model. Gradio is used to create an interactive and user-friendly web interface for NER.

## Features

- **Named Entity Recognition:** Users can input text, and the system identifies and highlights named entities in the text.
- **Interactive Web Interface:** Gradio provides a user-friendly web interface for text input and entity visualization.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ner-huggingface-api.git
    ```

2. Change into the project directory:

    ```bash
    cd ner-huggingface-api
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

3. Enter text into the input box, and the system will identify and highlight named entities in the text.

## Dependencies

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- requests: Library for making HTTP requests.

Install the dependencies using the following:

```bash
pip install flask gradio requests
```

## Configuration 
The application uses environment variables for configuration. Ensure to set the HUGGING_FACE_API_KEY variable in the .env file with your Hugging Face API key.

## Contributing 
Contributions are welcome! 

## License
This project is licensed under the MIT License.
