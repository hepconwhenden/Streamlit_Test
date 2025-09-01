import streamlit as st
import time
import pyttsx3

# 音声エンジン初期化（注意：一部環境では非同期処理が必要）
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 読み上げ速度

st.title("📢 1秒間隔で読み上げするタイマー")

# 入力：合計時間と読み上げ間隔
total_time = st.number_input("合計時間（秒）", min_value=1, value=30)
interval = st.number_input("読み上げ間隔（秒）", min_value=1, value=10)

if st.button("スタート"):
    placeholder = st.empty()
    start_time = time.time()
    next_read = interval

    while True:
        elapsed = int(time.time() - start_time)
        remaining = total_time - elapsed

        if remaining <= 0:
            placeholder.markdown("### ✅ タイマー終了！")
            engine.say("タイマー終了です")
            engine.runAndWait()
            break

        placeholder.markdown(f"### 残り時間：{remaining} 秒")

        # 読み上げタイミング（1秒ごとにチェック）
        if elapsed != 0 and elapsed % interval == 0:
            engine.say(f"{elapsed} 秒経過しました")
            engine.runAndWait()

        time.sleep(1)
