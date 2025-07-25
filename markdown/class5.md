### Python AI 聊天程式與 Streamlit 互動筆記

這份筆記主要介紹如何用 Python 建立簡單的 AI 聊天程式，使用到 OpenAI 的 API 和 Streamlit 介面互動。

---

### 1. 簡單 AI 對話程式

首先需要安裝套件：

- OpenAI: `pip install openai`
- dotenv: `pip install python-dotenv`

設定 OpenAI 的 API 密鑰：

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("你:")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")
```

---

### 2. 具記憶功能的 AI 對話程式

在程式內加入記憶功能，使對話連續且有上下文：

```python
message = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

while True:
    user_input = input("你:")
    if user_input.lower() in ["exit", "quit"]:
        break

    message.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(model="gpt-4o-mini", messages=message)
    assistant_message = response.choices[0].message.content

    message.append({"role": "assistant", "content": assistant_message})
    print(f"AI: {assistant_message}")
```

---

### 3. Streamlit 基礎用法

Streamlit 能製作快速且互動式的網頁：

```python
import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")
```

也可以透過迴圈顯示聊天歷史記錄：

```python
history = [
    {"role": "user", "content": "你好，AI"},
    {"role": "assistant", "content": "哈囉有啥需要幫忙的嗎"},
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="😀").write(message["content"])
    else:
        st.chat_message("assistant", avatar="😎").write(message["content"])
```

---

### 4. Streamlit 結合 Session State

用 Session State 儲存使用者輸入，實現持續對話：

```python
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    st.chat_message("user", avatar='😶').write(message['content'])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
```

---

### 5. 結合 Streamlit 與 OpenAI

更進階的聊天互動範例：

```python
import streamlit as st
import openai

openai.api_key = st.secrets['OPENAI_API_KEY']

if "message" not in st.session_state:
    st.session_state.message = []

prompt = st.chat_input("請輸入訊息")

if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.message
    )
    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
```

---

### 6. AI 圖片分析

Streamlit 上傳圖片並使用 AI 分析：

```python
import streamlit as st
import base64
import openai

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpeg", "jpg"])

if uploaded_file:
    st.image(uploaded_file, width=300)
    base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")

prompt = st.chat_input("請輸入訊息")
if prompt:
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]}]
    )
    assistant_message = response.choices[0].message.content
    st.write(assistant_message)
```

---

### 7. AI 主持「海龜湯」遊戲

利用 AI 玩猜謎遊戲，玩家猜測後 AI 提供提示：

```python
# 加載題目和答案，並設定系統提示詞。
```

透過這些內容，能有效地理解 Python 結合 AI 進行互動開發的基礎方式，並應用到簡單的網頁或程式中。
