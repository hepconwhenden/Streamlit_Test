import streamlit as st

# 換算係数（基準は N・m）
conversion_factors = {
    "N・m": 1,
    "cN・m": 100,
    "kgf・m": 0.101972,
    "kgf・cm": 10.1972,
    "lbf・ft": 0.737562,
    "lbf・in": 8.85075
}

# 単位の日本語説明（任意）
unit_descriptions = {
    "N・m": "ニュートン・メートル",
    "cN・m": "センチニュートン・メートル",
    "kgf・m": "キログラム重・メートル",
    "kgf・cm": "キログラム重・センチメートル",
    "lbf・ft": "ポンド・フィート",
    "lbf・in": "ポンド・インチ"
}

# タイトル
st.title("🔧 トルク換算ツール")

# 入力UI
value = st.number_input("数値を入力", min_value=0.0, format="%.4f")
from_unit = st.selectbox("変換元の単位", conversion_factors.keys())
to_unit = st.selectbox("変換先の単位", conversion_factors.keys())

# 換算処理
if st.button("換算する"):
    # N・mに変換 → 目的の単位へ変換
    value_in_Nm = value / conversion_factors[from_unit]
    converted_value = value_in_Nm * conversion_factors[to_unit]

    st.success(f"{value:.4f} {from_unit}（{unit_descriptions[from_unit]}） は "
               f"{converted_value:.4f} {to_unit}（{unit_descriptions[to_unit]}） です")

# オプション：すべての単位への一括換算表示
st.markdown("### 📊 一括換算結果")
if value > 0:
    value_in_Nm = value / conversion_factors[from_unit]
    for unit, factor in conversion_factors.items():
        result = value_in_Nm * factor
        st.write(f"- {result:.4f} {unit}（{unit_descriptions[unit]}）")
