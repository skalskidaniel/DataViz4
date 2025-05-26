import kagglehub
import pandas as pd
import os
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc


# Data
dataset_path = kagglehub.dataset_download("limtis/wikiliq-dataset")

data_beer = pd.read_csv(os.path.join(dataset_path, "beer_data.csv"))
data_spirits = pd.read_csv(os.path.join(dataset_path, "spirits_data.csv"))
data_wine = pd.read_csv(os.path.join(dataset_path, "wine_data.csv"))

# App Settings
app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

beer_tab = dbc.Row(
    dash_table.DataTable(
        data=data_beer.to_dict('records'),
        columns=[{"name": i, "id": i} for i in data_beer.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'}
    )
)

wine_tab = dbc.Card(
    dbc.CardBody([
        html.P("This is beer tab!")
    ])
)

spirits_tab = dbc.Card(
    dbc.CardBody([
        html.P("This is beer tab!")
    ])
)

tabs = dbc.Tabs([
    dbc.Tab(beer_tab, label="Beer"),
    dbc.Tab(wine_tab, label="Wine"),
    dbc.Tab(spirits_tab, label="Spirits")
])


app.layout = dbc.Container([
    # Title row
    dbc.Row([
        dbc.Col(
            html.P(
                "Welcome to the alcohol dashboard!",
                className="display-4 text-center"
            ),
            width=12
        )
    ], className="mt-3 mb-4"),
    
    # Main content row with sidebar and visualization area
    dbc.Row([
        # Left sidebar for parameters/controls
        dbc.Col([
            html.H4("What do you like to drink?"),
            dcc.RadioItems(
                id='alcohol-type',
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                options=[
                    {'label': 'Beer', 'value': 'Beer'},
                    {'label': 'Wine', 'value': 'Wine'},
                    {'label': 'Spirits', 'value': 'Spirits'}
                ],
                value='Beer',
            ),
            
            html.P("Filter by country:"),
            dcc.Dropdown(
                id='country-filter',
                options=[{'label': c, 'value': c} for c in data_beer['Country'].unique()],
                multi=True
            ),
            html.P("Price range:", className="mt-3"),
            dcc.RangeSlider(
                id='price-range',
                min=0,
                max=100,
                step=5,
                marks={i: f"${i}" for i in range(0, 101, 20)},
                value=[0, 50]
            )
        ], width=3, className="bg-light p-3 border rounded"),
        
        # Main visualization area
        dbc.Col([
            tabs
        ], width=9)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run(debug=False)