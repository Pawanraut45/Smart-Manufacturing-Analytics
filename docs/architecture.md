# Architecture Overview

**Goal:** Predict equipment failure within next 1 hour and propose prescriptive actions to reduce downtime.

Components:
- Data ingestion: sensors -> Azure IoT Hub / Edge -> Blob storage
- ETL: Azure Data Factory / Databricks notebooks -> process & aggregate
- Model training: Databricks / Azure ML using XGBoost / LSTM for time-series
- Deployment: Containerized Flask API behind AKS or App Service
- Monitoring: Application Insights / Prometheus for inference and drift
- CI/CD: GitHub Actions -> build image -> push to container registry -> deploy

**Data model**: time-series per machine, aggregated windows (1h), labels: failure within next 1h.

**Prescriptive layer**:
- Combine model scores with reliability rules to produce maintenance actions and estimated savings.
