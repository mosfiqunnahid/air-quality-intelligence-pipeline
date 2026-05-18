import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

import requests

from config import RAW_DATA_PATH

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

CITIES = {
    "Dortmund": (51.5136, 7.4653),
    "Berlin": (52.5200, 13.4050),
    "Hamburg": (53.5511, 9.9937),
    "Munich": (48.1351, 11.5820),
    "Cologne": (50.9375, 6.9603),
    "Düsseldorf": (51.2277, 6.7735),
    "Essen": (51.4556, 7.0116)
}


def fetch_air_quality(city: str, latitude: float, longitude: float) -> Dict[str, Any]:
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone",
        "timezone": "Europe/Berlin"
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()
    data["city"] = city
    data["latitude"] = latitude
    data["longitude"] = longitude

    logging.info(f"Fetched air-quality data for {city}")
    return data


def extract_air_quality_data() -> List[Dict[str, Any]]:
    raw_payloads = []

    for city, coords in CITIES.items():
        latitude, longitude = coords
        payload = fetch_air_quality(city, latitude, longitude)
        raw_payloads.append(payload)

    save_raw_json(raw_payloads)
    return raw_payloads


def save_raw_json(payloads: List[Dict[str, Any]], path: str = RAW_DATA_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    output = {
        "extracted_at_utc": datetime.utcnow().isoformat(),
        "source": "Open-Meteo Air Quality API",
        "payloads": payloads
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)

    logging.info(f"Raw air-quality data saved to {path}")