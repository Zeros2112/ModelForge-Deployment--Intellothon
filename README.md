# Hugging Face Model Hub Applications

This repository contains multiple applications leveraging the Hugging Face Model Hub for various natural language processing tasks. Each application comes with its own Flask web interface and, where applicable, Gradio for user interaction.

## Table of Contents
- [Introduction](#introduction)
- [Applications](#applications)
    - [Text Summarization with BART Model](#text-summarization-with-bart-model)
    - [Image Captioning with BLIP Model](#image-captioning-with-blip-model)
    - [Named Entity Recognition (NER) with BERT Model](#named-entity-recognition-ner-with-bert-model)
    - [Describe-and-Generate Game](#describe-and-generate-game)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository hosts applications that showcase the capabilities of various models available on the Hugging Face Model Hub. Each application is designed to solve a specific natural language processing task and provides an interactive interface for users to interact with the models.

## Applications

### Text Summarization with BART Model

The Text Summarization with BART Model application allows users to input text, and the system generates a summary using the BART model from the Hugging Face Model Hub. Gradio provides an interactive and user-friendly web interface for text summarization.

#### Features

- **Text Summarization:** Users can input text, and the system generates a concise summary using the BART model.
- **Interactive Web Interface:** Gradio provides a user-friendly web interface for text input and summary output.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

#### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Zeros2112/text-summarization-bart.git
    ```

2. Change into the project directory:

    ```bash
    cd text-summarization-bart
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

#### Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter text into the input box, and the system will generate a summary for the input text.

#### Dependencies

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- transformers: Hugging Face library for accessing the BART model.

Install the dependencies using the following:

```bash
pip install flask gradio transformers
```

### Image Captioning with BLIP Model

The Image Captioning with BLIP Model application allows users to upload an image, and the system generates a caption using the BLIP model from the Hugging Face Model Hub.

#### Features 
- **Image Captioning:** Users can upload an image, and the system generates a caption using the BLIP model.
- **Interactive Web Interface:** Gradio provides a user-friendly web interface for image input and caption output.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

#### Installation 

1. Clone the repository

```
   git clone https://github.com/Zeros2112/image-captioning-blip.git
```

2. Change into the project directory

```
   cd image-captioning-blip
```

3. Install the required dependencies

```
pip install -r requirements.txt
```

#### Usage 

1. Run the Flask application

```
python app.py
```

2. Open a web browser and go to http://127.0.0.1:5000/.
3. Upload an image, and the system will generate a caption for the image.

#### Dependencies 

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- transformers: Hugging Face library for accessing the BLIP model.
  
Install the dependencies using the following:
```
pip install flask gradio transformers
```

### Named Entity Recognition (NER) with BERT Model

The Named Entity Recognition (NER) with BERT Model application allows users to input text, and the system identifies and visualizes named entities using the BERT model from the Hugging Face Model Hub.

#### Features

- **Named Entity Recognition:** Users can input text, and the system identifies and highlights named entities in the text.
- **Interactive Web Interface:** Gradio provides a user-friendly web interface for text input and entity visualization.
- **Scalable:** The system is designed to be easily scalable, allowing for the integration of additional models or features.

#### Installation

Clone the repository:

```
git clone https://github.com/Zeros2112/ner-bert.git
```

Change into the project directory:

```
cd ner-bert
```

Install the required dependencies:


#### Usage

Run the Flask application:

```
python app.py
```

Open a web browser and go to http://127.0.0.1:5000/.

Enter text into the input box, and the system will identify and highlight named entities in the text.

#### Dependencies

- Flask: Web framework for building the application.
- Gradio: Library for creating interactive web interfaces.
- requests: Library for making HTTP requests.
- Install the dependencies using the following:

```
pip install flask gradio requests
```

### Describe-and-Generate Game
The Describe-and-Generate Game application is an interactive game where users upload an image, the system generates a caption for the image, and then uses the caption as a prompt to generate a new image.

#### Features

- **Interactive Game:** Users can upload an image, generate a caption, and then use the caption to generate a new image.
- **Gradio Interface:** Gradio is used to create an interactive web interface for image input and output.
- **Hugging Face API Integration:** The application uses the Hugging Face API to perform image captioning and generation.

#### Installation

```
git clone https://github.com/Zeros2112/describe-and-generate.git
```

Change into the project directory:

```
cd describe-and-generate
```

Install the required dependencies:

```
pip install -r requirements.txt
```




