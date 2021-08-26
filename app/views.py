from app import app
from flask import Flask, jsonify, request
import warnings
from app.content import my_ids, returnMovies
warnings.filterwarnings("ignore")
from app import parkinson
from math import floor
from app.predict import OffensivePredict

predict = OffensivePredict()
parkinson_model = parkinson.create_and_predict()

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
def parkinson_route():
    path = '/home/can/ai-projects/app/fromServer.wav'
    
    if request.method == 'POST':
        request.files['audio_data'].save(path)

        img = parkinson.bw_spectrogram_image(path)
        result= parkinson_model.predict(img)
        
        return str(floor(result*100)/100)
@app.route('/api/offensive', methods=['POST'])
def offensive_route():
    
    
    if request.method == 'POST':
        
        message = request.get_json()
        
        
        score = predict(message)[1]
        
        return jsonify(score)
        
    
    
    