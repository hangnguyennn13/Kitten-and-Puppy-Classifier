# import base64
# import re
import os 
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from flask import send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224

model_new = tf.keras.models.load_model("static/models/catdog_classifer.h5")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model')
def model_page():
    return render_template('model.html')

def api(full_path):

    img = tf.io.read_file(full_path)
    image = tf.image.decode_jpeg(img, channels=3)
    image = tf.image.resize(image, [IMAGE_WIDTH, IMAGE_HEIGHT])
    image /= 255.0
    image= np.expand_dims(image, axis=0)
    prediction = model_new.predict(image)
    
    return prediction

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        full_name = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(full_name)

        indices = {0: 'Cat', 1: 'Dog', 2: 'Invasive carcinomar', 3: 'Normal'}
        result = api(full_name)

        predicted_class = np.asscalar(np.argmax(result, axis=1))
        accuracy = round(result[0][predicted_class] * 100, 2)
        label = indices[predicted_class]
        return render_template('predict.html', image_file_name = file.filename, label = label, accuracy = accuracy)



@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
   app.run(debug = True)