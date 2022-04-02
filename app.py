
from flask import Flask,render_template, request, session, url_for, redirect, flash
import json
import os

from markupsafe import escape
from google.cloud import vision

app = Flask(__name__) #create instance of class flask

app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload")
def upload_image():
    client = vision.ImageAnnotatorClient()
    response = client.annotate_image({
        'image': {'source': {'image_uri': './test3.jpg'}},
        'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
    })
    print(response.annotations)  
    
    return "<p>Hello, World!</p>"