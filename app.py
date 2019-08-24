# import base64
# import re

import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model')
def model_page():
    return render_template('model.html')

@app.route("/model/upload/", methods=["POST"])
def upload_file():
    # img_raw = parse_image(request.get_data())

    # image = tf.image.decode_jpeg(img_raw, channels=3)
    # image = tf.image.resize(image, [28, 28])
    # image = (255 - image) / 255.0  # normalize to [0,1] range
    # image = tf.reshape(image, (1, 28, 28, 3))

    prediction = 0
    return str(prediction)

if __name__ == "__main__":
    app.run(debug = True)