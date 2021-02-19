#!/usr/bin/env python

import sys
import tensorflow as tf

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from model import OpenNsfwModel, InputType
from image_utils import create_tensorflow_image_loader

import numpy as np

input_type=InputType.BASE64_JPEG
model_weights="data/open_nsfw-weights.npy"

app = Flask(__name__)
api = Api(app)

class classifier(Resource):
  def get(self):
      model = OpenNsfwModel()
      fname = request.args.get('fn')
      
      with tf.Session() as sess:
        model.build(weights_path=model_weights, input_type=input_type)
        import base64
        fn_load_image = lambda filename: np.array([base64.urlsafe_b64encode(open(filename, "rb").read())])
        sess.run(tf.global_variables_initializer())
        image = fn_load_image(fname)
        predictions = \
            sess.run(model.predictions,
                     feed_dict={model.input: image})
        sfw, nsw = "{}:{}".format(*predictions[0]).split(":")
        scores = {
            "fileName" : fname,
            "sfw" : sfw,
            "nsw" : nsw
        }
        return jsonify(scores)

api.add_resource(classifier, '/classify')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#  curl -s localhost:5000/classify?fn='/home/mike/Pictures/Joey-Ryan.jpg' | jq .
