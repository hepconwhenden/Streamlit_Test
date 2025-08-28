import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import io

st.title("画像に落書きするアプリ 🎨")

# 画像アップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="元画像", use_column_width=True)

    # Canvas設定
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",  # 塗りつぶし色
        stroke_width=5,
        stroke_color="#ff0000",
        background_image=image,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="freedraw",
        key="canvas",
    )

    # 保存処理
    if st.button("保存"):
        if canvas_result.image_data is not None:
            result_image = Image.fromarray(canvas_result.image_data.astype("uint8"))
            st.image(result_image, caption="保存された画像")
            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            st.download_button("ダウンロード", buf.getvalue(), file_name="drawing.png", mime="image/png")
