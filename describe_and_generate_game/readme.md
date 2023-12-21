# Describe-and-Generate Game 🖍️

This project combines the power of the Hugging Face Model Hub and Gradio to create an interactive game where users provide a description, and the system generates an image based on the description.

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

The "Describe-and-Generate" game allows users to describe an image in text, and the system generates an image based on the provided description. It uses the Hugging Face Model Hub to perform image captioning and image generation. Gradio is used to create an interactive web interface for users to interact with the game.

## Features

- **Interactive Interface:** Users can upload an image and receive a generated caption along with an image generated based on the provided description.
- **Integration with Hugging Face Models:** The application leverages Hugging Face's API for image captioning and image generation using pre-trained models.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Zeros2112/describe-and-generate-game.git
    ```

2. Change into the project directory:

    ```bash
    cd describe-and-generate-game
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

3. Upload an image, and the system will generate a caption along with an image based on the provided description.

## Dependencies

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- requests: Library for making HTTP requests.
- Pillow (PIL): Python Imaging Library for image processing.

Install the dependencies using the following:

```
pip install flask gradio requests pillow
```

## Configuration 
The application uses environment variables for configuration. Ensure to set the HF_API_KEY variable in the .env file with your Hugging Face API key.

## Contributing 
Contributions are welcome!

## License 
This project is licensed under the MIT License. 
