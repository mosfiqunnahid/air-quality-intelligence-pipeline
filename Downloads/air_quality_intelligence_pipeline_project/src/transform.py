from typing import List, Dict, Any
from datetime import datetime
import pandas as pd


def transform_air_quality_data(raw_payloads: List[Dict[str, Any]]) -> pd.DataFrame:
    records = []

    pollutant_columns = {
        "pm10": "PM10",
        "pm2_5": "PM2.5",
        "carbon_monoxide": "CO",
        "nitrogen_dioxide": "NO2",
        "ozone": "O3"
    }

    for payload in raw_payloads:
        city = payload["city"]
        latitude = payload["latitude"]
        longitude = payload["longitude"]

        hourly = payload.get("hourly", {})
        times = hourly.get("time", [])

        for i, timestamp in enumerate(times):
            for column, pollutant_name in pollutant_columns.items():
                values = hourly.get(column, [])

                if i < len(values):
                    records.append({
                        "city": city,
                        "parameter": pollutant_name,
                        "value": values[i],
                        "unit": "µg/m³",
                        "datetime_utc": timestamp,
                        "latitude": latitude,
                        "longitude": longitude,
                        "extracted_at": datetime.utcnow().isoformat()
                    })

    df = pd.DataFrame(records)

    if df.empty:
        return df

    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["datetime_utc"] = pd.to_datetime(df["datetime_utc"], errors="coerce")

    return df