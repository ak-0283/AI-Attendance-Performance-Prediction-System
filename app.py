from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import numpy as np
import pickle
from agent import AttendanceAgent

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# ----------------------------------------
# LOAD MODEL & ENCODER FIRST
# ----------------------------------------
model = pickle.load(open("model/attendance_model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

# ----------------------------------------
# NOW CREATE AI AGENT (CORRECT PLACE)
# ----------------------------------------
agent = AttendanceAgent(model, encoder)

# ----------------------------------------
# ROUTES
# ----------------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dataset")
def dataset():
    return render_template("dataset.html")

@app.route("/model")
def model_page():
    return render_template("model.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    suggestion = None
    action = None

    if request.method == "POST":
        print("POST request received")  # DEBUG LINE

        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])
        assignments = float(request.form["assignments"])
        classes_missed = float(request.form["classes_missed"])

        input_data = np.array([[attendance, marks, assignments, classes_missed]])

        risk = agent.perceive(input_data)
        decision = agent.decide(risk)
        response = agent.act(decision)

        prediction = risk
        suggestion = response["message"]
        action = response["action"]

        print("Prediction:", prediction)  # DEBUG LINE

    return render_template(
        "predict.html",
        prediction=prediction,
        suggestion=suggestion,
        action=action
    )


@app.route("/download-report")
def download_report():
    return send_file("static/model_report.txt", as_attachment=True)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("All fields are required.", "error")
        elif "@" not in email:
            flash("Please enter a valid email address.", "error")
        else:
            flash(
                f"Thank you, {name}! Your message has been received. "
                f"We'll respond to {email} soon.",
                "success"
            )
            return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
