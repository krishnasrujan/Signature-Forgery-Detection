# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:00:29 2021

@author: Srujan
"""

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import numpy as np

# Keras
import tensorflow as tf
from tensorflow.keras.models import load_model

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer 

import numpy as np
import cv2
import os 
import pickle
# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
model = load_model('C:/Users/Srujan/Documents/Final_Project/base_network.h5',compile=False)
dir_path = 'C:/Users/Srujan/Documents/Final_Project'

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

def preprocess(filepath):
     
    try:
        img = cv2.imread(filepath,cv2.IMREAD_COLOR)     # reading image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # converting to gray scale
        thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # converting to black and white image
        thresh = cv2.erode(thresh, kernel, iterations=3)   # performing erosion operation 
        thresh = cv2.dilate(thresh, kernel, iterations=1)  # performing dilation 
        img = cv2.resize(thresh, (250, 75))             # resizing
        
        img = np.expand_dims(np.array(img), axis=-1)
        return img
    
    except Exception as ex:
        print(filepath) 
        
        
def predict(img,name):

    distances = []
    path = os.path.join(dir_path,name)
    vec1 = model(np.expand_dims(img,axis=0))

    for im in os.listdir(path):
        
        r_path = os.path.join(path,im)
        r_img = preprocess(r_path)
        vec2 = model(np.expand_dims(r_img,axis=0))
        dist = tf.math.squared_difference(vec1, vec2).numpy()
        dist = np.mean(dist[0]) # got two dimensional array with element 
                                # wise squared difference
        distances.append(dist)
        
    return distances

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        
        f = request.files['file']
        print('loaded')

        name = request.form['text']
        name = str(name)
        print('got name')

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'Uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        img = preprocess(file_path)
        distances = predict(img, name)
        
        if sum(distances)/len(distances) >700:
            return 'Signature is forged'
        else: return 'Signature is real'
    
    return None


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    