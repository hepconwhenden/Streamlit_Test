import streamlit as st

st.set_page_config(page_title="数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0

# カウントアップ処理
def increment():
    st.session_state.count += 1

# リセット処理
def reset():
    st.session_state.count = 0
    st.experimental_rerun()

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
    st.button("カウントアップ", on_click=increment, use_container_width=True)

# リセットボタン（サイドバー）
with st.sidebar:
    st.button("リセット", on_click=reset)
