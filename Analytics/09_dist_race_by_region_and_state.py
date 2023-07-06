import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def generate_race_distribution_chart(race):
    df_prouni = load_data()

    # Filtrar os beneficiários pela raça/cor selecionada
    df_race = df_prouni[df_prouni['RACA_BENEFICIARIO'] == race]

    # Análise da distribuição da raça/cor selecionada por região e UF
    dist_region_uf_race = df_race.groupby(['REGIAO_BENEFICIARIO', 'UF_BENEFICIARIO']).size().reset_index(name='Quantidade de Beneficiários')

    return dist_region_uf_race

#     # Gráfico de barras agrupadas da distribuição da raça/cor selecionada por região e UF
#     fig = px.bar(dist_region_uf_race, x='REGIAO_BENEFICIARIO', y='Quantidade de Beneficiários', color='UF_BENEFICIARIO', barmode='group',
#                 labels={'REGIAO_BENEFICIARIO': 'Região', 'Quantidade': 'Total', 'UF_BENEFICIARIO': 'UF dos Beneficiários'},
#                 title=f"Distribuição de Beneficiários por Região e UF (Raça/Cor: {race})")

#     # Exibir o gráfico
#     fig.show()

# generate_race_distribution_chart('Parda') #informar a raça/cor que deseja analisar
