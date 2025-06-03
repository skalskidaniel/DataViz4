from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

def create_top_picks(data: pd.DataFrame):
    cols = ["Name", "Country", "Price", "Rating", "Score"]
    top_items = data[cols].head(100)
    return dbc.Row([
            dash_table.DataTable(
                id='top-picks-table',
                columns=[{"name": col, "id": col} for col in top_items.columns],
                data=top_items.to_dict('records'), # type: ignore
                row_selectable='single',
                selected_rows=[],
                style_table={
                    'overflowX': 'hidden',
                    'overflowY': 'scroll',
                    'maxHeight': '700px',
                    'border': '1px solid #dee2e6',
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
        ]
    )
