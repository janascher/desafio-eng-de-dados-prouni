import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico():
    df_prouni = load_data()

    percentage_race = df_prouni['RACA_BENEFICIARIO'].value_counts(normalize=True) * 100

    fig = px.pie(percentage_race, values=percentage_race.values, names=percentage_race.index,
                 labels={'values': 'Percentual', 'RACA_BENEFICIARIO': 'Raça/Cor'},
                 title='Distribuição Percentual de Beneficiários por Raça/Cor')

    return fig



