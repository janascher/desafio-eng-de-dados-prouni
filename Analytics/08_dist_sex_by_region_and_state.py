import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Interface para seleção do sexo
sexo = input("Informe o sexo que deseja analisar (M/F): ")

# Filtrar os beneficiários pelo sexo selecionado
df_sexo = df_prouni[df_prouni['SEXO_BENEFICIARIO'] == sexo]

# Análise da distribuição do sexo selecionado por região e UF
dist_regiao_uf_sexo = df_sexo.groupby(['REGIAO_BENEFICIARIO', 'UF_BENEFICIARIO']).size().reset_index(name='Quantidade de Beneficiários')

# Gráfico de distribuição do sexo do beneficiário selecionado por região e UF
fig = px.bar(dist_regiao_uf_sexo, x='REGIAO_BENEFICIARIO', y='Quantidade de Beneficiários', color='UF_BENEFICIARIO', barmode="group", 
             labels={"x": "Região", "y": "Total", 'REGIAO_BENEFICIARIO': 'Região do Beneficiário', 'UF_BENEFICIARIO': 'UF dos Beneficiários'},)
fig.update_layout(title=f"Distribuição de Beneficiários por Região e UF (Sexo: {sexo})")

# Exibir o gráfico
fig.show()
