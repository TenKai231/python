import joblib
import pandas as pd
from flask import Flask, request, jsonify
import os
import logging
import datetime


logging.basicConfig(
    filemode='predication_api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = Flask(__name__)

# Pakai path absolut biar tidak bingung
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_LR = joblib.load(os.path.join(BASE_DIR, 'model_LR.pkl'))
kolom    = joblib.load(os.path.join(BASE_DIR, 'kolom_fitur.pkl'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df = df.reindex(columns=kolom, fill_value=0)
    prediction = model_LR.predict(df)
    logging.info(f"Data input: {data} | Prediksi harga: {prediction[0]}")
    return jsonify({'prediksi_harga': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)