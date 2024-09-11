import streamlit as st
import requests

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from src.settings import FASTAPI_PORT
from src.features.process_file import read_text, read_pdf, read_doc

st.set_page_config(layout='wide')

st.title("Ứng dụng tóm tắt tóm lược đơn văn bản",)

input_type = st.radio("Lựa chọn kiểu đầu vào", ["Nhập trực tiếp", "Tải file lên"], index=0)

# Input text
if input_type == "Nhập trực tiếp":
    text_content = st.text_area("Nhập văn bản để tóm tắt tóm lược:", height=250)
# Input file 
elif input_type == "Tải file lên":
    upload_file = st.file_uploader("Chọn tệp văn bản để tải lên", type=["txt", "pdf", "docx", "doc"])
    if upload_file:
        file_type = upload_file.name.split(".")[-1]
        # Read txt file
        if file_type == 'txt':
            text_file = read_text(upload_file)
        # Read pdf file 
        elif file_type == 'pdf':
            text_file = read_pdf(upload_file)
        # Read docx, doc file 
        elif 'doc' in file_type:
            text_file = read_doc(upload_file)
        # Get text content to send to API
        text_content = text_file
    else:
        st.write("Chưa chọn file nào")


response = None


col1, col2, col3 = st.columns((3, 8, 2))

with col1:
    language = st.radio("Lựa chọn ngôn ngữ", ["Tiếng Việt", "Tiếng Anh"], index=0)

with col2:
    model_type = st.radio("Lựa chọn mô hình",
                        ["Mô hình T5", "Mô hình BART"],
                        index=0)



if col3.button("Tóm tắt", use_container_width=True):

        
    response = requests.post(f"http://localhost:{FASTAPI_PORT}/summarization_text",
                             json={"text": text_content, 
                                   "model": model_type, 
                                   "lang": language,
                                   })

if response:
    result = response.json()
else:
    result = {'summary': ""}

st.title("Kết quả")
st.write(f"{result['summary']}")
