from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import get_filtered_items, get_top_scored_items

def create_top_picks(data: pd.DataFrame):
    filtered_data = get_filtered_items(data, "", "", [], [], [0, 200])
    top_items = get_top_scored_items(filtered_data)

    cols = ["Name", "Country", "Price", "Rating", "Score"]
    top_items = top_items[cols].head(100)
    return dbc.Row([
            html.H3("Our top picks", style={"color": "#2c3e50", "fontWeight": "bold"}),
            html.Hr(),
            dash_table.DataTable(
                id='top-picks-table',
                columns=[{"name": col, "id": col} for col in top_items.columns],
                data=top_items.to_dict('records'), # type: ignore
                row_selectable='single',
                style_table={
                    'overflowX': 'hidden',
                    'overflowY': 'scroll',
                    'height': '557px',
                    'border': '1px solid #dee2e6',
                    'borderRadius': '0.375rem',
                    'maxWidth': '100%',
                },
                style_header={
                    'backgroundColor': '#f8f9fa',
                    'fontWeight': 'bold',
                    'border': '1px solid #dee2e6',
                    'textAlign': 'left',
                    'padding': '0.75rem',
                    'fontSize': '14px',
                    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '0.75rem',
                    'border': '1px solid #dee2e6',
                    'fontSize': '14px',
                    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
                    'color': '#212529',
                    'whiteSpace': 'normal',
                    'overflow': 'hidden',
                    'textOverflow': 'normal',
                    'maxWidth': '200px'
                },
                style_data={
                    'backgroundColor': 'white',
                    'border': '1px solid #dee2e6',
                },
                style_data_conditional=[
                    {
                        'if': {'state': 'selected'},
                        'backgroundColor': 'white',  
                        'border': '1px solid #dee2e6',
                        'color': '#212529'
                    }
                ], # type: ignore
                virtualization=False,
                css=[{
                    'selector': '.dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner',
                    'rule': 'scroll-behavior: auto;'
                }]
            )
        ], className="bg-light border rounded m-2 p-3"
    )
