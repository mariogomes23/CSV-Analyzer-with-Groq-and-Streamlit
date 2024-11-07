import ollama
import streamlit as st



st.title("ollama!")
prompt = st.text_area(label="Qual a sua questão ? ")
button = st.button("Okay")
if button:
    if prompt:
        response = ollama.generate(model="llama3.1",prompt=prompt)
        st.markdown(response["response"])