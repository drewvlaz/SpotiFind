from flask import Flask,render_template, request, session, url_for, redirect, flash
import json
import os
import io
import requests

from markupsafe import escape
from google.cloud import vision
import google.auth
from matching import *
from SpotifyClient import *
from statistics import variance, mean

import random
import math


credentials, project = google.auth.default()
def_prob = ['VERY_UNLIKELY', 'UNLIKELY', 'NEUTRAL', 'LIKELY','VERY_LIKELY']

app = Flask(__name__) #create instance of class flask

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
    #print(response)
    s =''
    all_emotes = []
    for face in response.face_annotations:
        print("hi")
        if (face.detection_confidence >= 0.8):
            print(str(face.joy_likelihood).split('.')[-1])
            j = def_prob.index(str(face.joy_likelihood).split('.')[-1])
            s = def_prob.index(str(face.sorrow_likelihood).split('.')[-1])
            a = def_prob.index(str(face.anger_likelihood).split('.')[-1])
            e = def_prob.index(str(face.surprise_likelihood).split('.')[-1])
            emotions = [j, s, a, e]
            all_emotes.append(emotions)
    print(all_emotes)
    pid = match_emotion(all_emotes)
    playlist = generate_similar_playlist(pid)
    
    return f'{playlist}'

@app.route("/color")
def find_color():
    client = vision.ImageAnnotatorClient()
    path = './test1.jpg'
    print(path)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.annotate_image({
        'image': image,
        'features': [{'type_': vision.Feature.Type.IMAGE_PROPERTIES}]
        })
    prop = response.image_properties_annotation.dominant_colors.colors
    #print(prop)
    color_tuple = []
    #print(prop.colors)
    for x in prop:
        #print(x)
        rgb = x.color
        abx = (rgb.red, rgb.green, rgb.blue, round(float(x.pixel_fraction), 3))
        color_tuple.append(abx)
    print(color_tuple)
    pid = match_color(color_tuple[0])
    trax = generate_similar_playlist(pid)

    return f'{trax}'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")


def image_to_labels():
    client = vision.ImageAnnotatorClient()
    path = './test2.jpg'
    print(path)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.annotate_image({
        'image': image,
        'features': [{'type_': vision.Feature.Type.LABEL_DETECTION}]
        })
    print(response)
    
    labels = ''
    keywords = []
        
    for label in response.label_annotations:
        if (label.score > 0.7):
            keywords += [label.description]
            labels += label.description + "\n" + str(label.score) + "\n"
    print(keywords)
    
    urls = labels_rec(keywords)
    print(urls)
    return f'{urls}' 
