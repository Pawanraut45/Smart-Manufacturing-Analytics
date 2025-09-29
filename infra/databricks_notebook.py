# Databricks notebook - example ETL & Train (python)
# 1) Mount storage and read data
# df = spark.read.option("header",True).csv("/mnt/raw/sensor_readings.csv")
# 2) Basic transformations
# display(df.limit(10))
# 3) Write processed parquet to /mnt/processed/
# 4) Train with mlflow / xgboost (sketch)
