import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def visualize_beneficiarios_por_sexo(sex):
    df_prouni = load_data()

    # Filtrar os beneficiários pelo sexo selecionado
    df_sex = df_prouni[df_prouni['SEXO_BENEFICIARIO'] == sex]

    # Análise da distribuição do sexo selecionado por região e UF
    dist_region_uf_sex = df_sex.groupby(['REGIAO_BENEFICIARIO', 'UF_BENEFICIARIO']).size().reset_index(name='Quantidade de Beneficiários')

    return dist_region_uf_sex

#     # Gráfico de distribuição do sexo do beneficiário selecionado por região e UF
#     fig = px.bar(dist_region_uf_sex, x='REGIAO_BENEFICIARIO', y='Quantidade de Beneficiários', color='UF_BENEFICIARIO', barmode="group", 
#                 labels={"x": "Região", "y": "Total", 'REGIAO_BENEFICIARIO': 'Região do Beneficiário', 'UF_BENEFICIARIO': 'UF dos Beneficiários'},)
#     fig.update_layout(title=f"Distribuição de Beneficiários por Região e UF (Sexo: {sex})")

#     # Exibir o gráfico
#     fig.show()

# visualize_beneficiarios_por_sexo('F') #informar  sexo que deseja analisar (M/F)