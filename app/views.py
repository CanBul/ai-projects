from app import app
from flask import Flask, jsonify, request
import warnings
from app.content import my_ids, returnMovies
warnings.filterwarnings("ignore")
from app import parkinson
from math import floor

@app.route("/api", methods=['GET'])
def index():
    return "<h1 style='color:red'>Working!!</h1>"

@app.route("/api/recompy", methods=['POST'])
def recompy():

    if request.method == 'POST':

        points = request.get_json()
        mylist = my_ids(points)
        data = returnMovies(mylist)

        return jsonify(data)


@app.route('/api/parkinson', methods=['POST'])
def parkinson():
    path = '/home/can/Desktop/fromServer.wav'
    
    if request.method == 'POST':
        request.files['audio_data'].save(path)

        img = parkinson.bw_spectrogram_image(path)
        result= parkinson.create_and_predict(img)
        
        return str(floor(result*100)/100)
    