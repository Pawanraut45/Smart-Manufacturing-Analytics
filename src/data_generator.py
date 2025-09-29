# src/data_generator.py
import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sensor_stream(n_machines=5, days=7, freq_minutes=5):
    rows = []
    start = datetime.utcnow() - timedelta(days=days)
    for m in range(1, n_machines+1):
        t = start
        wear = random.uniform(0, 0.1)
        for i in range(int((days*24*60)/freq_minutes)):
            # simulate multiple sensors
            temp = 60 + 10*np.sin(i/50.0) + np.random.normal(0,0.5) + wear*100
            vib = 0.05 + 0.02*np.sin(i/30.0) + np.random.normal(0,0.005) + wear*2
            pressure = 5 + 0.5*np.cos(i/80.0) + np.random.normal(0,0.1)
            throughput = 100 + 5*np.sin(i/20.0) + np.random.normal(0,1)
            # failure probability increases with wear
            fail_prob = min(0.0005 + wear*0.01 + np.random.normal(0,0.0001), 0.05)
            failure = 1 if random.random() < fail_prob else 0
            # occasional maintenance resets wear
            if random.random() < 0.0008:
                wear = max(0, wear - random.uniform(0.02,0.05))
            wear += 0.0002
            rows.append({
                "timestamp": t.isoformat(),
                "machine_id": f"MC_{m:03d}",
                "sensor_temp": round(temp,3),
                "sensor_vib": round(vib,4),
                "sensor_pressure": round(pressure,3),
                "throughput": round(throughput,2),
                "failure": failure
            })
            t += timedelta(minutes=freq_minutes)
    return pd.DataFrame(rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/sensor_readings.csv")
    parser.add_argument("--n_machines", type=int, default=5)
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()
    df = generate_sensor_stream(n_machines=args.n_machines, days=args.days)
    df.to_csv(args.out, index=False)
    print(f"Wrote {len(df)} rows to {args.out}")

if __name__ == "__main__":
    main()
