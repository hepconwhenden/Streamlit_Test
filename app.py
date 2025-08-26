import streamlit as st
import math

st.title("🧮 数式対応電卓（√・カッコ・三角関数OK）")

st.markdown("""
**使える関数一覧：**
- `sqrt(x)`：平方根
- `sin(x)`、`cos(x)`、`tan(x)`：三角関数（ラジアン）
- `log(x)`、`log10(x)`：自然対数・常用対数
- `abs(x)`、`round(x)`：絶対値・四捨五入
- `pow(x, y)`：累乗
""")

# 数式入力欄
expression = st.text_input("数式を入力してください", value="sin(math.pi / 2) + cos(0)")

# 安全な評価関数
def safe_eval(expr):
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names.update({
        "abs": abs,
        "round": round,
        "pow": pow,
        "math": math  # 明示的に math.pi などを使えるように
    })

    return eval(expr, {"__builtins__": {}}, allowed_names)

# 計算実行
if st.button("計算する"):
    try:
        result = safe_eval(expression)
        st.success(f"結果：{result}")
    except Exception as e:
        st.error(f"エラー：{e}")
