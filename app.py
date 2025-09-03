import streamlit as st

st.set_page_config(page_title="縦型数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0

# カウントアップ処理
def increment():
    st.session_state.count += 1

# カウントダウン処理
def decrement():
    st.session_state.count -= 1

# リセット処理
def reset():
    st.session_state.count = 0

# レイアウト（中央揃え）
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

# カウントアップボタン（上）
st.button("➕ カウントアップ", on_click=increment, use_container_width=True)

# 数値表示（中央）
st.markdown(
    f"""
    <h1 style="text-align:center; font-size:5em; margin:0.5em 0;">📱 {st.session_state.count}</h1>
    """,
    unsafe_allow_html=True
)

# カウントダウンボタン（下）
st.button("➖ カウントダウン", on_click=decrement, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# リセットボタン（サイドバー）
with st.sidebar:
    st.button("リセット", on_click=reset)
