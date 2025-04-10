# 🌿 Plant Leaf Disease Detection using Machine Learning

A full-stack web app that identifies diseases in plant leaves using a trained Convolutional Neural Network (CNN). Built with React and Flask, this project empowers farmers and agriculturalists by offering a fast, user-friendly platform to diagnose plant health with image uploads. The app also provides disease-specific precautions and voice-based prediction output to enhance accessibility.

---

## 🧠 Project Overview

- **Goal**: Detect diseases in plant leaves using image-based ML model
- **Model**: CNN trained on the PlantVillage dataset
- **Frontend**: React (with Vite)
- **Backend**: Flask + TensorFlow
- **Voice Feature**: Speaks out the prediction (only for disease name)
- **Extra Modules Used**: `gTTS` for voice, `flask-cors` for CORS handling, `numpy`, `PIL`, etc.

---

## 📂 Project Structure

```
plant-disease-app/
│
├── backend/
│   ├── app.py
│   ├── utils/
│   └── saved_model/
│       └── plant_disease_model.h5
│
├── frontend/
│   ├── src/
│   └── index.html
│
├── dataset/
│   └── (Training images)
│
├── images/
│   ├── homepage.png
│   ├── upload.png
│   ├── prediction.png
│   └── precautions.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/Chandini7203/plant-disease-app.git
cd plant-disease-app
```

### 2. 📦 Install Backend Requirements
```bash
pip install -r requirements.txt
```

### 3. 🔁 Start the Backend Server
```bash
cd backend
python app.py
```

### 4. 🌐 Start the Frontend App
```bash
cd ../frontend
npm install
npm run dev
```

---

## 🖼️ Screenshots

### 🔹 Homepage
![Homepage](images/homepage.png)

### 🔹 Upload Image
![Upload](images/upload.png)

### 🔹 Prediction Output
![Prediction](images/prediction.png)

### 🔹 Precautions View
![Precautions](images/precautions.png)

---

## ✨ Key Features

- 🔍 Upload and detect plant leaf diseases in real-time  
- 📊 High accuracy CNN model  
- 📢 Voice-based prediction output (disease name only)  
- 💡 Precautions for each identified disease  
- 📱 Simple and responsive UI

---

## 🛠️ Tools & Technologies Used

| Layer        | Stack                            |
|--------------|----------------------------------|
| Frontend     | React (Vite), HTML, CSS, JS      |
| Backend      | Python, Flask, Flask-CORS        |
| ML Model     | TensorFlow, Keras (CNN), NumPy   |
| Voice Output | gTTS                             |
| Dataset      | PlantVillage                     |

---

## 🚀 Deployment (Push Commands)

```bash
git add .
git commit -m "Updated files"
git push origin main
```

---

