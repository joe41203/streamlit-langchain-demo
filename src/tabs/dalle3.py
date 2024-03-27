import streamlit as st
import settings
from openai import OpenAI
import requests
from io import BytesIO
from PIL import Image
import uuid

def dalle3():
    st.header("DALL-E3")
    image_description = st.text_input("プロンプトを入力してください", max_chars=200)

    if st.button("画像生成"):
        with st.spinner("画像を生成中..."):
            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            response = client.images.generate(
                model="dall-e-3",
                prompt=image_description,
                size="1792x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url

            # 画像をダウンロードして表示
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="生成された画像", use_column_width=True)

            # ランダムなファイル名を生成
            random_filename = str(uuid.uuid4()) + ".webp"

            # 画像を圧縮してWebP形式で保存
            webp_buffer = BytesIO()
            image.save(webp_buffer, format="WebP", quality=10)
            webp_buffer.seek(0)
            st.download_button(
                label="画像をダウンロード",
                data=webp_buffer,
                file_name=random_filename,
                mime="image/webp",
            )
