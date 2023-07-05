import pandas as pd


def load_data():
    # Caminho do arquivo
    path_data_curated = "./Data/curated/dados_prouni2020_tratados.csv"

    # Carregar os dados
    df_prouni = pd.read_csv(path_data_curated)
    return df_prouni
