
# 🌿 Plant Leaf Disease Detection App

A deep learning powered web app that detects diseases in plant leaves using Convolutional Neural Networks (CNN). Upload a leaf image, identify the disease, and get actionable precautions instantly — with multilingual support and voice output!

---

## 🚀 Features

- 🔍 Real-time disease prediction using CNN
- 📢 Voice output of disease name
- 🌐 Multilingual support (English, Telugu)
- 💡 Precaution suggestions
- 🌑 Beautiful dark-themed UI
- 🖼️ Image upload and preview functionality

---

## 🧠 Model

- **Model**: CNN (Trained using TensorFlow)
- **Dataset**: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Classes**:
  - Apple Black Rot, Grape Black Rot, Potato Late Blight, etc.
  - Healthy variants included

---

## 📸 Screenshots

### 🔹 Home Page
![Home Page](images/homepage.png)

### 🔹 Disease Prediction
![Prediction](images/prediction.png)

---

## 🛠️ Tech Stack

| Component   | Technology     |
|------------|----------------|
| Frontend   | React.js       |
| Backend    | Flask (Python) |
| Model      | TensorFlow     |
| Styling    | CSS (Dark Theme) |
| Voice      | Web Speech API |
| Hosting    | Local / GitHub |

---

## ⚙️ Installation

```bash
git clone https://github.com/Chandini7203/plant-disease-app.git
cd plant-disease-app
```

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🧪 How it Works

1. Upload an image of the plant leaf 🌿
2. App sends image to Flask backend 📤
3. Model processes image and predicts disease 🧠
4. Output shown on screen with precautions & voice output 🗣️

---

## 💬 Voice + Language Support

- Voice announces the **disease name**
- Language selector toggles between **English and Telugu**
- Descriptions shown based on selected language

---

## 🧼 Precautions

Each disease returns:
- Short description
- Suggested precautions
- Preventive actions

---

## 🤝 Contributors

- 👩‍💻 Chandini7203 — Fullstack Developer & Innovator
- 🤖 AI Model Trainer — BLIP, TensorFlow

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- PlantVillage Dataset
- TensorFlow & React communities
- All open-source contributors!
