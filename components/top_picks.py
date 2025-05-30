from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import get_filtered_items, get_top_scored_items

def create_top_picks(data: pd.DataFrame):
    filtered_data = get_filtered_items(data, "", "", [], [], [0, 200])
    top_items = get_top_scored_items(filtered_data)

    cols = ["Name", "Country", "Price", "Rating", "Score"]
    top_items = top_items[cols].head(13)
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            dbc.Table.from_dataframe(top_items, striped=False, bordered=True, hover=True, id='top-picks-table') # type: ignore
        ], className="bg-light border rounded m-3 p-3"
    )
