# Air Quality Intelligence Pipeline

An environmental data engineering and GIS analytics project for collecting, processing, storing, analyzing, and visualizing air-quality measurements using OpenAQ API, Python, PostgreSQL, SQL, Folium, Plotly, and Streamlit.

## Features

- Collect air-quality data from OpenAQ REST API
- Transform JSON responses into structured datasets
- Store data in CSV and optionally PostgreSQL
- Analyze pollutants such as PM2.5, PM10, NO2, O3, and CO
- Create GIS-based pollution maps
- Build an interactive Streamlit dashboard

## Technologies

Python • REST APIs • Pandas • PostgreSQL • SQLAlchemy • SQL • Folium • Plotly • Streamlit • GIS

## Workflow

```text
OpenAQ API → Python ETL → CSV/PostgreSQL → SQL Analytics → GIS Map → Dashboard
```

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 src/main.py
python3 src/eda.py
python3 src/create_map.py
streamlit run dashboard/app.py
```

To also load into PostgreSQL:

```bash
python3 src/main.py --postgres
```

## Output

- data/raw/openaq_raw.json
- data/processed/air_quality_data.csv
- reports/figures/air_quality_map.html
- Streamlit dashboard

## Learning Outcomes

REST API ingestion, JSON processing, ETL pipeline development, PostgreSQL loading, SQL analytics, GIS visualization, and dashboard development.
