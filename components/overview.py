from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import extract_item_value

def create_overview(selected_item: pd.Series, data: pd.DataFrame):
    
    def format_value(value):
        if isinstance(value, list):
            return ', '.join(str(v) for v in value)
        return str(value)

    return dbc.Row([
        html.H3("Top product overview"),
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
                html.H4("Investment potential"),
                html.P("The plot shows whether it is profitable to drink this product. The lower price and higher ABV, the better."),
                dcc.Graph(
                    id='abv-vs-price-scatter',
                    figure={
                        'data': [
                            {
                                'x': data['Price'],
                                'y': data['ABV'],
                                'mode': 'markers',
                                'type': 'scatter',
                                'text': data['Name'],
                                'hovertemplate': '%{text}<br>Price: %{x}<br>ABV: %{y}<extra></extra>',
                                'name': 'Alcohol % vs Price',
                                'marker': {'color': '#e9ecef', 'size': 10}
                            },
                            {
                                'x': [selected_item['Price']],
                                'y': [selected_item['ABV']],
                                'mode': 'markers',
                                'type': 'scatter',
                                'text': [selected_item['Name']],
                                'hovertemplate': '<b>%{text}</b><br>Price: %{x}<br>ABV: %{y}<extra></extra>',
                                'name': 'Selected',
                                'marker': {'color': '#0dcaf0', 'size': 18} 
                            }
                        ],
                        'layout': {
                            'title': 'Alcohol % vs Price',
                            'xaxis': {'title': 'Price', 'range': [0, 100]},
                            'yaxis': {'title': 'Alcohol % (ABV)'},
                            'legend': {
                                'orientation': 'h',
                                'yanchor': 'bottom',
                                'y': -0.3,
                                'xanchor': 'center',
                                'x': 0.5
                            },
                            'plot_bgcolor': '#f8f9fa',
                            'paper_bgcolor': '#f8f9fa',
                            'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}
                        }
                    },
                    config={'displayModeBar': False}
                ),
            ])
        ])
    ], class_name="bg-light border rounded m-3 p-3")