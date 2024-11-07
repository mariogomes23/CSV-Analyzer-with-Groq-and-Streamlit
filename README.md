# 📊 CSV Analyzer with Groq and Streamlit

Bem-vindo ao **CSV Analyzer**, uma aplicação interativa desenvolvida com **Streamlit** e **Groq**. Este projeto permite carregar arquivos CSV e fazer perguntas sobre o conteúdo, com respostas geradas por modelos avançados de linguagem.

## 🚀 Funcionalidades

- **Carregamento de CSV**: Envie arquivos CSV para análise.
- **Análise de Dados com IA**: Use a API da Groq para perguntas e obtenha insights sobre os dados carregados.
- **Interface Amigável**: Interface intuitiva para carregar arquivos, fazer perguntas e visualizar respostas rapidamente.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal da aplicação.
- **Streamlit**: Framework para criar interfaces web interativas.
- **Groq API**: Para gerar respostas de IA com base em perguntas sobre o CSV carregado.
- **Docker** e **Docker Compose**: Facilita o deploy e execução do projeto.

## 📂 Estrutura de Arquivos

```plaintext
.
├── .env                        # Variáveis de ambiente, incluindo a chave da API Groq
├── app.py                      # Arquivo principal do Streamlit
├── csv_handler.py              # Módulo para manipulação de CSV
├── groq_client.py              # Cliente da API Groq
├── Dockerfile                  # Dockerfile para construir a imagem
├── docker-compose.yml          # Docker Compose para simplificar o deploy
└── requirements.txt            # Dependências do projeto
