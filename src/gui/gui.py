import streamlit as st 
import requests 
st.set_page_config(layout='wide')

st.title("Abstractive Summarization Web Application",) 

text_input = st.text_area("Enter text for summarization:",height=250) 

response = None

col1, col2 , col3 = st.columns((2,10,1))

with col1:
    model_selection = st.radio(
        "Lựa chọn mô hình",
        ["Mô hình T5", "Mô hình BART",] ,
        index=0,
    )

with col2 :
    lang_selection = st.radio(
        "Lựa chọn ngôn ngữ",
        ["Tiếng Việt",
         "Tiếng Anh"],
         index=0
    )

if col3.button("Summary"): 
    response = requests.post("http://localhost:8000/summarization_text", json={"text": text_input,  "model":model_selection, "lang":lang_selection }) 

if response:
    result = response.json() 
else :
    result = {'summary':""}

st.title("Kết quả") 
st.write(f"{result['summary']}") 