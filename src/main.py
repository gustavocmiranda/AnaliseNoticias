"""Chamada do pipeline."""
import pandas as pd
from dotenv import dotenv_values

from extract import coleta_noticias
from transform import remove_linhas_nulas, transforma_dicionario_em_dataframe

config = dotenv_values(".env")

news = coleta_noticias(api_key=config["API_KEY"], topic="iphone")
df = transforma_dicionario_em_dataframe(news)
df = remove_linhas_nulas(df)

print(df.head())
