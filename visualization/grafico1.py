import plotly.express as px

def gerar_grafico():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from Scripts.data_loader import load_data

    # Carregar os dados
    df_prouni = load_data()

    # Quantidade de beneficiários por sexo
    count_sex = df_prouni['SEXO_BENEFICIARIO'].value_counts()

    # Criar o gráfico
    fig = px.bar(count_sex, x=count_sex.index, y=count_sex.values,
                 labels={'y': 'Quantidade', 'SEXO_BENEFICIARIO': 'Sexo'},
                 title='Quantidade de Beneficiários por Sexo')

    # Renomear os eixos x e y
    fig.update_layout(xaxis_title='Sexo')
    fig.update_layout(yaxis_title='Quantidade de Beneficiários')

    return fig
