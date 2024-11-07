from groq import Groq

def get_groq_client(api_key):
    """Cria e retorna um cliente Groq autenticado com a chave da API fornecida."""
    return Groq(api_key=api_key)
