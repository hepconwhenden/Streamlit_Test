import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="画像落書きアプリ", layout="centered")
st.title("🖌️ 画像に落書きするアプリ")

uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    st.image(image, caption="元画像", use_container_width=True)

    # 背景画像を使わず、キャンバスサイズだけ合わせる
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",
        stroke_width=5,
        stroke_color="#ff0000",
        background_color="#ffffff",  # 白背景
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("保存して表示"):
        if canvas_result.image_data is not None:
            result_image = Image.fromarray(canvas_result.image_data.astype("uint8"))
            st.image(result_image, caption="保存された画像", use_container_width=True)

            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            st.download_button(
                label="画像をダウンロード",
                data=buf.getvalue(),
                file_name="drawing.png",
                mime="image/png"
            )
