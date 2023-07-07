import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico():
    df_prouni = load_data()

    dist_type_scholarship_group = df_prouni.groupby(['TIPO_BOLSA', 'SEXO_BENEFICIARIO', 'RACA_BENEFICIARIO']).size().reset_index(name='COUNT')

    fig = px.bar(dist_type_scholarship_group, x='TIPO_BOLSA', y='COUNT', color='SEXO_BENEFICIARIO', barmode='stack',
                 facet_col='RACA_BENEFICIARIO',
                 labels={'TIPO_BOLSA': 'Tipo de Bolsa', 'COUNT': 'Quantidade de Beneficiários', 'RACA_BENEFICIARIO': 'Raça/Cor', 'SEXO_BENEFICIARIO': 'Sexo'},
                 title='Distribuição de Beneficiários por Tipo de Bolsa de Estudos, Sexo e Raça/Cor')

    return fig


