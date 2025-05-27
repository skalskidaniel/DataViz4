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

taste_beer = list({t.strip() for notes in data_beer['Tasting Notes'] for t in str(notes).split(',') if pd.notnull(notes)})
taste_spirits = list({t.strip() for notes in data_spirits['Tasting Notes'] for t in str(notes).split(',') if pd.notnull(notes)})
taste_wine = list({t.strip() for notes in data_wine['Tasting Notes'] for t in str(notes).split(',') if pd.notnull(notes)})

food_wine = list({f.strip() for food in data_wine['Food Pairing'] for f in str(food).split(',') if pd.notnull(food)})

categories_beer = list({t.strip() for type in data_beer['Categories'] for t in str(type).split(',') if pd.notnull(type)})
categories_spirits = list({t.strip() for type in data_spirits['Categories'] for t in str(type).split(',') if pd.notnull(type)})
categories_wine = list({t.strip() for type in data_wine['Categories'] for t in str(type).split(',') if pd.notnull(type)})


# App Settings
app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # Title row
    dbc.Row([
        dbc.Col([
            html.H1(
                "Welcome to the alcohol dashboard!",
                className="display-4 text-center"
            ),
            html.P(
                "The dashboard has been designed to help you find a proper drink for yourself",
                className="text-center"
            )
        ], width=12)
    ], className="mt-3 mb-4"),
    
    # Main content row with sidebar and visualization area
    dbc.Row([
        # Left sidebar for parameters/controls
        dbc.Col([
            html.H3("Adjust your preferences", className="mt-3 mb-3"),
            html.H4("Drink type", className="mt-3 mb-3"),
            dbc.RadioItems(
                id='type',
                options=[
                    {'label': '\u00A0\u00A0Beer', 'value': 'Beer'},
                    {'label': '\u00A0\u00A0Wine', 'value': 'Wine'},
                    {'label': '\u00A0\u00A0Spirits', 'value': 'Spirits'}
                ],
                value='Beer',
                labelStyle={'display': 'block', 'marginBottom': '8px', 'paddingLeft': '4px'},
                className="mt-3 mb-3"
            ),
            
            html.H4("Category", className="mt-3 mb-3"),
            dcc.Dropdown(
               id='category',
               options=[{'label': c, 'value': c} for c in categories_beer], #TODO not only beer
               className="mt-3 mb-3",
            ),
            
            html.H4("Tasting Notes", className="mt-3 mb-3"),
            dcc.Dropdown(
                id='taste-filter',
                options=[{'label': c, 'value': c} for c in taste_wine], #TODO only visible if wine is chosen
                multi=True,
                className="mt-3 mb-3"
            ),
            
            html.H4("Food Pairing", className="mt-3 mb-3"), #TODO show only when wine is chosen
            dcc.Dropdown(
                id='food_filter',
                options=[{'label': c, 'value': c} for c in food_wine],
                multi=True,
                className="mt-3 mb-3"
            ),
            
            html.H4("Price range (per liter)"),
            dcc.RangeSlider(
                id='price-range',
                min=0,
                max=100,
                step=5,
                marks={i: f"${i}" for i in range(0, 101, 20)},
                value=[0, 50],
                className="mt-3 mb-1"
            )
        ], width=3, className="bg-light p-3 border rounded"),
        
        # Main visualization area
        dbc.Col([
            dbc.Card()
        ], width=9)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run(debug=False)