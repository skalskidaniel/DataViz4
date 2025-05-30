from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import get_filtered_items

def create_top_picks(data: pd.DataFrame):
    q = get_filtered_items(data, "", [], [], [0, 200])[0]
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            dbc.Table.from_dataframe(q, striped=False, bordered=True, hover=True, id='top-picks-table') # type: ignore
        ], className="bg-light border rounded m-3 p-3"
    )
