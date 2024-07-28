import pandas as pd

def get_data(path):
    """
    Lê os dados de um arquivo CSV e retorna um DataFrame.

    Parâmetros:
    path (str): O caminho para o arquivo CSV que contém os dados.

    Retorna:
    pd.DataFrame: Um DataFrame contendo os dados do arquivo CSV.
    """
    # Lê os dados do arquivo CSV especificado no caminho 'path'
    df = pd.read_csv(path)

    # Retorna o DataFrame contendo os dados lidos
    return df
