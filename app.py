import streamlit as st
import time
from gtts import gTTS
import os

st.title("🔊 gTTSで読み上げするタイマー")

total_time = st.number_input("合計時間（秒）", min_value=1, value=30)
interval = st.number_input("読み上げ間隔（秒）", min_value=1, value=10)

if st.button("スタート"):
    placeholder = st.empty()
    start_time = time.time()

    while True:
        elapsed = int(time.time() - start_time)
        remaining = total_time - elapsed

        if remaining <= 0:
            placeholder.markdown("### ✅ タイマー終了！")
            tts = gTTS("タイマー終了です", lang='ja')
            tts.save("end.mp3")
            audio_file = open("end.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")
            break

        placeholder.markdown(f"### 残り時間：{remaining} 秒")

        if elapsed != 0 and elapsed % interval == 0:
            tts = gTTS(f"{elapsed} 秒経過しました", lang='ja')
            tts.save("say.mp3")
            audio_file = open("say.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

        time.sleep(1)
