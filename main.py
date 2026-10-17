import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

sample = [
    {
        "name": "Sample location A",
        "lat": 27.77,
        "lon": -82.64,
        "concentration": "Example: background"
    },
    {
        "name": "Sample location B",
        "lat": 27.50,
        "lon": -82.70,
        "concentration": "Example: elevated"
    },
]

m = folium.Map(
    location=[27.7, -82.6],
    zoom_start=8,
    tiles="OpenStreetMap"
)

for sample in sample:
    folium.CircleMarker(
        location=[sample["lat"], sample["lon"]],
        radius=7,
        popup=(
            f'{sample["name"]}<br>'
            f'{sample["concentration"]}'
        ),
        tooltip=sample["name"],
        fill=True,
        fill_opacity=0.8
    ).add_to(m)

m.save("red_tide_map.html")