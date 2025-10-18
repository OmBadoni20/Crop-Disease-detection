# 🌾 Crop Disease Detection using CNN

This project is a web application that uses a Convolutional Neural Network (CNN) to detect diseases in various crops from an uploaded image. It can identify 38 different types of plant and disease combinations.

## 📋 Features

* Simple web interface for uploading crop images.
* Predicts one of 38 classes of plant diseases.
* Built with Flask for the backend and TensorFlow/Keras for the model.
* Displays the uploaded image and the prediction result.

## ⚙️ Setup and Installation

**1. Clone the Repository**

```bash
git clone https://github.com/OmBadoni20/Crop-Disease-detection.git
cd Crop-Disease-detection
```

**2. Install Git LFS**
The model file (`model.h5`) is very large and is managed using Git Large File Storage (LFS). You must have Git LFS installed.

```bash
# Install Git LFS (if you haven't already)
git lfs install
```

**3. Download the Model File**
Pull the LFS files to download the actual `model.h5` file.

```bash
git lfs pull
```

**4. Install Dependencies**
It's recommended to create a virtual environment. The required packages are listed in `requirements.txt`.

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\activate

# Install the required packages
pip install Flask tensorflow numpy Pillow
```

*(Note: You can create a `requirements.txt` file with the packages above for easier installation.)*

## ▶️ How to Run

Once the setup is complete, run the Flask application from the project's root directory:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000`. Upload an image of a crop leaf to get a prediction.

## 📊 Results and Demonstration

The model was trained on a dataset of plant images and can predict 38 different classes.

Train Accuracy  : 98.14 %
Test Accuracy   : 96.77 %
Precision Score : 96.77 %
Recall Score    : 96.77 %

**Example Prediction:**

Here is an example of an uploaded image and the model's output.

* **Input Image:**
  ![Sample Leaf](C:\Users\ombad\OneDrive\Desktop\crop_disease_app\static\00075aa8-d81a-4184-8541-b692b78d398a___FREC_Scab 3335_270deg.jpg)

* **Predicted Output:**

  ```
  Predicted Disease: Corn (maize) healthy
  ```

  *(Note: The actual prediction may vary based on the image provided.)*

---

### 🖼️ Additional Example from GitHub Repository

Below is another example image demonstrating the app’s working:

![My Demo Image](https://github.com/yourusername/yourrepo/blob/main/path_to_your_image.jpg?raw=true)
![My Demo Image](https://github.com/yourusername/yourrepo/blob/main/path_to_your_image.jpg?raw=true)
![My Demo Image](https://github.com/yourusername/yourrepo/blob/main/path_to_your_image.jpg?raw=true)

*(Replace the link above with your actual GitHub image URL.)*

---

## 📂 Project Structure

```
crop_disease_app/
│
├── app.py                  # Main Flask application
├── model.h5                # The trained Keras CNN model (handled by Git LFS)
├── .gitattributes          # Specifies which files Git LFS should track
├── README.md               # This file
│
├── static/
│   ├── style.css           # CSS for the web interface
│   └── grapes-732x549-thumbnail.avif # Example image
│
└── templates/
    └── index.html          # HTML template for the web interface
```
