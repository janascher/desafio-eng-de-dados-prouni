import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Contagem de beneficiários por raça/cor
count_race = df_prouni['RACA_BENEFICIARIO'].value_counts()

# Gráfico de barras da contagem de beneficiários por raça/cor
fig = px.bar(count_race, x=count_race.index, y=count_race.values,
             labels={'RACA_BENEFICIARIO': 'Raça/Cor'},
             title=f'Quantidade de Beneficiários por Raça/Cor')

# Renomear os eixos x e y
fig.update_layout(xaxis_title='Raça/Cor')
fig.update_layout(yaxis_title='Quantidade de Beneficiários')

# Exibir o gráfico
fig.show()