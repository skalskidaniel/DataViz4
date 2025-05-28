from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

#TODO
def create_content_area(data: pd.DataFrame):
    return dbc.Col([
            html.P("There will be a table displayed", className='text-center fw-bold'),
            html.P("It will probably contain top 5 results with only few columns", className='text-center')
        ], className="bg-light border rounded m-3 p-3")