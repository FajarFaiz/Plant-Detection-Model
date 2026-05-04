from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load model safely
try:
    model = load_model("models/model.h5")  # <-- make sure this path is correct
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
    model = None

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_and_preprocess(img_path, target_size=(225, 225)):
    try:
        img = image.load_img(img_path, target_size=target_size, color_mode='rgb')
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
2
def predict_image(img_path):
    if model is None:
        return "Model not loaded", 0.0
    img_array = load_and_preprocess(img_path)
    if img_array is None:
        return "Invalid Image", 0.0
    preds = model.predict(img_array)[0]
    class_idx = np.argmax(preds)
    labels = {0: 'Healthy Leaf', 1: 'Powdery Mildew', 2: 'Early Blight', 3: 'Rust'}
    return labels.get(class_idx, "Unknown"), float(preds[class_idx])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    label, confidence = predict_image(filepath)
    return jsonify({'label': label, 'confidence': confidence, 'filename': filename})

if __name__ == "__main__":
    app.run(debug=True)

##venv/Scripts/Activate.ps1