import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico():
    df_prouni = load_data()

    count_race = df_prouni['RACA_BENEFICIARIO'].value_counts()

    fig = px.bar(count_race, x=count_race.index, y=count_race.values,
                 labels={'RACA_BENEFICIARIO': 'Raça/Cor'},
                 title='Quantidade de Beneficiários por Raça/Cor')

    fig.update_layout(xaxis_title='Raça/Cor')
    fig.update_layout(yaxis_title='Quantidade de Beneficiários')

    return fig

