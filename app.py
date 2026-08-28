from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("maternal_health_model.pkl")


# =========================================================
# COMMON PREDICTION FUNCTION
# =========================================================

def make_prediction(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):

    # -----------------------------
    # Feature Engineering
    # -----------------------------

    pulse_pressure = systolic_bp - diastolic_bp

    map_value = (systolic_bp + (2 * diastolic_bp)) / 3

    fever = 1 if body_temp >= 100.4 else 0

    high_bs = 1 if bs > 7.8 else 0

    # Age Groups
    agegroup_30_40 = age >= 30 and age < 40
    agegroup_40_50 = age >= 40 and age < 50
    agegroup_50_plus = age >= 50
    agegroup_teen = age < 20

    # BP Category
    bp_category_high = (
        systolic_bp >= 140 or diastolic_bp >= 90
    )

    bp_category_normal = (
        systolic_bp < 130 and diastolic_bp < 85
    )

    # Heart Rate Category
    hr_category_normal = (
        60 <= heart_rate <= 100
    )

    # -----------------------------
    # Create DataFrame
    # -----------------------------

    input_data = pd.DataFrame([[
        age,
        systolic_bp,
        diastolic_bp,
        bs,
        body_temp,
        heart_rate,
        pulse_pressure,
        map_value,
        fever,
        high_bs,
        agegroup_30_40,
        agegroup_40_50,
        agegroup_50_plus,
        agegroup_teen,
        bp_category_high,
        bp_category_normal,
        hr_category_normal
    ]], columns=[
        "Age",
        "SystolicBP",
        "DiastolicBP",
        "BS",
        "BodyTemp",
        "HeartRate",
        "PulsePressure",
        "MAP",
        "Fever",
        "HighBS",
        "AgeGroup_30-40",
        "AgeGroup_40-50",
        "AgeGroup_50+",
        "AgeGroup_Teen",
        "BP_Category_High",
        "BP_Category_Normal",
        "HR_Category_Normal"
    ])

    # Convert boolean columns to integers
    bool_columns = [
        "AgeGroup_30-40",
        "AgeGroup_40-50",
        "AgeGroup_50+",
        "AgeGroup_Teen",
        "BP_Category_High",
        "BP_Category_Normal",
        "HR_Category_Normal"
    ]

    input_data[bool_columns] = (
        input_data[bool_columns].astype(int)
    )

    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(input_data)
    prediction = model.predict(input_data)

    print("Prediction:", prediction)
    print("Probabilities:", model.predict_proba(input_data))
    print("Classes:", model.classes_)

    prediction_value = int(prediction[0])

    # -----------------------------
    # Risk Mapping
    # -----------------------------

    risk_mapping = {
        0: "High Risk",
        1: "Low Risk",
        2: "Mid Risk"
    }

    icon_mapping = {
        0: "🔴",
        1: "🟢",
        2: "🟡"
    }

    message_mapping = {
        0: "The AI model indicates a higher predicted risk level. Please consider seeking appropriate medical attention.",

        1: "The AI model indicates a lower predicted risk level based on the provided parameters.",

        2: "The AI model indicates a moderate predicted risk level. Consider discussing the results with a healthcare professional."
    }

    return {
        "risk": risk_mapping[prediction_value],
        "icon": icon_mapping[prediction_value],
        "message": message_mapping[prediction_value]
    }


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/")
def home():
    return render_template("dashboard.html")


# =========================================================
# ASSESSMENT PAGE
# =========================================================

@app.route("/assessment")
def assessment():
    return render_template("index.html")


# =========================================================
# ANALYTICS
# =========================================================

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


# =========================================================
# VOICE ASSISTANT
# =========================================================

@app.route("/assistant")
def assistant():
    return render_template("assistant.html")


# =========================================================
# NORMAL FORM PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])

    systolic_bp = int(
        request.form["systolic_bp"]
    )

    diastolic_bp = int(
        request.form["diastolic_bp"]
    )

    bs = float(
        request.form["bs"]
    )

    body_temp = float(
        request.form["body_temp"]
    )

    heart_rate = int(
        request.form["heart_rate"]
    )

    # Use common prediction function
    result = make_prediction(
        age,
        systolic_bp,
        diastolic_bp,
        bs,
        body_temp,
        heart_rate
    )

    return render_template(
        "result.html",

        risk=result["risk"],

        icon=result["icon"],

        message=result["message"],

        age=age,

        systolic_bp=systolic_bp,

        diastolic_bp=diastolic_bp,

        bs=bs,

        body_temp=body_temp,

        heart_rate=heart_rate
    )


# =========================================================
# VOICE PREDICTION
# =========================================================

@app.route("/voice-predict", methods=["POST"])
def voice_predict():

    age = int(
        request.form["age"]
    )

    systolic_bp = int(
        request.form["systolic_bp"]
    )

    diastolic_bp = int(
        request.form["diastolic_bp"]
    )

    bs = float(
        request.form["bs"]
    )

    body_temp = float(
        request.form["body_temp"]
    )

    heart_rate = int(
        request.form["heart_rate"]
    )

    # Use THE SAME ML FUNCTION
    result = make_prediction(
        age,
        systolic_bp,
        diastolic_bp,
        bs,
        body_temp,
        heart_rate
    )

    # Send result directly to result.html
    return render_template(
        "result.html",

        risk=result["risk"],

        icon=result["icon"],

        message=result["message"],

        age=age,

        systolic_bp=systolic_bp,

        diastolic_bp=diastolic_bp,

        bs=bs,

        body_temp=body_temp,

        heart_rate=heart_rate
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)