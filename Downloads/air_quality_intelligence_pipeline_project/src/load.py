import os, logging
import pandas as pd
from config import PROCESSED_DATA_PATH
from database import load_dataframe_to_postgres
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_to_csv(df: pd.DataFrame, path: str = PROCESSED_DATA_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path): df.to_csv(path, mode="a", header=False, index=False)
    else: df.to_csv(path, index=False)
    logging.info(f"Saved {len(df)} rows to {path}")

def load_outputs(df: pd.DataFrame, use_postgres: bool = False) -> None:
    save_to_csv(df)
    if use_postgres: load_dataframe_to_postgres(df)
