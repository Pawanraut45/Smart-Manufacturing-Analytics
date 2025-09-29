# Smart Manufacturing Analytics
Project: Predictive & Prescriptive Analytics for Manufacturing (Dry Laundry Platform)

**Purpose:** Demonstration project built to match the P&G job description for advanced analytics in smart manufacturing: process & equipment analytics, predictive maintenance/prognostics, data pipelines, model deployment, and CI/CD.

**What's included**
- Synthetic sensor dataset simulating manufacturing equipment.
- ETL pipeline scripts (pandas / PySpark-ready structure).
- Feature engineering and modeling (XGBoost regression/classification + baseline LSTM sketch).
- Model evaluation and explainability artifacts.
- Deployment example: Flask API + Dockerfile.
- Infra templates: Azure Data Factory pipeline JSON stub, Databricks notebook script.
- CI: GitHub Actions workflow for tests and container build.
- Docs: architecture, data dictionary, usage guide.

**Repository structure**
```
├─ data/                      # synthetic data CSV
├─ notebooks/                 # analysis & model notebooks (py scripts)
├─ src/                       # source code: etl, features, train, serve
├─ infra/                     # infra templates (ADF, Databricks)
├─ docs/                      # architecture and design docs
├─ .github/workflows/         # CI workflow
├─ Dockerfile
├─ requirements.txt
└─ README.md
```

**How to use**
1. Create a Python 3.9+ venv and install: `pip install -r requirements.txt`
2. Generate data: `python src/data_generator.py --out data/sensor_readings.csv --n_machines 10 --days 30`
3. Run ETL: `python src/etl.py --in data/sensor_readings.csv --out data/processed.csv`
4. Train model: `python src/train_model.py --in data/processed.csv --model_out models/xgb_model.json`
5. Serve model: `docker build -t pg-smart-manufacturing . && docker run -p 5000:5000 pg-smart-manufacturing`

**License:** MIT
**Author:** Generated for P&G role match demonstration
**Generated on:** 2025-09-29
