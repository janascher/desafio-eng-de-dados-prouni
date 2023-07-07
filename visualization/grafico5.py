import os
import sys
import pandas as pd
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico():
    df_prouni = load_data()

    df_prouni['DATA_NASCIMENTO'] = pd.to_datetime(df_prouni['DATA_NASCIMENTO'], format='%d/%m/%Y')
    df_prouni['IDADE'] = (pd.Timestamp('now') - df_prouni['DATA_NASCIMENTO']) / pd.Timedelta(days=365.25)

    average_age = df_prouni.groupby(['SEXO_BENEFICIARIO', 'RACA_BENEFICIARIO'])['IDADE'].mean().reset_index()
    average_age = average_age.rename(columns={'IDADE': 'MEDIA_DE_IDADE'})
    average_age['MEDIA_DE_IDADE'] = average_age['MEDIA_DE_IDADE'].apply(lambda x: round(x, 2))
    average_age['MEDIA_DE_IDADE'] = average_age['MEDIA_DE_IDADE'].astype(str) + '%'

    fig = px.scatter(average_age, x='RACA_BENEFICIARIO', y='MEDIA_DE_IDADE', color='SEXO_BENEFICIARIO',
                     labels={'RACA_BENEFICIARIO': 'Raça/Cor', 'SEXO_BENEFICIARIO': 'Sexo', 'MEDIA_DE_IDADE': 'Média de Idade'},
                     title='Média de Idade dos Beneficiários por Sexo e Raça/Cor')

    fig.update_traces(marker=dict(size=20))

    return fig


