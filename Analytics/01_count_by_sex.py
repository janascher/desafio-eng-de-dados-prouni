import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Contagem de beneficiários por sexo
count_sex = df_prouni['SEXO_BENEFICIARIO'].value_counts()

# Gráfico de contagem de beneficiários por sexo
fig = px.bar(count_sex, x=count_sex.index, y=count_sex.values, 
             labels={'y': 'Quantidade','SEXO_BENEFICIARIO': 'Sexo'},
             title=f'Quantidade de Beneficiários por Sexo')

# Renomear os eixos x e y
fig.update_layout(xaxis_title='Sexo')
fig.update_layout(yaxis_title='Quantidade de Beneficiários')

# Exibir o gráfico
fig.show()
