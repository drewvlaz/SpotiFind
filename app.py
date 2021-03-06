from flask import Flask,render_template, request, session, url_for, redirect, flash, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import json
import os
import io
# import requests
# import urllib
import wget

from markupsafe import escape
from google.cloud import vision
import google.auth
from matching import *
from SpotifyClient import *
from statistics import variance, mean

import random
import math

imagepath = './applejeans.jpg'

credentials, project = google.auth.default()
def_prob = ['VERY_UNLIKELY', 'UNLIKELY', 'NEUTRAL', 'LIKELY','VERY_LIKELY']

app = Flask(__name__, static_url_path='', static_folder='spotifind-frontend/build') #create instance of class flask
CORS(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/testing")
def testing_page():
    return "<p>Testing call</p>"


class ApiHandler(Resource):
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': ""
      }

  def post(self):
    # print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('authToken')

    args = parser.parse_args()

    client = SpotifyClient("hack")
    print(args)
    print(client.get_current_user(access_token=args["authToken"]))

    # request_type = args['authToken']
    # request_json = args['authToken']
    # # ret_status, ret_msg = ReturnData(request_type, request_json)
    # # currently just returning the req straight
    # ret_status = request_type
    # ret_msg = request_json

    # if ret_msg:
    #   message = "Your Message Requested: {}".format(ret_msg)
    # else:
    #   message = "No Msg"

    message = args
    
    final_ret = {"status": "Success", "message": message}

    return final_ret

class AuthApiHandler(ApiHandler):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('authToken', type=str)
        args = parser.parse_args()
        client = SpotifyClient("hack")
        print(args)
        print(client.get_current_user(access_token=args["authToken"]))
        message = args
        final_ret = {"status": "Success", "message": message}
        return final_ret

class LabelsApiHandler(ApiHandler):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('labels', type=str, action='append')
        parser.add_argument('authToken', type=str)
        args = parser.parse_args()
        client = SpotifyClient("hack")
        urilist = client.labels_rec(args["labels"], access_token=args["authToken"])
        url = make_playlist("UH2022", urilist, args["authToken"])
        # print(client.get_current_user(accesslist_token=args["labels"]))
        message = url
        print(url)
        final_ret = {"status": "Success", "message": message}
        return final_ret


class GoogleUploadApiHandler(ApiHandler):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('imageUrl', type=str)
        args = parser.parse_args()
        # client = SpotifyClient("hack")
        # print(args)
        # print(client.get_current_user(accesslist_token=args["labels"]))

        client = vision.ImageAnnotatorClient()
        # path = './test1.jpg'
        image_url = args["imageUrl"]#[5:]
        print(image_url)
        
        path = wget.download(image_url)
        # with io.open(path, 'rb') as image_file:
        #     content = image_file.read()

        # # fake user agent of Safari
        # fake_useragent = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'
        # r = urllib.request.Request(image_url, headers={'User-Agent': fake_useragent})
        # f = urllib.request.urlopen(r)

        # print or write
        print(f.read())

        content = ""
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

        message = playlist
        final_ret = {"status": "Success", "message": message}
        return final_ret


api = Api(app)
api.add_resource(AuthApiHandler, '/flask/auth')
api.add_resource(LabelsApiHandler, '/flask/labels')
api.add_resource(GoogleUploadApiHandler, '/flask/upload')

# @app.route("/color")
# def find_color():
#     client = vision.ImageAnnotatorClient()
#     path = './test1.jpg'
#     print(path)
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()


@app.route('/emotion')
def find_emotion():
    client = vision.ImageAnnotatorClient()
        
    with io.open(imagepath, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.annotate_image({
        'image': image,
        'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
    })

    
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
    url = make_playlist("UH2022 color", playlist)
    return f'{url}'

@app.route("/color")
def find_color():
    client = vision.ImageAnnotatorClient()
    
    # print(path)
    with io.open(imagepath, 'rb') as image_file:
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

    url = make_playlist("UH2022 color", trax)
    return f'{url}'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")

@app.route("/labels")
def image_to_labels():
    client = vision.ImageAnnotatorClient()
    
    with io.open(imagepath, 'rb') as image_file:
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
    
    
    urls = a.labels_rec(keywords)
    # print(urls)
    url = make_playlist("UH2022 color", urls)
    return f'{url}' 
