# notebooks/analysis.py
# Quick analysis & visualization of synthetic dataset
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sensor_readings.csv', parse_dates=['timestamp'])
print(df['machine_id'].nunique(), "machines,", len(df), "rows")
sample = df[df['machine_id']=='MC_001'].set_index('timestamp').resample('1H').mean()
sample[['sensor_temp','sensor_vib']].plot(subplots=True)
plt.savefig('notebooks/quick_plot.png')
print('Saved quick_plot.png')
