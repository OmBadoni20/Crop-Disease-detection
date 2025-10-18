from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your trained CNN model
model = load_model("model.h5")  # make sure the .h5 file is here

# Class labels (your 38 classes)
class_labels = [
    "Apple Apple scab",
    "Apple Black rot",
    "Apple Cedar apple rust",
    "Apple healthy",
    "Blueberry healthy",
    "Cherry (including sour) Powdery mildew",
    "Cherry (including sour) healthy",
    "Corn (maize) Cercospora leaf spot Gray leaf spot",
    "Corn (maize) Common rust",
    "Corn (maize) Northern Leaf Blight",
    "Corn (maize) healthy",
    "Grape Black rot",
    "Grape Esca (Black Measles)",
    "Grape Leaf blight (Isariopsis Leaf Spot)",
    "Grape healthy",
    "Orange Haunglongbing (Citrus greening)",
    "Peach Bacterial spot",
    "Peach healthy",
    "Pepper, bell Bacterial spot",
    "Pepper, bell healthy",
    "Potato Early blight",
    "Potato Late blight",
    "Potato healthy",
    "Raspberry healthy",
    "Soybean healthy",
    "Squash Powdery mildew",
    "Strawberry Leaf scorch",
    "Strawberry healthy",
    "Tomato Bacterial spot",
    "Tomato Early blight",
    "Tomato Late blight",
    "Tomato Leaf Mold",
    "Tomato Septoria leaf spot",
    "Tomato Spider mites Two-spotted spider mite",
    "Tomato Target Spot",
    "Tomato Tomato Yellow Leaf Curl Virus",
    "Tomato Tomato mosaic virus",
    "Tomato healthy"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction_text="No file uploaded")

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction_text="No file selected")

    # Save uploaded image
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # Preprocess image for your model (256x256)
    img = image.load_img(file_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    disease_name = class_labels[predicted_class]

    return render_template('index.html',
                           prediction_text=f"Predicted Disease: {disease_name}",
                           image_url=file_path)

if __name__ == '__main__':
    app.run(debug=True)

