import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import requests

st.title("📱 現在地の気温（Open-Meteo）")

# 位置情報の取得
location = streamlit_geolocation()

if location:
    lat = location["latitude"]
    lon = location["longitude"]
    st.success(f"現在地：緯度 {lat:.4f}, 経度 {lon:.4f}")

    # Open-Meteo APIで現在の気象データ取得
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]
        weather_code = data["current_weather"]["weathercode"]

        st.metric(label="🌡️ 気温", value=f"{temp:.1f} °C")
        st.write(f"💨 風速：{wind} km/h")
        st.write(f"🧭 天気コード：{weather_code}")
    else:
        st.error("気象データの取得に失敗しました。")
else:
    st.warning("位置情報の取得を許可してください。")
