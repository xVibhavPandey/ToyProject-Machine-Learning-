from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        cgpa = float(request.form["cgpa"])
        iq = float(request.form["iq"])

        features = np.array([[cgpa, iq]])
        prediction = model.predict(features)[0]

        # Convert output to Yes/No
        result = "Yes" if prediction == 1 else "No"

        return render_template("index.html", prediction_text=f"Placement: {result}")

    except:
        return render_template("index.html", prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)