import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico():
    df_prouni = load_data()

    percentage_sex = df_prouni['SEXO_BENEFICIARIO'].value_counts(normalize=True) * 100

    fig = px.pie(percentage_sex, values=percentage_sex.values, names=percentage_sex.index,
                 labels={'values': 'Percentual', 'SEXO_BENEFICIARIO': 'Sexo'},
                 title='Distribuição Percentual de Beneficiários por Sexo')

    return fig

