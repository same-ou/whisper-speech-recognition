# Whisper Speech Recognition Deployment

## Overview
This repository contains a deployment of the Whisper speech recognition model using Flask and Python. Whisper is a cutting-edge speech recognition model designed to accurately transcribe speech input into text.

## Features
  * RESTful API: Access Whisper's capabilities through a user-friendly RESTful API for seamless integration with your applications.
  * Customizable Configuration: Configure Whisper's parameters and settings to suit your specific speech recognition needs.
## Getting Started
1. Clone the Repository: Begin by cloning this repository to your local machine.
```bash
git clone git@github.com:same-ou/whisper-speech-recognition.git
```
2. Install Dependencies: Navigate to the project directory and install the required Python dependencies.
```bash
cd whisper-speech-recognition
pip install requirements.txt
```
4. Run the Application: Start the Flask server to run the Whisper speech recognition model deployment.
```bash
python app.py
```
5. Access the API: Once the Flask server is running, you can access the Whisper API at http://localhost:5000.
   
## API Endpoints

**POST /translate**: Submit audio data to the API endpoint for speech recognition. The response will contain the transcribed text.

## Example Usage

```python
import requests

url = 'http://localhost:5000/recognize'
audio_file = open('path-to-your-audio-file.wav', 'rb')
files = {'file': ('audio.wav', audio_file, 'audio/wav')}
response = requests.post(url, files=files)

print(response.json())
```
## Connect With Me
Have feedback, suggestions, or questions about the Whisper speech recognition deployment? Feel free to connect with me:

Email: [elhadramidev@gmail.com](mailto:elhadramidev@gmail.com)       |       Linkedin: [OUSSAMA EL HADRAMI](https://www.linkedin.com/in/elhadrami-oussama/)

Happy coding! 🚀✨
