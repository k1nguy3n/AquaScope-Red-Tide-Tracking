import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="AquaScope",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 AquaScope")
st.subheader("Red Tide Monitoring Dashboard")
st.write("Explore sampling locations and their reported conditions.")

# Temporary demo locations — NOT real measurements
sampling_points = [
    {
        "name": "Sample Site A",
        "lat": 27.7676,
        "lon": -82.6403,
        "level": "Low",
        "color": "green",
        "details": "Demo location near St. Petersburg, Florida."
    },
    {
        "name": "Sample Site B",
        "lat": 27.8006,
        "lon": -82.5523,
        "level": "Moderate",
        "color": "orange",
        "details": "Demo location. No real sample data available."
    },
    {
        "name": "Sample Site C",
        "lat": 27.6770,
        "lon": -82.7370,
        "level": "High",
        "color": "red",
        "details": "Demo location. No real sample data available."
    },
]

# Center map around the sample sites
m = folium.Map(
    location=[27.75, -82.64],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# Add clickable sampling markers
for point in sampling_points:
    popup_html = f"""
    <div style="width: 200px">
        <h4>{point['name']}</h4>
        <b>Demo category:</b> {point['level']}<br>
        <b>Coordinates:</b><br>
        {point['lat']:.4f}, {point['lon']:.4f}<br><br>
        {point['details']}
    </div>
    """

    folium.Marker(
        location=[point["lat"], point["lon"]],
        tooltip=point["name"],
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(
            color=point["color"],
            icon="info-sign"
        )
    ).add_to(m)

# Display map in Streamlit
st_folium(
    m,
    use_container_width=True,
    height=600,
    returned_objects=[]
)

st.caption(
    "DEMO ONLY: Locations and categories are illustrative, "
    "not actual red tide observations."
)

