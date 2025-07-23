from flask import Flask, request, jsonify
import os
import tempfile
import numpy as np
from keras.models import load_model
from model.i3d_wrapper import I3DWrapper
from utils.preprocess import preprocess_video
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

# Load model once
MODEL_PATH = 'model/model.h5'
model = load_model(MODEL_PATH, custom_objects={'I3DWrapper': I3DWrapper})

# Kelas target
CLASSES = ['lenggang', 'joged', 'hitam manis','kembang payung','langkah jepen' ]

@app.route('/')
def home():
    return "Video Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400

    video_file = request.files['video']

    if video_file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        video_file.save(tmp.name)
        video_path = tmp.name

    try:
        input_video = preprocess_video(video_path)
        predictions = model.predict(input_video)[0]
        predicted_class = CLASSES[np.argmax(predictions)]
        confidence = float(np.max(predictions)) * 100

        return jsonify({
            'prediction': predicted_class,
            'confidence': round(confidence, 2),
            'probabilities': {
                cls: round(float(prob) * 100, 2)
                for cls, prob in zip(CLASSES, predictions)
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(video_path)

if __name__ == '__main__':
    app.run(debug=True)
