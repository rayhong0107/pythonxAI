import streamlit as st
import os

file_path="markdown"
files=os.listdir(file_path)
for f in files:
    if f.endswith('.md'):
        with open(f"{file_path}/{f}", "r", encoding="utf-8") as file:
            content=file.read()
        with st.expander(f[:-3] + " 課堂筆記"):
            st.write(content)