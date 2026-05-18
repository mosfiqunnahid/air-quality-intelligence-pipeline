import os
import pandas as pd
import folium
from folium.plugins import HeatMap
DATA_PATH = "data/processed/air_quality_data.csv"
OUTPUT_MAP = "reports/figures/air_quality_map.html"

def create_air_quality_map():
    os.makedirs(os.path.dirname(OUTPUT_MAP), exist_ok=True)
    df = pd.read_csv(DATA_PATH).dropna(subset=["latitude", "longitude", "value"])
    m = folium.Map(location=[51.16, 10.45], zoom_start=4)
    HeatMap(df[["latitude", "longitude", "value"]].values.tolist(), radius=8, blur=12).add_to(m)
    for _, row in df.head(100).iterrows():
        popup = f"<b>Pollutant:</b> {row['parameter']}<br><b>Value:</b> {row['value']} {row.get('unit','')}<br><b>Time:</b> {row.get('datetime_utc','')}"
        folium.CircleMarker(location=[row["latitude"], row["longitude"]], radius=4, popup=popup, color="blue", fill=True, fill_opacity=0.6).add_to(m)
    m.save(OUTPUT_MAP)
    print(f"Air quality map saved to {OUTPUT_MAP}")
if __name__ == "__main__": create_air_quality_map()
