from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import get_filtered_items, get_top_scored_items

def create_top_picks(data: pd.DataFrame):
    filtered_data = get_filtered_items(data, "", "", [], [], [0, 200])
    top_items = get_top_scored_items(filtered_data)

    cols = ["Name", "Country", "Price", "Rating", "Score"]
    top_items = top_items[cols].head(100)
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            dash_table.DataTable(
                id='top-picks-table',
                columns=[{"name": col, "id": col} for col in top_items.columns],
                data=top_items.to_dict('records'), # type: ignore
                row_selectable='single',
                style_table={
                    'overflowX': 'hidden',
                    'overflowY': 'scroll',
                    'height': '550px',
                    'maxHeight': '550px',
                    'border': '1px solid #dee2e6',
                    'borderRadius': '0.375rem',
                    'maxWidth': '100%',
                    'width': '100%',
                    'tableLayout': 'fixed'
                },
                style_header={
                    'backgroundColor': '#f8f9fa',
                    'fontWeight': 'bold',
                    'border': '1px solid #dee2e6',
                    'textAlign': 'left',
                    'padding': '0.75rem',
                    'fontSize': '14px',
                    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
                    'position': 'sticky'
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
                fixed_rows={'headers': True},
                virtualization=False,
                css=[{
                    'selector': '.dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner',
                    'rule': 'scroll-behavior: smooth;' # 'auto' is often better than 'smooth' for virtualized tables
                }]
            )
        ], className="bg-light border rounded m-3 p-3"
    )
