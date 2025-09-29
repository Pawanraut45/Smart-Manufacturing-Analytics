# src/etl.py
import argparse
import pandas as pd
from datetime import datetime

def run_etl(inpath, outpath):
    df = pd.read_csv(inpath, parse_dates=['timestamp'])
    # basic cleaning
    df = df.dropna()
    # add derived columns
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.date
    # rolling aggregates per machine
    df = df.sort_values(['machine_id','timestamp'])
    df['temp_roll_mean_1h'] = df.groupby('machine_id')['sensor_temp'].transform(lambda x: x.rolling(window=12, min_periods=1).mean())
    df['vib_roll_max_1h'] = df.groupby('machine_id')['sensor_vib'].transform(lambda x: x.rolling(window=12, min_periods=1).max())
    # write processed
    df.to_csv(outpath, index=False)
    print(f"Processed {len(df)} rows -> {outpath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inpath", required=True)
    parser.add_argument("--out", dest="outpath", default="data/processed.csv")
    args = parser.parse_args()
    run_etl(args.inpath, args.outpath)
