"""Display validated forecast records in a local Streamlit dashboard."""

import streamlit as st

from auburn_weather_monitor.api import ApiError
from auburn_weather_monitor.cli import DEFAULT_LATITUDE, DEFAULT_LONGITUDE
from auburn_weather_monitor.config import get_user_agent
from auburn_weather_monitor.logging_config import configure_logging
from auburn_weather_monitor.service import get_forecast


st.set_page_config(page_title="Auburn Weather Monitor", page_icon="🌤️")
st.title("Auburn Weather Monitor")
st.write("Enter coordinates and load a validated National Weather Service forecast.")

latitude = st.number_input("Latitude", value=DEFAULT_LATITUDE, format="%.4f")
longitude = st.number_input("Longitude", value=DEFAULT_LONGITUDE, format="%.4f")
st.caption("A live request requires internet access. No API key is required.")

if st.button("Load forecast", type="primary"):
    configure_logging("INFO")
    try:
        _, records = get_forecast(latitude, longitude, get_user_agent())
    except ApiError as error:
        st.error(str(error))
    else:
        if not records:
            st.warning("The API returned no forecast periods.")
        else:
            first = records[0]
            col1, col2 = st.columns(2)
            col1.metric("First period", str(first["name"]))
            col2.metric(
                "Temperature",
                f'{first["temperature"]} {first["temperature_unit"]}',
            )
            st.dataframe(records, use_container_width=True, hide_index=True)
