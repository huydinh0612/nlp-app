import streamlit as st 
import requests 
st.set_page_config(layout='wide')

st.title("Abstractive Summarization Web Application",) 

text_input = st.text_area("Enter text for summarization:",height=250) 

response = None

col1, col2 , col3 = st.columns((2,10,1))

with col1:
    model_selected = st.radio(
        "Choose a summarizer",
        ["Model 1", "Model 2",] ,
        index=0,
    )

with col2 :
    prompt_selected = st.radio(
        "Choose a prompt technique",
        ["Zero-shot summary",
         "One-shot summary"],
         index=0
    )

if col3.button("Summary"): 
    response = requests.post("http://localhost:8000/summarization_text", json={"text": text_input,  "model":model_selected, "prompt":prompt_selected }) 

if response:
    result = response.json() 
else :
    result = {'summary':""}
st.write(f"{result['summary']}") 