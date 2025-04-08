from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import os
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load model (stable path)
MODEL_PATH = os.path.join("saved_model", "plant_disease_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

# Class names
class_names = ['Apple___Black_rot', 'Apple___healthy', 'Apple___rust', 'Apple___scab', 
               'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
               'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
               'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 
               'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 
               'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
               'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 
               'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 
               'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 
               'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
               'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 
               'Tomato___healthy']

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No image part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Read and preprocess
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((128, 128))
        img_array = np.array(image).astype('float32') / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))

        return jsonify({
            "prediction": predicted_class,
            "confidence": confidence
        })

    except Exception as e:
        print("🔥 Exception occurred:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return 'Backend is running!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
