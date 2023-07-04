import os
import sys
import plotly.graph_objects as go #TODO Substituir para Dash?

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Filtrar dados para uma instituição de ensino específica
# nome_ies = 'Nome da Instituição'  # Substitua pelo nome da instituição desejada
nome_ies = 'FACULDADE DE QUIXERAMOBIM'
df_filtered = df_prouni[df_prouni['NOME_IES_BOLSA'] == nome_ies]

# Distribuição de beneficiários por sexo na instituição de ensino filtrada
dist_sexo = df_filtered['SEXO_BENEFICIARIO'].value_counts()

# Distribuição de beneficiários por raça/cor na instituição de ensino filtrada
dist_raca_cor = df_filtered['RACA_BENEFICIARIO'].value_counts()

# Gráfico de barras empilhadas para a distribuição de beneficiários por sexo e raça/cor
fig = go.Figure(data=[
    go.Bar(name='Masculino', x=dist_raca_cor.index, y=df_filtered[df_filtered['SEXO_BENEFICIARIO'] == 'M']['RACA_BENEFICIARIO'].value_counts()),
    go.Bar(name='Feminino', x=dist_raca_cor.index, y=df_filtered[df_filtered['SEXO_BENEFICIARIO'] == 'F']['RACA_BENEFICIARIO'].value_counts())
])

fig.update_layout(barmode='stack', xaxis_title='Raça/Cor', yaxis_title='Quantidade de Beneficiários', title='Distribuição de Beneficiários por Sexo e Raça/Cor - {institution}')

# Exibir o gráfico
fig.show()
