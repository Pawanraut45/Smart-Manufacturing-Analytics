# src/evaluate.py
import argparse
import pandas as pd
import joblib
from sklearn.metrics import classification_report,roc_auc_score

def evaluate(inpath, model_path):
    df = pd.read_csv(inpath, parse_dates=['timestamp'])
    model = joblib.load(model_path)
    features = ['sensor_temp','sensor_vib','sensor_pressure','throughput','temp_roll_mean_1h','vib_roll_max_1h','hour']
    df['failure_next_1h'] = df.groupby('machine_id')['failure'].shift(-12).fillna(0).astype(int)
    df = df.dropna(subset=features + ['failure_next_1h'])
    X = df[features]
    y = df['failure_next_1h']
    preds = model.predict(X)
    proba = model.predict_proba(X)[:,1]
    print(classification_report(y, preds))
    try:
        print("ROC AUC:", roc_auc_score(y, proba))
    except:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inpath", required=True)
    parser.add_argument("--model", dest="model_path", required=True)
    args = parser.parse_args()
    evaluate(args.inpath, args.model_path)
