

Iris Species Prediction App 🌸

This repository contains a simple web application that predicts the species of an Iris flower based on its sepal and petal measurements. The application uses a Gaussian Naive Bayes classifier trained on the famous Iris dataset.

Introduction

This project demonstrates a basic machine learning web application built with Flask. Users can input measurements of an Iris flower, and the application will predict whether it's a setosa, versicolor, or virginica species.

Features

Simple User Interface: A straightforward web form to input flower measurements.

Machine Learning Model:

Employs a Gaussian Naive Bayes model for classification.

Real-time Prediction: Provides instant predictions based on user input.

Files in this Repository

app.py: 

The main Flask application file. It loads the dataset, trains the Naive Bayes model, and handles web requests for the home page and prediction.


data.csv: 

The dataset containing Iris flower measurements (sepal length, sepal width, petal length, petal width) and their corresponding species (target). 


requirements.txt: 

Lists the Python dependencies required to run the application. 

templates/: 
<img width="1366" height="768" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/6a38ff33-e5b9-4abd-b14f-f93f80f37f68" />
<img width="1366" height="768" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/79966495-d60f-4daf-92d9-3da483e88f37" />

(Implied, but not provided in the prompt - you'll need index.html and result.html in this directory)

index.html: The HTML template for the home page where users input features.

result.html: The HTML template to display the prediction result.
