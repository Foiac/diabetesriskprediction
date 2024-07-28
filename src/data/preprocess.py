import numpy as np

def process_data(df):
    """
    Processa um DataFrame para tratar valores zero em colunas específicas e substituir por NaN,
    seguido pelo preenchimento desses valores faltantes com a média da coluna.

    Parâmetros:
    df (pd.DataFrame): O DataFrame contendo os dados a serem processados.

    Retorna:
    pd.DataFrame: O DataFrame processado com valores zero substituídos por NaN e valores faltantes
                  preenchidos com a média da coluna.
    """
    # Lista de colunas para substituir valores "0" por valores NaN
    columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    # Substitui 0 por np.nan nas colunas especificadas
    df[columns] = df[columns].replace(0, np.nan)

    # Itera por cada coluna e preenche valores faltantes com a média da coluna
    df.fillna({col: df[col].mean() for col in columns}, inplace=True)

    return df
