import streamlit as st
import requests
from streamlit_geolocation import geolocation  # GPS取得

# WeatherAPIのAPIキー
API_KEY = "722378415b404ea395945853252608"

st.title("📱 WeatherAPIで現在地の気温取得")

location = geolocation()

if location:
    lat = location["latitude"]
    lon = location["longitude"]
    st.success(f"現在地：緯度 {lat:.4f}, 経度 {lon:.4f}")

    # WeatherAPIのエンドポイント
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&lang=ja"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        wind = data["current"]["wind_kph"]
        st.metric(label="🌡️ 気温", value=f"{temp:.1f} °C")
        st.write(f"🌤️ 天気：{condition}")
        st.write(f"💨 風速：{wind} km/h")
    else:
        st.error("WeatherAPIからのデータ取得に失敗しました。")
else:
    st.warning("位置情報の取得を許可してください。")
