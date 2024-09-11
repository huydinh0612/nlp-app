import streamlit as st
import requests

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from src.settings import FASTAPI_PORT

st.set_page_config(layout='wide')

st.title("Ứng dụng tóm tắt tóm lược đơn văn bản",)

input_type = st.radio("Lựa chọn kiểu đầu vào", ["Nhập trực tiếp", "Tải file lên"], index=0)
if input_type == "Nhập trực tiếp":
    input = st.text_area("Nhập văn bản để tóm tắt tóm lược:", height=250)
elif input_type == "Tải file lên":
    input = st.file_uploader("Chọn tệp văn bản để tải lên", type=["txt", "pdf", "docx", 'doc'])
    if input:
        file_type = input.name.split(".")[-1]
        if file_type == 'txt':
            input = input.read().decode("utf-8")
            st.write(input)
    else:
        st.write("Chưa chọn file nào")
        # doc = Document(uploaded_file)
        # text_input = "\n".join([para.text for para in doc.paragraphs])


response = None

col1, col2, col3 = st.columns((3, 8, 2))

with col1:
    level1 = st.radio("Lựa chọn ngôn ngữ", ["Tiếng Việt", "Tiếng Anh"], index=0)

with col2:
    level2 = st.radio("Lựa chọn mô hình",
                        ["Mô hình T5", "Mô hình BART"],
                        index=0)



if col3.button("Summary", use_container_width=True):
    response = requests.post(f"http://localhost:{FASTAPI_PORT}/summarization_text",
                             json={"text": input, "model": level2, "lang": level1})

if response:
    result = response.json()
else:
    result = {'summary': ""}

st.title("Kết quả")
st.write(f"{result['summary']}")
