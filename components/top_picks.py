from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import get_filtered_items, get_top_scored_items

def create_top_picks(data: pd.DataFrame):
    filtered_data = get_filtered_items(data, "", "", [], [], [0, 200])
    top_items = get_top_scored_items(filtered_data)

    cols = ["Name", "Country", "Price", "Rating", "Score"]
    top_items = top_items[cols].head(12)
    return dbc.Col([
            html.H3("Our top picks"),
            html.Hr(),
            dash_table.DataTable(
                id='top-picks-table',
                columns=[{"name": col, "id": col} for col in top_items.columns],
                data=top_items.to_dict('records'), # type: ignore
                row_selectable='single',
                style_table={
                    'overflowX': 'auto',
                    'border': '1px solid #dee2e6',
                    'borderRadius': '0.375rem',
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
                    'color': '#212529'
                },
                style_data={
                    'backgroundColor': 'white',
                    'border': '1px solid #dee2e6',
                },
                css=[
                    {
                        'selector': '.dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner table',
                        'rule': 'border-collapse: separate; border-spacing: 0;'
                    },
                    {
                        'selector': '.dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner tr:hover',
                        'rule': 'background-color: #f5f5f5 !important;'
                    }
                ]
            )
        ], className="bg-light border rounded m-3 p-3"
    )
