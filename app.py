import streamlit as st
import math

st.title("📱 タップ式数式電卓")

# セッション状態で式を保持
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ボタン群
buttons = [
    ["7", "8", "9", "/", "sqrt("],
    ["4", "5", "6", "*", "sin("],
    ["1", "2", "3", "-", "cos("],
    ["0", ".", "(", ")", "+"],
    ["C", "←", "=", "pi", "tan("]
]

# 数式表示
st.text_input("数式", value=st.session_state.expression, key="display", disabled=True)

# ボタン描画
for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        if cols[i].button(label):
            if label == "C":
                st.session_state.expression = ""
            elif label == "←":
                st.session_state.expression = st.session_state.expression[:-1]
            elif label == "=":
                try:
                    allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
                    allowed.update({"abs": abs, "round": round, "pi": math.pi})
                    result = eval(st.session_state.expression, {"__builtins__": {}}, allowed)
                    st.session_state.expression = str(result)
                except Exception as e:
                    st.error(f"エラー：{e}")
            else:
                st.session_state.expression += label
