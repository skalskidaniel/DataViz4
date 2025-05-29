from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import extract_item_value

def create_general_plots():
    wines = pd.read_csv("data/wine_data.csv", index_col=0)
    beers = pd.read_csv("data/beer_data.csv", index_col=0)  
    spirits = pd.read_csv("data/spirits_data.csv", index_col=0)

    return dbc.Row([
        html.H3("General alcohol categories overview"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H4("Name"),
                html.P(selected_item.Name),
                html.H4("Type"),
                html.P(selected_item.Type),
                html.H4("Price"),
                html.P(extract_item_value(selected_item, 'Price')),
                html.H4("Brand"),
                html.P(selected_item.Brand),
                html.H4("Country"),
                html.P(selected_item.Country),
                html.H4("Tasting notes"),
                html.P(extract_item_value(selected_item, 'Tasting Notes'))
            ]),
            
            dbc.Col([
                html.H4("Investment potential"),
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
                                'marker': {'color': '#888', 'size': 10}
                            },
                            {
                                'x': [selected_item['Price']],
                                'y': [selected_item['ABV']],
                                'mode': 'markers',
                                'type': 'scatter',
                                'text': [selected_item['Name']],
                                'hovertemplate': '<b>%{text}</b><br>Price: %{x}<br>ABV: %{y}<extra></extra>',
                                'name': 'Selected',
                                'marker': {'color': 'crimson', 'size': 18}
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
                            }
                        }
                    }
                ),
            ])
        ])
    ], class_name="bg-light border rounded m-3 p-3")