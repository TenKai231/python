import joblib
import pandas as pd 
import numpy as np
from flask import Flask, request,jsonify
import os

app = Flask(__name__)

# model_lars = joblib.load('module 13/model_lars.pkl')
# model_LR = joblib.load('module 13/model_LR.pkl')
# model_GBR = joblib.load('module 13/model_GBR.pkl')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_LR = joblib.load(os.path.join(BASE_DIR, 'model_LR.pkl'))
kolom    = joblib.load(os.path.join(BASE_DIR, 'kolom_fitur.pkl'))

# print("Model LARS:", model_lars)
# print("Model LR:", model_LR)
# print("Model GBR:", model_GBR)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json3
    # Perform prediction using the loaded models
    df = pd.DataFrame([data])
    # Ensure the order of columns matches the training data
    df = df.reindex(columns=kolom, fill_value=0)  # Ensure the order of columns matches the training data
    # Ensure the order of columns matches the training data    
    prediction = model_LR.predict(df)
    return jsonify({"prediction_price": float(prediction[0])})
if __name__ == '__main__':
    app.run(debug=True)



