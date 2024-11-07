import os
import streamlit as st
from dotenv import load_dotenv
from groq_client import get_groq_client
from csv_handler import handle_csv_upload

def main():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        st.error("A chave de API da Groq não foi encontrada. Verifique o arquivo .env.")
        return

    client = get_groq_client(api_key)

    st.set_page_config(page_title="Analisar CSV")
    st.header("Analisar CSV")
    
    csv_file = st.file_uploader("Carregar ficheiro CSV", type="csv")
    if csv_file:
        handle_csv_upload(csv_file, client)

if __name__ == "__main__":
    main()
