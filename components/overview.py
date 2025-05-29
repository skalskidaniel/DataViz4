from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import extract_item_value

def create_overview(selected_item: pd.Series):
    
    return dbc.Row([
        html.H3("Product overview"),
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
                html.H4("Description"),
                html.P(extract_item_value(selected_item, 'Description')),
                html.H4("Alcohol by Volume"),
                html.P(selected_item.ABV),
                html.H4("Available volumes"),
                html.P(extract_item_value(selected_item, 'Volume')),
                html.H4("Suggested serving temperature"),
                html.P(extract_item_value(selected_item, 'Suggested Serving Temperature')),
            ]),
            
            dbc.Col([
                html.H4("Reviews"),
                html.P("There will be a ratings bar chart", className="fst-italic"),
                html.P("The feature will include a visual chart showing rating distributions. When users hover over any review, they’ll see a breakdown of how many ratings were given for each star level (1-5 stars).", className="fst-italic")
            ])
        ])
    ], class_name="bg-light border rounded m-3 p-3")