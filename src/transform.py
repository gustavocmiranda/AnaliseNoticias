"""Transformação / Limpeza das notícias."""
import pandas as pd


def transforma_dicionario_em_dataframe(noticias: dict) -> pd.DataFrame:
    """Função que recebe as notícias em um dicionário e transforma em um dataframe."""
    for noticia in noticias:
        noticia["source_id"] = noticia["source"]["id"]
        noticia["source_name"] = noticia["source"]["name"]
        noticia.pop("source")

    df = pd.DataFrame(noticias)

    return df


def remove_linhas_nulas(df: pd.DataFrame) -> pd.DataFrame:
    """Função que remove linhas com indicação de 'removed'."""
    pass
