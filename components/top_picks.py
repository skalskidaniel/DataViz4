from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import query_data

def create_top_picks(data: pd.DataFrame):
    q = query_data(data, "", [], [], [0, 200])
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            dbc.Table.from_dataframe(q, striped=True, bordered=True, hover=True, id='top-picks-table') # there is not really a problem, it works
            dash_table.DataTable(
                data=data.head(15).to_dict('records'),
                columns=[{"name": i, "id": i} for i in {"Name", "Type", "Price", "Country", "Rating"}],
                page_size=15,
                style_table={
                    'overflowX': 'auto',
                    'width': '100%',
                    'minWidth': '100%',
                },
                style_cell={
                    'textAlign': 'left',
                    'minWidth': '120px', 
                    'width': '120px',
                    'maxWidth': '200px',
                    'whiteSpace': 'normal'
                }
            )
        ], className="bg-light border rounded m-3 p-3"
    )