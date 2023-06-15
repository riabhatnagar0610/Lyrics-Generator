# Lyrics-Generator

![GitHub stars](https://img.shields.io/github/stars/riabhatnagar0610/Lyrics-Generator)
![GitHub forks](https://img.shields.io/github/forks/riabhatnagar0610/Lyrics-Generator)

A lyrics generation project that utilizes a Long Short-Term Memory (LSTM) model trained on lyrics from over 75 artists across different genres. The project is built using Python.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Lyrics-Generator project is designed to generate song lyrics based on user input. It utilizes an LSTM model trained on a large collection of lyrics from various artists to learn the patterns and structures of song lyrics. Given an initial line or phrase provided by the user, the model generates a set of lyrics that are coherent and stylistically similar to the input.

This project is built using the Flask framework, which allows for easy deployment and interaction with the generated lyrics through a web interface. The frontend is developed using HTML, CSS, and JavaScript to provide a user-friendly experience.

## Technologies Used

The Lyrics-Generator project incorporates the following technologies:

- LSTM (Long Short-Term Memory)
- Deep Learning
- Flask
- HTML
- CSS
- JavaScript
- And more...

## Installation

To set up the Lyrics-Generator project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/riabhatnagar0610/Lyrics-Generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Lyrics-Generator
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:

   ```bash
   python app.py
   ```

5. Access the application by visiting `http://localhost:5000` in your web browser.

## Usage

The main code for the Jupyter notebook can be found at `lyrics-generator-using-rnn.ipynb`

1. Open the Lyrics-Generator web application in your preferred web browser.

2. Enter an initial line or phrase in the provided input field.

3. Click the "Generate Lyrics" button.

4. Wait for the LSTM model to process the input and generate the lyrics.

5. The generated lyrics will be displayed on the screen.

6. Optionally, you can click the "Generate Again" button to generate new lyrics based on a different input.

## Contributing

Contributions to the Lyrics-Generator project are welcome and encouraged. To contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make the necessary modifications in your branch.

4. Test your changes to ensure they work as intended.

5. Submit a pull request with a detailed explanation of your changes.
