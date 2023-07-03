import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import plotly.express as px
from Scripts.data_loader import load_data

df_prouni = load_data()

# Contagem de beneficiários por sexo
count_sex = df_prouni["SEXO_BENEFICIARIO"].value_counts()

# Gráfico de contagem de beneficiários por sexo
fig = px.bar(count_sex, x=count_sex.index, y=count_sex.values)

# Renomear os eixos x e y
fig.update_layout(xaxis_title="Sexo")
fig.update_layout(yaxis_title="Quantidade")

# Exibir o gráfico
fig.show()
