import os
import pandas as pd
import streamlit as st
import plotly.express as px
DATA_PATH = "data/processed/air_quality_data.csv"
st.set_page_config(page_title="Air Quality Intelligence Dashboard", layout="wide")
st.title("Air Quality Intelligence Dashboard")
st.write("Interactive dashboard for OpenAQ air-quality measurements.")
if not os.path.exists(DATA_PATH):
    st.error("No processed data found. Run: python3 src/main.py")
    st.stop()
df = pd.read_csv(DATA_PATH)
if df.empty:
    st.warning("Dataset is empty")
    st.stop()
selected = st.selectbox("Select Pollutant", sorted(df["parameter"].dropna().unique()))
filtered = df[df["parameter"] == selected]
col1, col2, col3 = st.columns(3)
col1.metric("Measurements", len(filtered))
col2.metric("Average Value", round(filtered["value"].mean(), 2))
col3.metric("Max Value", round(filtered["value"].max(), 2))
st.subheader("Pollutant Value Distribution")
st.plotly_chart(px.histogram(filtered, x="value", nbins=40, title=f"Distribution of {selected}"), use_container_width=True)
st.subheader("Average Pollution by Pollutant")
avg_df = df.groupby("parameter", as_index=False)["value"].mean()
st.plotly_chart(px.bar(avg_df, x="parameter", y="value", title="Average Value by Pollutant"), use_container_width=True)
st.subheader("Geospatial Measurement Points")
map_df = filtered.dropna(subset=["latitude", "longitude"]).head(1000)
fig_map = px.scatter_mapbox(map_df, lat="latitude", lon="longitude", color="value", hover_data=["parameter", "value", "unit"], zoom=2, height=500, title=f"Map of {selected} Measurements")
fig_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig_map, use_container_width=True)
st.subheader("Data Preview")
st.dataframe(filtered.head(100))
