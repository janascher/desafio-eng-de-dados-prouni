import dash
import sys
import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from grafico1 import gerar_grafico as grafico1
from grafico2 import gerar_grafico as grafico2
from grafico3 import gerar_grafico as grafico3
from grafico4 import gerar_grafico as grafico4
from grafico5 import gerar_grafico as grafico5
from grafico6 import gerar_grafico as grafico6
from grafico7 import gerar_grafico as grafico7
from grafico8 import gerar_grafico as grafico8
from grafico9 import gerar_grafico as grafico9
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Criar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Gráficos"),
    
    
    dcc.Graph(
        id='grafico-1',
        figure=grafico1()
    ),
    dcc.Graph(
        id='grafico-2',
        figure=grafico2()
    ),
    dcc.Graph(
        id='grafico-3',
        figure=grafico3()
    ),
    dcc.Graph(
        id='grafico-4',
        figure=grafico4()
    ),
    dcc.Graph(
        id='grafico-5',
        figure=grafico5()
    ),
    dcc.Graph(
        id='grafico-6',
        figure=grafico6()
    ),
    dcc.Graph(
        id='grafico-7',
        figure=grafico7('UNIVERSIDADE PAULISTA')
    ),
    html.Div([
        dcc.Dropdown(
            id='select-sexo',
            options=[
                {'label': 'Masculino', 'value': 'M'},
                {'label': 'Feminino', 'value': 'F'}
            ],
            value='',
            placeholder='Selecione o sexo'
        ),
        dcc.Graph(id='grafico-8')
    ]),
    
    html.Div([
        dcc.Dropdown(
            id='select-etnia',
            options=[
                {'label': 'Branca', 'value': 'Branca'},
                {'label': 'Parda', 'value': 'Parda'},
                {'label': 'Preta', 'value': 'Preta'},
                {'label': 'Amarela', 'value': 'Amarela'},
                {'label': 'Indigena', 'value': 'Indï¿½gena'}
            ],
            value='',
            placeholder='Selecione a etnia'
        ),
        dcc.Graph(id='grafico-9')
    ])
    
])

# Callback para atualizar o gráfico-8 com base na seleção do dropdown de sexo
@app.callback(
    Output('grafico-8', 'figure'),
    [Input('select-sexo', 'value')]
)
def atualizar_grafico8(sexo):
    figura = grafico8(sexo)  # Lógica para gerar o gráfico-8 com base na seleção do dropdown de sexo
    return figura

# Callback para atualizar o gráfico-9 com base na seleção do dropdown de etnia
@app.callback(
    Output('grafico-9', 'figure'),
    [Input('select-etnia', 'value')]
)
def atualizar_grafico9(etnia):
    figura = grafico9(etnia)  # Lógica para gerar o gráfico-9 com base na seleção do dropdown de etnia
    return figura

# Executar a aplicação Dash
if __name__ == '__main__':
    app.run_server(debug=True)
