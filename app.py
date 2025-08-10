from flask import Flask, render_template, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)


df = pd.read_csv("data.csv")  

X = df.drop(columns=["target"])
y = df["target"]


model = GaussianNB()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(request.form.get(f"feature{i}")) for i in range(1, X.shape[1] + 1)]
        prediction = model.predict([features])[0]
        return render_template("result.html", prediction=prediction)
    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
