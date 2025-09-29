# src/train_model.py
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import xgboost as xgb
import joblib
import os

def train(inpath, model_out):
    df = pd.read_csv(inpath, parse_dates=['timestamp'])
    # use recent window features
    features = ['sensor_temp','sensor_vib','sensor_pressure','throughput','temp_roll_mean_1h','vib_roll_max_1h','hour']
    df['failure_next_1h'] = df.groupby('machine_id')['failure'].shift(-12).fillna(0).astype(int)
    df = df.dropna(subset=features + ['failure_next_1h'])
    X = df[features]
    y = df['failure_next_1h']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    proba = model.predict_proba(X_test)[:,1]
    print(classification_report(y_test, preds))
    try:
        print("ROC AUC:", roc_auc_score(y_test, proba))
    except:
        pass
    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    joblib.dump(model, model_out)
    print("Saved model to", model_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inpath", required=True)
    parser.add_argument("--model_out", default="models/xgb_model.joblib")
    args = parser.parse_args()
    train(args.inpath, args.model_out)
