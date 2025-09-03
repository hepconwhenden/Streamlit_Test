import streamlit as st

st.set_page_config(page_title="縦型数取器", layout="centered")

# 初期化
if "count" not in st.session_state:
    st.session_state.count = 0
if "action" not in st.session_state:
    st.session_state.action = None

# ボタン押下 → フラグをセット
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

if st.button("➕ カウントアップ", use_container_width=True):
    st.session_state.action = "up"
    st.rerun()

st.markdown(
    f"""
    <h1 style="text-align:center; font-size:5em; margin:0.5em 0;">📱 {st.session_state.count}</h1>
    """,
    unsafe_allow_html=True
)

if st.button("➖ カウントダウン", use_container_width=True):
    st.session_state.action = "down"
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# フラグに応じて処理（再実行後に確実に反映）
if st.session_state.action == "up":
    st.session_state.count += 1
    st.session_state.action = None
elif st.session_state.action == "down":
    st.session_state.count -= 1
    st.session_state.action = None

# リセットボタン（サイドバー）
with st.sidebar:
    if st.button("リセット"):
        st.session_state.count = 0
        st.session_state.action = None
        st.rerun()
