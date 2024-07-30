# Sentiment Analyzer using Hugging Face

## Introduction
This project is a sentiment analyzer built using the Hugging Face `transformers` library. It utilizes state-of-the-art NLP models to classify text into different sentiment categories. The project is developed in PyCharm and includes an interactive user interface using Gradio.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)
5. [License](#license)

## Features
- **State-of-the-art NLP models**: Uses Hugging Face `transformers` for sentiment analysis.
- **Interactive UI**: Includes a web-based interface built with Gradio.
- **Data Processing**: Utilizes `pandas` for data manipulation and `matplotlib` for visualizations.
- **Export Capabilities**: Supports exporting results to Excel and Word documents using `openpyxl` and `python-docx`.

## Installation
To install the necessary dependencies, clone the repository and run:

```bash
git clone https://github.com/janki-purohit/sentiment-analyzer.git
cd sentiment-analyzer
pip install -r requirements.txt
```
## Usage
To run the sentiment analyzer, use the following command:

```
python app.py
```
### Example

Here's an example of how to use the sentiment analyzer:

1. Launch the application using the command above.
2. Open the web interface provided by Gradio.
3. Upload product review doc file.
4. View the sentiment classification results.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### requirements.txt

```plaintext
transformers
torch
gradio
pandas
matplotlib
openpyxl
python-docx
```

