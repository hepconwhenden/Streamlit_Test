import streamlit as st

st.set_page_config(page_title="数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0

# カウント表示
st.markdown(f"<h1 style='text-align:center;'>📱 {st.session_state.count}</h1>", unsafe_allow_html=True)

# ボタン配置
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("カウントアップ", use_container_width=True):
        st.session_state.count += 1

# リセットボタン
with st.sidebar:
    if st.button("リセット"):
        st.session_state.count = 0
