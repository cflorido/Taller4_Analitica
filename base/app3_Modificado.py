import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


# -*- coding: utf-8 -*-
import pycountry

cc={}

t = list(pycountry.countries)

for country in t:
    cc[country.name]=country.alpha_2

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

country_iso = {
    'China': 'CHN',            
    'United States': 'USA',    
    'Russia': 'RUS',          
    'Japan': 'JPN',           
    'Germany': 'DEU',          
    'United Kingdom': 'GBR',  
    'India': 'IND',           
    'France': 'FRA',          
    'Italy': 'ITA',           
    'Canada': 'CAN',           
    'South Korea': 'KOR'       
}


df['iso_alpha'] = df['country'].map(country_iso)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    
    fig = px.choropleth(filtered_df, locations="iso_alpha",
                        color="lifeExp", hover_name="country",
                        range_color=[20, 80],
                        labels={"lifeExp": "Life Expectancy"},
                        title=f"Expectativa de vida en {selected_year} para las potencias mundiales actuales")

    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
