"""Coleta das notícias."""
from newsapi import NewsApiClient, const


def coleta_noticias(api_key: str, topic: str) -> dict:
    """
    Função que coleta as notícias com o tópico desejado.

    args:
    api_key(str): API Key da newsapi.org
    topic(str): tópico de interesse

    return: Dicionário com as notícias relacionadas ao tópico selecionado, se a conexão com a API foi bem sucedida
    """
    api = NewsApiClient(api_key=api_key)
    return api.get_everything(q=topic)["articles"]
