from flask import Flask, request, send_file, jsonify
import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow.keras.preprocessing.image import load_img
import tensorflow as tf
import numpy as np
import os
import io
import sys
from proto import np_to_protobuf
from PIL import Image 


HOST = os.getenv('TF_SERVING_HOST', 'localhost:8500')
app = Flask(__name__)
print(HOST)
channel = grpc.insecure_channel(HOST)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

from kih.helper import create_preprocessor
preprocessor = create_preprocessor("efficientnet_v2", target_size=(150, 150))

classes = [
    'moderate',
    'normal',
    'severe'
]


def process_image1(image):
    with Image.open(image) as img:
        img = img.resize((128, 128))
        def preprocess_input(x):
            x /= 255
            x -= 1.
            return x
        x = np.array(img , dtype='float32')
        X = np.array([x])

        X = preprocess_input(X)
    return X


def process_image2(image):
    with Image.open(image) as img:
        img = img.resize((128, 128))
        def preprocess_input(x):
            x /= 127.5
            x -= 1.0
            return x
        x = np.array(img, dtype='float32')
        X = np.array([x])

        X = preprocess_input(X)
    return X




@app.route("/predict", methods=["POST"])
def predict_endpoint():
    image = request.files['file']
    X = preprocessor.from_path(image)
    #X = process_image2(image)
    print(X.dtype)
    print(X.shape)
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'xr_knee_model'
    pb_request.model_spec.signature_name = 'serving_default'
    pb_request.inputs['input_1'].CopyFrom(np_to_protobuf(X))
    pb_response = stub.Predict(pb_request, timeout=20.0)
    preds = pb_response.outputs['dense_1'].float_val
    preds = dict(zip(classes,preds))
    print(preds)
    return jsonify(preds)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9797) 



