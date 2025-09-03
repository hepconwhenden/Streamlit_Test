import streamlit as st

st.set_page_config(page_title="数取器", layout="centered")

# 初期化（最上部で1回だけ）
if "count" not in st.session_state:
    st.session_state.count = 0

# カウント表示（中央揃え）
st.markdown(
    f"""
    <div style="text-align:center;">
        <h1 style="font-size:5em;">📱 {st.session_state.count}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# カウントアップボタン（中央配置）
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("カウントアップ", use_container_width=True):
        st.session_state.count += 1

# リセットボタン（サイドバー）
with st.sidebar:
    if st.button("リセット"):
        st.session_state.count = 0
        st.rerun()  # ← これが「1番の方法」
