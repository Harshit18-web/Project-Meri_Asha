# 🌸 Meri Asha

> **An AI-powered maternal healthcare assistant designed to make risk assessment and healthcare support more accessible, intelligent, and user-friendly.**

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-Enabled-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-Flask-black?style=for-the-badge&logo=flask" />
</p>

---

## 📖 Overview

**Meri Asha** is an AI-powered healthcare platform focused on supporting **maternal health assessment and assistance**.

The platform combines **Machine Learning, Natural Language Processing, and Voice Technology** to provide an accessible healthcare experience.

Meri Asha helps users assess maternal health risk through important health parameters while also providing an AI-powered assistant for natural and voice-based interaction.

---

## 🎯 Problem

Maternal health assessment can become challenging when healthcare workers have limited access to timely medical support and intelligent digital tools.

**Meri Asha aims to bridge this gap by providing AI-assisted risk prediction and accessible healthcare assistance through a simple digital platform.**

---

## 💡 Solution

Meri Asha brings multiple healthcare capabilities together in one platform:

* 🩺 **Maternal Health Risk Prediction**
* 🤖 **AI-powered Healthcare Assistant**
* 🎙️ **Voice-based Interaction**
* 🧠 **Natural Language Processing**
* 📊 **Health Analytics Dashboard**
* 🌐 **Simple and Accessible Web Interface**

---

# ✨ Key Features

### 🩺 Maternal Health Risk Assessment

The system analyzes important maternal health parameters and predicts the corresponding risk level.

**Risk Categories:**

```text
🟢 Low Risk
🟡 Mid Risk
🔴 High Risk
```

---

### 🤖 AI Healthcare Assistant

Users can interact with the healthcare assistant using natural language to get relevant health-related assistance.

The goal is to make healthcare interaction more intuitive than a traditional form-based system.

---

### 🎙️ Voice Assistant

Meri Asha supports voice interaction to make the platform easier and more accessible.

```text
User Speech
     ↓
Speech Recognition
     ↓
NLP Processing
     ↓
AI Response
     ↓
Voice / Text Response
```

---

### 📊 Analytics Dashboard

The analytics section provides a visual overview of assessment-related information and helps users understand the generated results.

---

# 🧠 Machine Learning

The maternal health prediction module uses a **Random Forest Classifier**.

### Prediction Pipeline

```text
Patient Health Parameters
          ↓
     Data Validation
          ↓
   Feature Engineering
          ↓
     Preprocessing
          ↓
    Random Forest
          ↓
    Risk Prediction
          ↓
  Low / Mid / High Risk
```

### Input Parameters

The model works with parameters such as:

* Age
* Systolic Blood Pressure
* Diastolic Blood Pressure
* Blood Sugar
* Body Temperature
* Heart Rate

Additional engineered features include:

* Pulse Pressure
* Mean Arterial Pressure (MAP)
* Fever indicator
* High Blood Sugar indicator
* Age Group
* Blood Pressure Category
* Heart Rate Category

---

# 🏗️ Architecture

```text
                    ┌───────────────────┐
                    │       USER        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     Frontend      │
                    │  HTML/CSS/JS      │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
             Health Assessment    Voice Assistant
                    │                   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Flask Backend    │
                    │    Python API     │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
              ML Prediction        NLP / Voice
                    │                   │
                    ▼                   ▼
              Risk Result         AI Response
```

---

# 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

### Backend

* Python
* Flask

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Joblib

### AI / NLP / Voice

* Natural Language Processing
* Speech Recognition
* Whisper
* Text-to-Speech

### Database / Services

* Firebase
* Firestore
* Firebase Authentication

### Deployment & Development

* Render
* Git
* GitHub
* PyCharm

---

# 📂 Project Structure

```text
Meri-Asha/
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   ├── analytics.html
│   └── assistant.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── VoiceModelTraining/
│
├── whisper/
│
├── maternal_health_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Getting Started

## Prerequisites

Make sure you have the following installed:

* Python 3.x
* pip
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/Harshit18-web/Meri-Asha.git
cd Meri-Asha
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

The Flask development server will start locally.

Open the URL displayed in your terminal to access **Meri Asha**.

---

# 🔄 Application Flow

```text
                 USER
                   │
                   ▼
          ┌────────────────┐
          │  Meri Asha UI  │
          └───────┬────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Health Input        Voice / Text
        │                   │
        ▼                   ▼
   ML Pipeline          NLP System
        │                   │
        ▼                   ▼
 Risk Prediction       AI Response
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
             USER RESULT
```

---

# 🚀 Deployment

Meri Asha can be deployed as a Flask web application using a cloud hosting platform such as **Render**.

For production deployment, the Flask application can be served using a WSGI server such as:

```bash
gunicorn app:app
```

Environment variables and API credentials should be configured securely through the deployment platform.

---

# 🔮 Future Scope

* 🌍 Multilingual healthcare assistance
* 🗣️ Regional-language voice support
* 📱 Mobile application
* 🏥 Healthcare-provider integration
* 👩‍⚕️ Medical referral and escalation
* 📡 Offline support for low-connectivity regions
* 📈 Advanced predictive analytics
* 🔐 Enhanced healthcare data privacy
* 🧠 Improved personalized AI assistance

---

# ⚠️ Disclaimer

Meri Asha is an **AI-assisted healthcare project** developed for educational, research, and decision-support purposes.

The predictions generated by the system should **not be considered a medical diagnosis or a replacement for professional medical advice**.

Users should consult qualified healthcare professionals for medical decisions.

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/your-feature

# Commit your changes
git add .
git commit -m "Add: your feature"

# Push your branch
git push origin feature/your-feature
```

Then open a Pull Request.

---

# ⭐ Support

If you like **Meri Asha**, consider giving the repository a ⭐ on GitHub.

<p align="center">

### 🌸 Meri Asha

**AI for Accessible Maternal Healthcare**

Built with ❤️ using **Python • Flask • Machine Learning • NLP • Voice Technology**

</p>
