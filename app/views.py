from app import app
from flask import Flask, jsonify, request
import warnings
warnings.filterwarnings("ignore")

@app.route("/api", methods=['GET', 'POST'])
def index():
    return "<h1 style='color:blue'>Hello There!</h1>"

    