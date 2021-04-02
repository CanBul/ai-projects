from app import app
from flask import Flask, jsonify, request
import warnings
from app.content import my_ids, returnMovies
warnings.filterwarnings("ignore")

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



    