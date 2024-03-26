import streamlit as st
import settings
from openai import OpenAI


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
        st.image(image_url, caption="生成された画像", use_column_width=True)
