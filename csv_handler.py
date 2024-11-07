import pandas as pd
import streamlit as st
from io import StringIO

def handle_csv_upload(csv_file, client):
    try:
        # Carregar o CSV
        csv_data = pd.read_csv(csv_file, on_bad_lines='skip') 
        st.write("Conteúdo carregado do CSV:")
        st.write(csv_data.head())

        # Converter o CSV para um formato que o Groq possa analisar
        csv_buffer = StringIO()
        csv_data.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Entrada do usuário
        user_question = st.text_input("Qual a sua questão relacionada ao csv carregado?")
        if user_question:
            st.write(f"Sua questão: {user_question}")
            with st.spinner(text="Analisando...relaxa"):
                try:
                    # Preparar o conteúdo para a análise
                    content_to_analyze = f"Aqui está o CSV carregado: \n{csv_data.head().to_string()} \n\nAgora, responda à pergunta abaixo:\n{user_question}"

                    # Chamar a API Groq para obter a resposta
                    response = analyze_with_groq(client, content_to_analyze)
                    st.write(response)

                except Exception as e:
                    st.error(f"Erro ao processar a pergunta com a API Groq: {e}")
                    
    except pd.errors.ParserError as e:
        st.error(f"Erro ao processar o CSV: {e}")
    except Exception as e:
        st.error(f"Erro desconhecido ao processar o arquivo CSV: {e}")

def analyze_with_groq(client, content_to_analyze):
    """Chama a API Groq para obter uma resposta com base no conteúdo analisado"""
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": content_to_analyze
        }],
        model="llama3-8b-8192", 
    )
    return chat_completion.choices[0].message.content
