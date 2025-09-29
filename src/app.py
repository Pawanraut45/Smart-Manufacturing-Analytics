# src/app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = None
FEATURE_ORDER = ['sensor_temp','sensor_vib','sensor_pressure','throughput','temp_roll_mean_1h','vib_roll_max_1h','hour']

@app.before_first_request
def load_model():
    global model
    model = joblib.load('models/xgb_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.json
    if isinstance(payload, dict):
        df = pd.DataFrame([payload])
    else:
        df = pd.DataFrame(payload)
    # ensure columns
    try:
        X = df[FEATURE_ORDER]
    except Exception as e:
        return jsonify({"error":"missing features","details":str(e)}), 400
    preds = model.predict_proba(X)[:,1]
    return jsonify({"predicted_failure_probability": preds.tolist()})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
