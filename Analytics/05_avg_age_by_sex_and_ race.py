import os
import sys
import pandas as pd
import plotly.express as px

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Scripts.data_loader import load_data

df_prouni = load_data()

# Converta a coluna 'DATA_NASCIMENTO' em um formato datetime para executar cálculos com base em datas 
df_prouni['DATA_NASCIMENTO'] = pd.to_datetime(df_prouni['DATA_NASCIMENTO'], format='%d/%m/%Y')

# Calcula a idade de cada beneficiário com base na sua data de nascimento, ou seja, subtrai a coluna 'DATA_NASCIMENTO' da data atual e divide o resultado pelo número de dias em um ano para obter a idade em anos.
df_prouni['IDADE'] = (pd.Timestamp('now') - df_prouni['DATA_NASCIMENTO']) / pd.Timedelta(days=365.25)

# Média de idade dos beneficiários por sexo e raça/cor
average_age = df_prouni.groupby(['SEXO_BENEFICIARIO', 'RACA_BENEFICIARIO'])['IDADE'].mean().reset_index()

# Renomear a coluna 'IDADE' para 'Média de Idade'
average_age = average_age.rename(columns={'IDADE': 'MEDIA_DE_IDADE'})

# Arredonda o valor da média de idade para duas casas decimais
average_age['MEDIA_DE_IDADE'] = average_age['MEDIA_DE_IDADE'].apply(lambda x: round(x, 2))

# Adiciona o símbolo '%' ao final do valor formatado
average_age['MEDIA_DE_IDADE'] = average_age['MEDIA_DE_IDADE'].astype(str) + '%'

# Gráfico de dispersão da média de idade dos beneficiários por sexo e raça/cor
fig = px.scatter(average_age, x='RACA_BENEFICIARIO', y='MEDIA_DE_IDADE', color='SEXO_BENEFICIARIO', 
                 labels={'RACA_BENEFICIARIO': 'Raça/Cor', 'SEXO_BENEFICIARIO': 'Sexo', 'MEDIA_DE_IDADE': 'Média de Idade'}, 
                 title=f'Média de Idade dos Beneficiários por Sexo e Raça/cor')

fig.update_traces(marker=dict(size=20))

# Exibir o gráfico
fig.show()
