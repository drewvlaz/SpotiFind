
from flask import Flask,render_template, request, session, url_for, redirect, flash
import json
import os
import io

from markupsafe import escape
from google.cloud import vision
import google.auth

credentials, project = google.auth.default()

app = Flask(__name__) #create instance of class flask

app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload")
def upload_image():
    client = vision.ImageAnnotatorClient()
    path = './test1.jpg'
    print(path)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.annotate_image({
        'image': image,
        'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
        })
    # response = client.image_properties(image=image)
    # props = response.image_properties_annotation
    # print('Properties:')
    #print(len(response))
    print(response)
    s =''
    for face in response.face_annotations:
        print("hi")
        if (face.detection_confidence > 0.7):
            s += 'joy ' + str(face.joy_likelihood) + "\n"
            s += 'sorrow ' + str(face.sorrow_likelihood) + "\n"
            s += 'anger ' + str(face.anger_likelihood)+ "\n"
            s += 'surprise ' + str(face.surprise_likelihood)+ "\n"
    print(s)
    
    
    return f'{s}'