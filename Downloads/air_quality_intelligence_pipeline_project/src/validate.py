import pandas as pd
REQUIRED_COLUMNS = ["parameter", "value", "datetime_utc", "latitude", "longitude"]

def validate_air_quality_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return df
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing: raise ValueError(f"Missing required columns: {missing}")
    df = df.drop_duplicates()
    df = df.dropna(subset=REQUIRED_COLUMNS)
    df = df[(df["value"] >= 0) & (df["value"] < 5000)]
    df = df[(df["latitude"].between(-90, 90)) & (df["longitude"].between(-180, 180))]
    return df
