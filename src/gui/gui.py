import streamlit as st
import requests

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from src.settings import FASTAPI_PORT

st.set_page_config(layout='wide')

st.title("Ứng dụng tóm tắt tóm lược đơn văn bản",)

text_input = st.text_area("Nhập văn bản để tóm tắt tóm lược:", height=250)

response = None

col1, col2, col3 = st.columns((3, 8, 2))

with col1:
    level1 = st.radio("Lựa chọn ngôn ngữ", ["Tiếng Việt", "Tiếng Anh"], index=0)

with col2:

    if level1 == "Tiếng Việt":
        level2 = st.radio("Lựa chọn mô hình",
                          ["ntkhoi/mt5-vi-news-summarization", "ntkhoi/bart-vi-news-summarization"],
                          index=0)
    elif level1 == "Tiếng Anh":
        level2 = st.radio("Lựa chọn mô hình",
                          ["siddheshtv/abstractive_summarization", "facebook/bart-large-cnn"],
                          index=0)


if col3.button("Summary", use_container_width=True):
    response = requests.post(f"http://localhost:{FASTAPI_PORT}/summarization_text",
                             json={"text": text_input, "model": level2, "lang": level1})

if response:
    result = response.json()
else:
    result = {'summary': ""}

st.title("Kết quả")
st.write(f"{result['summary']}")
