import os
import sys
import plotly.graph_objects as go

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico(nome_ies):
    df_prouni = load_data()

    df_filtered = df_prouni[df_prouni['NOME_IES_BOLSA'] == nome_ies]

    dist_sex = df_filtered['SEXO_BENEFICIARIO'].value_counts()
    dist_race = df_filtered['RACA_BENEFICIARIO'].value_counts()

    fig = go.Figure(data=[
        go.Bar(name='Masculino', x=dist_race.index, y=df_filtered[df_filtered['SEXO_BENEFICIARIO'] == 'M']['RACA_BENEFICIARIO'].value_counts()),
        go.Bar(name='Feminino', x=dist_race.index, y=df_filtered[df_filtered['SEXO_BENEFICIARIO'] == 'F']['RACA_BENEFICIARIO'].value_counts())
    ])

    fig.update_layout(barmode='stack', xaxis_title='Raça/Cor', yaxis_title='Quantidade de Beneficiários',
                      title='Distribuição de Beneficiários por Sexo e Raça/Cor - {}'.format(nome_ies))

    return fig


