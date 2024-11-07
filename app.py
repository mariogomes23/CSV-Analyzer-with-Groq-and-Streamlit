import ollama
import streamlit as st



st.title("ollama!")
prompt = st.text_area(label="Qual a sua questão ? ")
button = st.button("Okay")
if button:
    if prompt:
        response = ollama.generate(model="gemma:2b",prompt=prompt)
        st.markdown(response["response"])