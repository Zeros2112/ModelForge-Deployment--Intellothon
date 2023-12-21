# Text Summarization with BART Model

This project leverages the Hugging Face Model Hub to perform text summarization using the BART (facebook/bart-large-cnn) model. Gradio is employed to create an interactive web interface where users can input text, and the system generates a summary.

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

The Text Summarization with BART Model project enables users to input text, and the system generates a summary using the BART model from the Hugging Face Model Hub. Gradio is used to provide an interactive and user-friendly web interface for text summarization.

## Features

- **Text Summarization:** Users can input text, and the system generates a concise summary using the BART model.
- **Interactive Web Interface:** Gradio provides a user-friendly web interface for text input and summary output.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-summarization-bart.git
    ```

2. Change into the project directory:

    ```bash
    cd text-summarization-bart
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

3. Enter text into the input box, and the system will generate a summary for the input text.

## Dependencies

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- transformers: Hugging Face library for accessing the BART model.

Install the dependencies using the following:

```bash
pip install flask gradio transformers
```

## Configuration 
The application uses environment variables for configuration. Ensure to set the PORT2 variable in the .env file for the specified port.

## Contributing 
Contributions are welcome!

## License
This project is licensed under the MIT License.
