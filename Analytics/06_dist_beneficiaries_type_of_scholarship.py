import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Distribuição de beneficiários por tipo de bolsa de estudos, sexo e raça
dist_type_scholarship_group = df_prouni.groupby(['TIPO_BOLSA', 'SEXO_BENEFICIARIO', 'RACA_BENEFICIARIO']).size().reset_index(name='COUNT')

# Gráfico de barras empilhadas
fig = px.bar(dist_type_scholarship_group, x='TIPO_BOLSA', y='COUNT', color='SEXO_BENEFICIARIO', barmode='stack',
             facet_col='RACA_BENEFICIARIO', 
             labels={'TIPO_BOLSA': 'Tipo de Bolsa', 'COUNT': 'Quantidade de Beneficiários', 'RACA_BENEFICIARIO': 'Raça/Cor', 'SEXO_BENEFICIARIO': 'Sexo'},
             title='Distribuição de Beneficiários por Tipo de Bolsa de Estudos, Sexo e Raça/Cor')

# Exibir o gráfico
fig.show()
