import streamlit as st

st.set_page_config(page_title="数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0
if "increment_flag" not in st.session_state:
    st.session_state.increment_flag = False

# カウントアップ処理（フラグを使う）
if st.button("カウントアップ", use_container_width=True):
    st.session_state.increment_flag = True
    st.rerun()

# フラグが立っていたらカウントを増やす
if st.session_state.increment_flag:
    st.session_state.count += 1
    st.session_state.increment_flag = False

# カウント表示
st.markdown(
    f"""
    <div style="text-align:center;">
        <h1 style="font-size:5em;">📱 {st.session_state.count}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# リセットボタン（サイドバー）
with st.sidebar:
    if st.button("リセット"):
        st.session_state.count = 0
        st.rerun()
