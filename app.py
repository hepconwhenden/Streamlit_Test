import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import pandas as pd

st.title("📸 画像に描画できる Streamlit アプリ")

# Sidebar 設定
st.sidebar.header("🛠️ 描画ツール設定")
drawing_mode = st.sidebar.selectbox("描画モード", ("freedraw", "line", "rect", "circle", "point", "transform"))
stroke_width = st.sidebar.slider("線の太さ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("線の色", "#000000")
bg_color = st.sidebar.color_picker("背景色（画像がない場合）", "#eeeeee")
realtime_update = st.sidebar.checkbox("リアルタイム更新", True)

# Point モード用の半径設定
point_display_radius = st.sidebar.slider("ポイント表示半径", 1, 25, 3) if drawing_mode == "point" else 0

# 背景画像のアップロード
bg_image_file = st.sidebar.file_uploader("背景画像をアップロード", type=["png", "jpg", "jpeg"])

# 背景画像の読み込みとサイズ取得
if bg_image_file:
    image = Image.open(bg_image_file)
    width, height = image.size
else:
    image = None
    width, height = 600, 400  # デフォルトサイズ

# Canvas の表示
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # オレンジの半透明
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=image,
    update_streamlit=realtime_update,
    height=height,
    width=width,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius,
    key="canvas",
)

# 描画結果の表示
st.subheader("🖼️ 描画結果")
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

# 描画オブジェクトのデータ表示
if canvas_result.json_data is not None:
    st.subheader("📋 描画オブジェクトの詳細")
    objects = pd.json_normalize(canvas_result.json_data["objects"])
    for col in objects.select_dtypes(include=["object"]).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)
