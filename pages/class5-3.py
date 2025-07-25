import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")

history=[
    {"role":"user", "content":"你好，AI"},
    {"role":"assistant", "content":"哈囉有啥需要幫忙的嗎"},
    {"role":"user", "content":"請問 st.chat_message()怎麼用"},
    {
        "role":"assistant", "content":"st.chat_message()可以讓你用聊天泡泡的方式顯示訊息喔"
    },
]


for message in history:
    if message["role"]=="user":
        st.chat_message("user",avatar="😀").write(message["content"])
    else:
        st.chat_message("assistant", avatar="😎").write(message["content"])

