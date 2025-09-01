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

st.title("⏳ タイマー開始・終了アナウンス付きタイマー")

# 入力項目（分＋秒）
minutes_input = st.number_input("分（0以上）", min_value=0, value=1)
seconds_input = st.number_input("秒（0以上、60以上もOK）", min_value=0, value=0)

# 合計秒数を計算（秒が60以上でも繰り上げ）
total_time = minutes_input * 60 + seconds_input

interval = st.number_input("通常読み上げ間隔（秒）", min_value=1, value=15)
last_phase = st.number_input("ラスト何秒から毎秒読み上げするか", min_value=1, max_value=total_time, value=10)

if st.button("スタート"):
    placeholder = st.empty()

    # 🔔 開始アナウンス
    tts = gTTS("タイマーを開始します", lang='ja')
    tts.save("start.mp3")
    autoplay_audio("start.mp3")
    time.sleep(2)

    start_time = time.time()

    while True:
        elapsed = int(time.time() - start_time)
        remaining = total_time - elapsed

        if remaining < 0:
            break

        placeholder.markdown(f"### 残り時間：{remaining} 秒")

        # 通常の読み上げ（ラストフェーズ前）
        if elapsed != 0 and elapsed % interval == 0 and remaining > last_phase:
            tts = gTTS(f"{elapsed} 秒経過", lang='ja')
            tts.save("say.mp3")
            autoplay_audio("say.mp3")

        # ラストフェーズ：毎秒読み上げ（0秒も含む）
        if remaining <= last_phase:
            tts = gTTS(f"{remaining}", lang='ja')
            tts.save("countdown.mp3")
            autoplay_audio("countdown.mp3")

        if remaining == 0:
            # 🔊 0秒の読み上げ（再度明示的に）
            tts = gTTS("0", lang='ja')
            tts.save("zero.mp3")
            autoplay_audio("zero.mp3")
            time.sleep(1.5)

            # ✅ 終了アナウンス
            placeholder.markdown("### ✅ タイマー終了！")
            tts = gTTS("タイマー終了です", lang='ja')
            tts.save("end.mp3")
            autoplay_audio("end.mp3")
            time.sleep(2)
            break

        time.sleep(1)
