from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objects as go # Import go
from scipy.stats import percentileofscore # Import percentileofscore
from data.loader import extract_item_value

def create_overview(selected_item: pd.Series, data: pd.DataFrame):
    
    df = data.copy()
    
    df["Score"] = (
        df["ABV"].astype(str).str.replace('%', '', regex=False).astype(float) * 10
        + df["Rating"].astype(float) * df["Rate Count"].astype(float)
        - df["Price"].astype(str).str.replace(r'[\$,]', '', regex=True).astype(float) * 2
    ).clip(lower=0).round()
    
    data_clean = df.dropna(subset=["Score"])
    
    selected_abv_str = str(selected_item.get('ABV', '0')).replace('%', '')
    selected_abv = pd.to_numeric(selected_abv_str, errors='coerce')
    if pd.isna(selected_abv): selected_abv = 0

    selected_price_str = str(selected_item.get('Price', '0')).replace('$', '').replace(',', '')
    selected_price = pd.to_numeric(selected_price_str, errors='coerce')
    if pd.isna(selected_price): selected_price = 0
    
    selected_rating_val = selected_item.get('Rating', 0)
    selected_rating = pd.to_numeric(selected_rating_val, errors='coerce')
    if pd.isna(selected_rating): selected_rating = 0

    selected_rate_count_val = selected_item.get('Rate Count', 0)
    selected_rate_count = pd.to_numeric(selected_rate_count_val, errors='coerce')
    if pd.isna(selected_rate_count): selected_rate_count = 0
    
    selected_score = max(selected_abv * 10 + selected_rating * selected_rate_count - selected_price * 2, 0)
    selected_name = selected_item.get('Name', 'Unknown')

    all_scores = data_clean['Score'].tolist()
    if all_scores: 
        selected_percentile = percentileofscore(all_scores, selected_score, kind='rank')
    else:
        selected_percentile = 0

    def format_value(value):
        if isinstance(value, list):
            return ', '.join(str(v) for v in value)
        if pd.isna(value):
            return "N/A"
        return str(value)

    return dbc.Row([
        html.H3("Selected product overview", style={"color": "#2c3e50", "fontWeight": "bold"}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H4("Name", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Name')), style={"color": "#7f8c8d"}),
                html.H4("Type", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Type')), style={"color": "#7f8c8d"}),
                html.H4("Price", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Price')), style={"color": "#7f8c8d"}),
                html.H4("Brand", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Brand')), style={"color": "#7f8c8d"}),
                html.H4("Country", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Country')), style={"color": "#7f8c8d"}),
                html.H4("Ratings", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Rating')), style={"color": "#7f8c8d"}),
                html.H4("Rate count", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Rate Count')), style={"color": "#7f8c8d"})
            ], md=4),
            
            dbc.Col([
                html.H4("Description", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Description')), style={"color": "#7f8c8d"}),
                html.H4("Alcohol by Volume", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'ABV')), style={"color": "#7f8c8d"}),
                html.H4("Available volumes", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Volume')), style={"color": "#7f8c8d"}),
                html.H4("Suggested serving temperature", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Suggested Serving Temperature')), style={"color": "#7f8c8d"}),
                html.H4("Tasting notes", style={"color": "#34495e"}),
                html.P(format_value(extract_item_value(selected_item, 'Tasting Notes')), style={"color": "#7f8c8d"})
            ], md=4), 
            
            dbc.Col([
                html.H4("Percentile Rank", style={"color": "#34495e"}),
                html.P([
                    "Our score is computed as ",
                    html.Code("ABV × 10 + Rating × RateCount − Price × 2", style={"fontFamily": "monospace", "background": "#f4f4f4", "padding": "2px 6px", "borderRadius": "4px", 'color': '#34495e'})
                ], style={"color": "#7f8c8d", "marginBottom": "8px"}),
                html.P([
                    "Selected product score: ",
                    html.Strong(f"{selected_score:.0f}")
                ], style={"color": "#7f8c8d"}),
                html.P([
                    "This product scores better than ",
                    html.Strong(f"{selected_percentile:.1f}%"),
                    " of other products."
                ], style={"color": "#7f8c8d"}),
                dcc.Graph(
                    id='score-gauge-plot',
                    figure=go.Figure(
                        go.Indicator(
                            mode = "gauge+number",
                            value = selected_percentile,
                            number = {'suffix': "%", 'font': {'size': 24, 'color': '#2c3e50'}},
                            domain = {'x': [0, 1], 'y': [0, 1]},
                            title = {'text': '', 'font': {'color': '#2c3e50'}},
                            gauge = {
                                'axis': {
                                    'range': [0, 100],
                                    'showticklabels': False, 
                                    'ticks': '', 
                                },
                                'bar': {'thickness': 0}, 
                                'borderwidth': 0.5,
                                'steps': [ 
                                    {'range': [0, 20], 'color': '#e3f2fd'},
                                    {'range': [20, 40], 'color': '#bbdefb'},
                                    {'range': [40, 60], 'color': '#90caf9'},
                                    {'range': [60, 80], 'color': '#42a5f5'},
                                    {'range': [80, 100], 'color': '#1976d2'} 
                                ],
                                'threshold': {
                                    'line': {'color': "#1565c0", 'width': 3}, 
                                    'thickness': 0.85,
                                    'value': selected_percentile
                                }
                            }
                        )
                    ).update_layout(
                        paper_bgcolor="rgba(248,249,250,1)",
                        plot_bgcolor="rgba(248,249,250,1)",
                    ),
                    config={'displayModeBar': False},
                    style={'height': '300px',
                           'margin': {'t': 10, 'b': 10, 'l': 10, 'r': 10}
                           } 
                )
            ], md=4)
        ])
    ], class_name="bg-light border rounded m-2 p-3")