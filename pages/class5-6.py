import streamlit as st
import base64
import openai

openai.api_key=st.secrets['OPENAI_API_KEY']

st.title("AI圖像分析")

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpeg", "jpg"])

if uploaded_file:  
    st.image(uploaded_file, caption="已上傳圖片", width=300)

    with open ("temp_image.jpg","wb") as f:
        f.write(uploaded_file.getbuffer())

    with open ("temp_image.jpg","rb") as image_file:
        base64_image= base64.b64encode(image_file.read()).decode("utf-8")


prompt= st.chat_input("請輸入訊息")
if prompt:
    response= openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text": prompt,
                    },
                    {
                        "type":"image_url",
                        "image_url":{
                            "url":f"data:image/jpeg;base64,{base64_image}"
                            },
                    },
                ],
            },
        ],
    )
    assistant_message=response.choices[0].message.content
    st.write(assistant_message)

