import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "elt_db")
DB_USER = os.getenv("DB_USER", "elt_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "elt_password")

CSV_PATH = os.getenv("CSV_PATH", "/data/raw/telecom_churn.csv")

SCHEDULE_MINUTES = int(os.getenv("SCHEDULE_MINUTES", "60"))

SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"