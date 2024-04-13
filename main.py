from flask import Flask, request, render_template_string, jsonify, redirect
import librosa
from asr_inference import AsrInference
from Search import SearchEngine
import os
from werkzeug.utils import secure_filename
# from googletrans import Translator

app = Flask(__name__)
asr = AsrInference(model_name='openai/whisper-small')
se = SearchEngine()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Whisper</title>
</head>
<body>
    <h1>Whisper ASR API</h1>
</body>
</html>
"""

@app.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template_string(TEMPLATE)
    
    text = ""
    if request.method=='POST':
        if 'file' not in request.files:
            return dict(request.get_json())
        
        file = request.files['file']

        if file.filename == "":
            return 'No file selected.', 400
         # save the file
        temp_filepath = os.path.join(os.getcwd(), 'Audios', secure_filename(file.filename))
        file.save(temp_filepath)
        
        
        audio, _= librosa.load(temp_filepath, sr=16_000)
        result = asr.transcribe(audio)
        return jsonify(result)

@app.route('/translate', methods=['POST'])
def translate():
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            audio, _= librosa.load(file, sr=16_000)
            result = asr.translate(audio)
            return jsonify(result)
        
@app.route('/hotel', methods=['POST'])
def get_hotels():
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            audio, _= librosa.load(file, sr=16_000)
            query = asr.translate(audio)
            result = se.searchHotels(query)
            return jsonify(result)

@app.route('/restaurant', methods=['POST'])
def get_resturants():
     if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            audio, _= librosa.load(file, sr=16_000)
            query = asr.translate(audio)
            result = se.searchRestaurants(query)
            return jsonify(result)
        
@app.route('/attraction', methods=['POST'])
def get_attr():
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            audio, _= librosa.load(file, sr=16_000)
            query = asr.translate(audio)
            result = se.searchAttr(query)
            return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
