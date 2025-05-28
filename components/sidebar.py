from dash import html, dcc
import dash_bootstrap_components as dbc

def create_sidebar(categories, taste, food):
    return  dbc.Col([
                html.H3("Adjust your preferences", className="m-1"),
                html.H4("Drink type", className="m-3"),
                dbc.RadioItems(
                    id='type',
                    options=[
                        {'label': '\u00A0\u00A0Beer', 'value': 'Beer'},
                        {'label': '\u00A0\u00A0Wine', 'value': 'Wine'},
                        {'label': '\u00A0\u00A0Spirits', 'value': 'Spirits'}
                    ],
                    value='Beer',
                    className="m-3"
                ),
                
                html.H4("Category", className="m-3"),
                dcc.Dropdown(
                id='category',
                options=[{'label': c, 'value': c} for c in categories],
                className="m-3",
                ),
                
                html.H4("Tasting Notes", className="m-3"),
                dcc.Dropdown(
                    id='taste-filter',
                    options=[{'label': c, 'value': c} for c in taste], 
                    multi=True,
                    className="m-3"
                ),
                
                html.H4("Food Pairing", className="m-3"), 
                dcc.Dropdown(
                    id='food-filter',
                    options=[{'label': c, 'value': c} for c in food],
                    multi=True,
                    className="m-3",
                ),
                
                html.H4("Price range (per liter)", className="m-3"),
                dcc.RangeSlider(
                    id='price-range',
                    min=0,
                    max=100,
                    step=5,
                    marks={i: f"${i}" for i in range(0, 101, 20)},
                    value=[0, 50],
                    className="m-3"
                )
            ], width=3, className="bg-light border rounded m-3 p-3")