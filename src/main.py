"""Chamada do pipeline."""
from dotenv import dotenv_values

from extract import coleta_noticias
from transform import transforma_dicionario_em_dataframe

config = dotenv_values(".env")

news = coleta_noticias(api_key=config["API_KEY"], topic="iphone")
df = transforma_dicionario_em_dataframe(news)

print(df)
