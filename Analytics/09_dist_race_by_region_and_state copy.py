import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Interface para seleção da raça/cor
raca = input("Informe a raça/cor que deseja analisar: ")

# Filtrar os beneficiários pela raça/cor selecionada
df_raca = df_prouni[df_prouni['RACA_BENEFICIARIO'] == raca]

# Análise da distribuição da raça/cor selecionada por região e UF
dist_regiao_uf_raca = df_raca.groupby(['REGIAO_BENEFICIARIO', 'UF_BENEFICIARIO']).size().reset_index(name='Quantidade de Beneficiários')

# Gráfico de barras agrupadas da distribuição da raça/cor selecionada por região e UF
fig = px.bar(dist_regiao_uf_raca, x='REGIAO_BENEFICIARIO', y='Quantidade de Beneficiários', color='UF_BENEFICIARIO', barmode='group',
             labels={'REGIAO_BENEFICIARIO': 'Região', 'Quantidade': 'Total', 'UF_BENEFICIARIO': 'UF dos Beneficiários'},
             title=f"Distribuição de Beneficiários por Região e UF (Raça/Cor: {raca})")

# Exibir o gráfico
fig.show()
