import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Distribuição percentual de beneficiários por sexo
percentage_sex = df_prouni['SEXO_BENEFICIARIO'].value_counts(normalize=True) * 100

# Gráfico de distribuição percentual de beneficiários por sexo
fig = px.pie(percentage_sex, values=percentage_sex.values, names=percentage_sex.index, 
             labels={'values': 'Percentual', 'SEXO_BENEFICIARIO': 'Sexo'}, 
             title=f'Distribuição Percentual de Beneficiários por Sexo')

# Exibir o gráfico
fig.show()
