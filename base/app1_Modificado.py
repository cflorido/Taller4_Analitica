# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# python app1.py
# y luego visite el sitio 
# http://127.0.0.1:8050/ 
# en su navegador.

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
df = pd.DataFrame({
    "Carreras": ["Ing Industrial", "Ing Sistemas", "Ing Mecanica", "Ing Civil", "Ing Industrial", "Ing Sistemas", "Ing Mecanica", "Ing Civil"],
    "Cantidad": [100, 75, 102, 126, 150, 240, 178, 250],
    "Sexo": ["Mujeres", "Mujeres","Mujeres","Mujeres","Hombres", "Hombres","Hombres","Hombres"]
})

colors    = ['rgb(255,192,203)','rgb(160,206,222)']

fig = px.bar(df, x="Carreras", y="Cantidad", color="Sexo", barmode="group", color_discrete_sequence=colors)

app.layout = html.Div(children=[
    html.H1(children='Mujeres en Ingenieria'),

    html.Div(children='''
        Histograma de cantidad de estudiantes de ingenieria divididos por sexo
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        En este gráfico se observa el número de estudiantes de ingenieria divididos entre hombres y mujeres.
    '''),
    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
        ],
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
