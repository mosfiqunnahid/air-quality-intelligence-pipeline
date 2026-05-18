import argparse, logging
from extract import extract_air_quality_data
from transform import transform_air_quality_data
from validate import validate_air_quality_data
from load import load_outputs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline(use_postgres: bool = False):
    logging.info("Starting Air Quality Intelligence Pipeline")
    raw_payloads = extract_air_quality_data()
    df = transform_air_quality_data(raw_payloads)
    df = validate_air_quality_data(df)
    if df.empty:
        logging.warning("No valid air-quality records found")
        return
    load_outputs(df, use_postgres=use_postgres)
    logging.info(f"Pipeline completed with {len(df)} valid records")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--postgres", action="store_true", help="Load into PostgreSQL as well as CSV")
    args = parser.parse_args()
    run_pipeline(use_postgres=args.postgres)
