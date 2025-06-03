from dash import html, dcc
import dash_bootstrap_components as dbc
import math

def create_sidebar(categories, countries, taste, food, max_price, price_marks, chosen_price_range):
    return dbc.Row([
        html.H4("Drink type", className='mt-3', style={"color": "#34495e"}),
        dbc.RadioItems(
            id='type',
            options=[
                {'label': '\u00A0\u00A0Beer', 'value': 'Beer'},
                {'label': '\u00A0\u00A0Wine', 'value': 'Wine'},
                {'label': '\u00A0\u00A0Spirits', 'value': 'Spirits'}
            ],
            value='Beer'
        ),
        
        html.H4("Category", className='mt-3', style={"color": "#34495e"}),
        dcc.Dropdown(
            id='category',
            options=[{'label': c, 'value': c} for c in categories]
        ),
        
        html.H4("Country", className="mt-3", style={"color": "#34495e"}),
        dcc.Dropdown(
            id='country',
            options=[{'label': c, 'value': c} for c in countries]
        ),
        
        html.H4("Tasting Notes", className='mt-3', style={"color": "#34495e"}),
        dcc.Dropdown(
            id='taste-filter',
            options=[{'label': c, 'value': c} for c in taste], 
        ),
        
        html.H4("Food Pairing", className='mt-3', style={"color": "#34495e"}), 
        dcc.Dropdown(
            id='food-filter',
            options=[{'label': c, 'value': c} for c in food],
        ),
        
        html.H4("Price range (per liter)", className='mt-3', style={"color": "#34495e"}),
        dcc.RangeSlider(
            id='price-range',
            min=0,
            max=int(math.ceil(max_price / 10.0)) * 10,
            step=5,
            marks=price_marks, # type: ignore
            value=[chosen_price_range[0], chosen_price_range[1]],
            tooltip={"placement": "bottom", "template": "${value}"}
        )
    ], className="bg-light border m-2 p-1")