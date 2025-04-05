# 🌿 Plant Leaf Disease Detection - ML Based Web App

A machine learning–based web application for detecting plant leaf diseases using Convolutional Neural Networks (CNN). Users can upload an image of a leaf to receive instant disease predictions and view relevant precautions.

---

## 🚀 Features

- 📷 Upload plant leaf images via a simple UI
- 🧠 CNN-based ML model predicts disease accurately
- 🔊 Voice output of predicted disease
- 💡 Displays relevant precautions for each disease
- 🌐 Full-stack app: React (frontend) + Flask (backend)

---

## 📂 Project Structure

```bash
plant-disease-app/
│
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── model_trainer.py
│   ├── precautions.json
│   ├── saved_model/
│   │   └── plant_disease_model.h5
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.js
│   │   │   └── Result.js
│   └── ...
│
├── dataset/                   # PlantVillage images
├── images/                    # Screenshots for README
├── temp/                      # Uploaded images
├── templates/                 # Flask fallback HTML
└── README.md
```

---

## 🧠 Model Information

- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow / Keras
- **Dataset**: [PlantVillage (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Accuracy**: ~95% on test data
- **Model Output**: Disease class name (string)

---

## ⚙️ Running the Project Locally

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm start
```

Now open your browser at [http://localhost:5173/](http://localhost:5173/)

---

## 📸 Screenshots

### 🏠 Homepage

<!-- Paste homepage image below -->
![Homepage](./images/homepage.png)

---

### 📤 Uploading a Leaf Image

<!-- Paste upload page image below -->
![Upload Page](./images/uploading.png)

---

### 🧾 Prediction Result with Voice Output

<!-- Paste result screenshot below -->
![Prediction Result](./images/prediction_result.png)
---

### 💡 Precautions Page

<!-- Paste precautions screenshot below -->
![Precautions](./images/precautions.png)

---

## 📌 Precaution Data

Precautions are stored in `backend/precautions.json`. After predicting the disease, users can view the suggested measures to prevent or treat the disease using the **Precautions** button on the interface.

---

## ✅ Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | React.js           |
| Backend      | Flask (Python)     |
| ML Model     | CNN (TensorFlow)   |
| Dataset      | PlantVillage       |

---

## 💡 Possible Future Enhancements

- 🌐 Deploy to cloud (Render / Hugging Face Spaces)
- 📱 Improve mobile responsiveness
- 🗣️ Add multi-language support (currently only voice output is implemented)

---