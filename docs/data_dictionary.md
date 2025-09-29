# Data Dictionary

- timestamp: ISO-8601 timestamp of the reading
- machine_id: unique machine identifier
- sensor_temp: temperature reading (C)
- sensor_vib: vibration magnitude
- sensor_pressure: pressure reading
- throughput: units produced per minute
- failure: binary flag (0/1) recording if an immediate failure was observed at that timestamp
- temp_roll_mean_1h: rolling mean of temperature over last 1 hour (12 readings if 5-min freq)
- vib_roll_max_1h: rolling max vibration over last 1 hour
