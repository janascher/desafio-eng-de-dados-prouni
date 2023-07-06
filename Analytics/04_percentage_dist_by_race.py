import os
import sys
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

def generate_race_distribution_chart():
    df_prouni = load_data()

    # Distribuição percentual de beneficiários por raça/cor
    percentage_sex = df_prouni['RACA_BENEFICIARIO'].value_counts(normalize=True) * 100

    return percentage_sex

#     # Gráfico de distribuição percentual de beneficiários por sexo
#     fig = px.pie(percentage_sex, values=percentage_sex.values, names=percentage_sex.index,
#                 labels={'values': 'Percentual', 'RACA_BENEFICIARIO': 'Raça/Cor'}, 
#                 title=f'Distribuição Percentual de Beneficiários por Raça/Cor',)

#     # Exibir o gráfico
#     fig.show()

# generate_race_distribution_chart()