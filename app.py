import streamlit as st
import time
from gtts import gTTS
import base64
import os

def autoplay_audio(file_path):
    if not os.path.exists(file_path):
        st.error(f"ファイルが見つかりません: {file_path}")
        return
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

st.title("⏳ ラスト秒数を指定して読み上げるタイマー")

# 入力項目
total_time = st.number_input("合計時間（秒）", min_value=10, value=60)
interval = st.number_input("通常読み上げ間隔（秒）", min_value=1, value=15)
last_phase = st.number_input("ラスト何秒から毎秒読み上げするか", min_value=1, max_value=total_time, value=10)

if st.button("スタート"):
    placeholder = st.empty()
    start_time = time.time()

    while True:
        elapsed = int(time.time() - start_time)
        remaining = total_time - elapsed

        if remaining <= 0:
            placeholder.markdown("### ✅ タイマー終了！")

            # 🔊 ビープ音 → 少し待って → 読み上げ
            autoplay_audio("beep.mp3")
            time.sleep(2)  # ビープ音の長さに応じて調整

            tts = gTTS("タイマー終了です", lang='ja')
            tts.save("end.mp3")
            autoplay_audio("end.mp3")
            break

        placeholder.markdown(f"### 残り時間：{remaining} 秒")

        if elapsed != 0 and elapsed % interval == 0 and remaining > last_phase:
            tts = gTTS(f"{elapsed} 秒経過", lang='ja')
            tts.save("say.mp3")
            autoplay_audio("say.mp3")

        if remaining <= last_phase:
            tts = gTTS(f"{remaining}", lang='ja')
            tts.save("countdown.mp3")
            autoplay_audio("countdown.mp3")

        time.sleep(1)
