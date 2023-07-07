import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def gerar_grafico(race):
    df_prouni = load_data()

    df_race = df_prouni[df_prouni['RACA_BENEFICIARIO'] == race]

    dist_region_uf_race = df_race.groupby(['REGIAO_BENEFICIARIO', 'UF_BENEFICIARIO']).size().reset_index(name='Quantidade de Beneficiários')

    fig = px.bar(dist_region_uf_race, x='REGIAO_BENEFICIARIO', y='Quantidade de Beneficiários', color='UF_BENEFICIARIO', barmode='group',
                 labels={'REGIAO_BENEFICIARIO': 'Região', 'Quantidade de Beneficiários': 'Total', 'UF_BENEFICIARIO': 'UF dos Beneficiários'},
                 title=f"Distribuição de Beneficiários por Região e UF (Raça/Cor: {race})")

    return fig

