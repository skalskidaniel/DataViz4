from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

#TODO
def create_top_picks(data: pd.DataFrame):
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            html.P("There will be a table displayed", className='text-center fw-bold fst-italic'),
            html.P("It will probably contain top 5 results with only few columns", className='text-center fst-italic')
        ], className="bg-light border rounded m-3 p-3")