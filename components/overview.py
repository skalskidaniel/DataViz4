from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from data.loader import extract_item_value

def create_overview(selected_item: pd.Series, data: pd.DataFrame):
    
    df = data.copy()
    
    df["Score"] = (
        df["ABV"].astype(str).str.replace('%', '', regex=False).astype(float) * 10
        + df["Rating"].astype(float) * df["Rate Count"].astype(float)
        - df["Price"].astype(str).str.replace(r'[\$,]', '', regex=True).astype(float) * 2
    ).clip(lower=0).round()
    
    data_clean = df.dropna(subset=["Score"])
    
    selected_abv = pd.to_numeric(str(selected_item.get('ABV', 0)).replace('%', ''), errors='coerce') or 0
    selected_price = pd.to_numeric(str(selected_item.get('Price', 0)).replace('$', '').replace(',', ''), errors='coerce') or 0
    selected_rating = selected_item.get('Rating', 0) or 0
    selected_rate_count = selected_item.get('Rate Count', 0) or 0
    
    selected_score = max(selected_abv * 10 + selected_rating * selected_rate_count - selected_price * 2, 0)
    selected_name = selected_item.get('Name', 'Unknown')
    
    data_sorted = data_clean.sort_values('Score', ascending=True).reset_index(drop=True)
    
    data_sorted['Rank'] = range(1, len(data_sorted) + 1)
    
    selected_rank = None
    for idx, row in data_sorted.iterrows():
        if (abs(row['Score'] - selected_score) < 0.01 and 
            row.get('Name', '') == selected_name):
            selected_rank = row['Rank']
            break
        
    if selected_rank is None:
        score_diff = abs(data_sorted['Score'] - selected_score)
        closest_idx = score_diff.idxmin()
        selected_rank = data_sorted.loc[closest_idx, 'Rank']
    

    def format_value(value):
        if isinstance(value, list):
            return ', '.join(str(v) for v in value)
        return str(value)

    return dbc.Row([
        html.H3("Selected product overview"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H4("Name"),
                html.P(format_value(extract_item_value(selected_item, 'Name'))),
                html.H4("Type"),
                html.P(format_value(extract_item_value(selected_item, 'Type'))),
                html.H4("Price"),
                html.P(format_value(extract_item_value(selected_item, 'Price'))),
                html.H4("Brand"),
                html.P(format_value(extract_item_value(selected_item, 'Brand'))),
                html.H4("Country"),
                html.P(format_value(extract_item_value(selected_item, 'Country'))),
                html.H4("Ratings"),
                html.P(format_value(extract_item_value(selected_item, 'Rating'))),
                html.H4("Rate count"),
                html.P(format_value(extract_item_value(selected_item, 'Rate Count')))
            ]),
            
            dbc.Col([
                html.H4("Description"),
                html.P(format_value(extract_item_value(selected_item, 'Description'))),
                html.H4("Alcohol by Volume"),
                html.P(format_value(extract_item_value(selected_item, 'ABV'))),
                html.H4("Available volumes"),
                html.P(format_value(extract_item_value(selected_item, 'Volume'))),
                html.H4("Suggested serving temperature"),
                html.P(format_value(extract_item_value(selected_item, 'Suggested Serving Temperature'))),
                html.H4("Tasting notes"),
                html.P(format_value(extract_item_value(selected_item, 'Tasting Notes')))
            ]),
            
            dbc.Col([
                html.H4("Product Ranking"),
                html.P([
                    "Selected product score: ",
                    html.B(str(round(selected_score)))
                ]),
                html.P("Each dot represents a product. Your selection is highlighted in blue."),
                dcc.Graph(
                    id='score-ranking-plot',
                    figure={
                        'data': [
                            {
                                'x': data_sorted['Rank'],
                                'y': data_sorted['Score'],
                                'mode': 'markers',
                                'type': 'scatter',
                                'name': 'All Products',
                                'marker': {
                                    'color': '#6c757d',
                                    'size': 6,
                                    'opacity': 0.6
                                },
                                'hovertemplate': 'Name: %{text}<br>Rank: %{x}<br>Score: %{y}<extra></extra>',
                                'text': data_sorted.get('Name', '').fillna('Unknown') # type: ignore
                            },
                            {
                                'x': [selected_rank],
                                'y': [selected_score],
                                'mode': 'markers',
                                'type': 'scatter',
                                'name': 'Selected Product',
                                'marker': {
                                    'color': '#0dcaf0',
                                    'size': 12,
                                    'symbol': 'star',
                                    'line': {'color': '#fff', 'width': 2}
                                },
                                'hovertemplate': f'<b>SELECTED</b><br>Name: {selected_name}<br>Rank: %{{x}}<br>Score: %{{y}}<extra></extra>'
                            }
                        ],
                        'layout': {
                            'title': 'Product Score Ranking (Red Star = Your Selection)',
                            'xaxis': {'title': 'Rank (1 = Lowest Score)'},
                            'yaxis': {'title': 'Score'},
                            'plot_bgcolor': '#f8f9fa',
                            'paper_bgcolor': '#f8f9fa',
                            'margin': {'t': 60, 'b': 60, 'l': 60, 'r': 40},
                            'showlegend': False,
                            'hovermode': 'closest'
                        }
                    },
                    config={'displayModeBar': False})
            ])
        ])
    ], class_name="bg-light border rounded m-3 p-3")