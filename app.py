import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="画像落書きアプリ", layout="centered")
st.title("🖌️ 画像に落書きするアプリ")

uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # PIL形式に変換し、RGBAモードに統一
    image = Image.open(uploaded_file).convert("RGBA")
    st.image(image, caption="元画像", use_container_width=True)

    # Canvas描画
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",  # 塗りつぶし色
        stroke_width=5,
        stroke_color="#ff0000",
        background_image=image,  # PIL.Image形式で渡す
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="freedraw",
        key="canvas",
    )

    # 描画結果の保存と表示
    if st.button("保存して表示"):
        if canvas_result.image_data is not None:
            result_image = Image.fromarray(canvas_result.image_data.astype("uint8"))
            st.image(result_image, caption="保存された画像", use_container_width=True)

            # ダウンロードボタン
            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            st.download_button(
                label="画像をダウンロード",
                data=buf.getvalue(),
                file_name="drawing.png",
                mime="image/png"
            )
