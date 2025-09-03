import streamlit as st

st.set_page_config(page_title="縦型数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0

# カウントアップボタン（上）
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
if st.button("➕ カウントアップ", use_container_width=True):
    st.session_state.count += 1

# 数値表示（中央）
st.markdown(
    f"""
    <h1 style="text-align:center; font-size:5em; margin:0.5em 0;">📱 {st.session_state.count}</h1>
    """,
    unsafe_allow_html=True
)

# カウントダウンボタン（下）
if st.button("➖ カウントダウン", use_container_width=True):
    st.session_state.count -= 1
st.markdown("</div>", unsafe_allow_html=True)

# リセットボタン（サイドバー）
with st.sidebar:
    if st.button("リセット"):
        st.session_state.count = 0
        st.rerun()
