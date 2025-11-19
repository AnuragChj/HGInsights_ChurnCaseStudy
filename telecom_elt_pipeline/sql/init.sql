CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;

-- analytics / reporting table
DROP TABLE IF EXISTS analytics.telecom_churn_clean;

CREATE TABLE analytics.telecom_churn_clean (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER,
    gender TEXT,
    tenure INTEGER,
    monthly_charges NUMERIC,
    contract_type TEXT,
    internet_service TEXT,
    total_charges NUMERIC,
    tech_support BOOLEAN,
    churn BOOLEAN
);

CREATE INDEX IF NOT EXISTS idx_analytics_churn
    ON analytics.telecom_churn_clean (churn);