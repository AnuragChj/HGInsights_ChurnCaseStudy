# Telecom Customer Churn ELT Pipeline

Step by step overview

This project implements a ELT pipeline for a telecom churn CSV Kaggle dataset using:

- Python (pandas, SQLAlchemy)
- PostgreSQL (staging + analytics schemas)
- APScheduler (orchestration, hourly)
- Metabase (reporting/dashboard)
- Docker + docker-compose (fully containerised)


Process:

1. Raw CSV is ingested into the staging schema.
2. Data is transformed (missing values handled, PII anonymised).
3. Cleaned data is loaded into the analytics schema.
4. Metabase connects to PostgreSQL and provides reports on churn.


Running guidelines:

1. Download the telecom churn CSV from Kaggle and save it as:

 data/raw/telecom_churn.csv

 It is uploaded  in the public Github repository shared with the same path:

 data/raw/telecom_churn.csv


2.Copy .env.example to .env and adjust scheduler minutes/ configurations if needed.

3.Build and start the stack:
docker-compose up --build


4.The pipeline will run immediately. It is scheduled to run every 60 minutes by default.

5.Open Metabase at http://localhost:3000
 and connect to the elt_db Postgres database.


Here is the repository hierarchy for details:

telecom-elt-pipeline/
├─ docker-compose.yml
├─ README.md
├─ requirements.txt
├─ .env.example
├─ data/
│  └─ raw/          # telecom churn CSV stored here
├─ sql/
│  └─ init.sql      # DB schemas
└─ app/
   ├─ __init__.py
   ├─ config.py
   ├─ db.py
   ├─ pipeline.py   # Extract data -> Load data -> Transform ->Load data
   └─ main.py       # orchestration (start)

