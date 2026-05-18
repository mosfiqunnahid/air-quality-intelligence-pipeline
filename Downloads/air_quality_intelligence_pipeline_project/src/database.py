import os, logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from config import TABLE_NAME
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_engine():
    if not DATABASE_URL: raise ValueError("DATABASE_URL is missing in .env")
    return create_engine(DATABASE_URL)

def create_table_if_not_exists():
    engine = get_engine()
    sql = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id SERIAL PRIMARY KEY,
        parameter TEXT,
        value DOUBLE PRECISION,
        unit TEXT,
        datetime_utc TIMESTAMP,
        datetime_local TEXT,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION,
        sensor_id INTEGER,
        location_id INTEGER,
        extracted_at TIMESTAMP
    );
    """
    with engine.begin() as conn:
        conn.execute(text(sql))
    logging.info(f"Table ready: {TABLE_NAME}")

def load_dataframe_to_postgres(df):
    if df.empty:
        logging.warning("No rows to load into PostgreSQL")
        return
    engine = get_engine()
    create_table_if_not_exists()
    df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
    logging.info(f"Loaded {len(df)} rows into PostgreSQL")
