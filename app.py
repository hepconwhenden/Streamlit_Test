import streamlit as st
import time
from datetime import datetime

st.title("⏳ ミリ秒付きタイマー")

total_time = st.number_input("合計時間（秒）", min_value=1, value=10)
interval = st.number_input("読み上げ間隔（秒）", min_value=1, value=3)

if st.button("スタート"):
    placeholder = st.empty()
    start_time = time.time()
    next_read_time = start_time + interval

    while True:
        now = time.time()
        elapsed = now - start_time
        remaining = total_time - elapsed

        if remaining <= 0:
            placeholder.markdown("### ✅ タイマー終了！")
            break

        # ミリ秒付きで表示（小数点第3位まで）
        placeholder.markdown(f"### 残り時間：{remaining:.3f} 秒")

        if now >= next_read_time:
            st.write(f"🔊 読み上げ：残り {remaining:.3f} 秒")
            next_read_time += interval

        time.sleep(0.05)  # 50ms間隔で更新
