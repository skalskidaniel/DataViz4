from dash import html, dcc
import dash_bootstrap_components as dbc

def create_sidebar(categories, taste, food):
    return dbc.Row([
            dbc.Col([
                html.H3("Adjust your preferences", className="mt-3 mb-3"),
                html.H4("Drink type", className="mt-3 mb-3"),
                dbc.RadioItems(
                    id='type',
                    options=[
                        {'label': '\u00A0\u00A0Beer', 'value': 'Beer'},
                        {'label': '\u00A0\u00A0Wine', 'value': 'Wine'},
                        {'label': '\u00A0\u00A0Spirits', 'value': 'Spirits'}
                    ],
                    value='Beer',
                    labelStyle={'display': 'block', 'marginBottom': '8px', 'paddingLeft': '4px'},
                    className="mt-3 mb-3"
                ),
                
                html.H4("Category", className="mt-3 mb-3"),
                dcc.Dropdown(
                id='category',
                options=[{'label': c, 'value': c} for c in categories],
                className="mt-3 mb-3",
                ),
                
                html.H4("Tasting Notes", className="mt-3 mb-3"),
                dcc.Dropdown(
                    id='taste-filter',
                    options=[{'label': c, 'value': c} for c in taste], 
                    multi=True,
                    className="mt-3 mb-3"
                ),
                
                html.H4("Food Pairing", className="mt-3 mb-3"), 
                dcc.Dropdown(
                    id='food-filter',
                    options=[{'label': c, 'value': c} for c in food],
                    multi=True,
                    className="mt-3 mb-3",
                ),
                
                html.H4("Price range (per liter)"),
                dcc.RangeSlider(
                    id='price-range',
                    min=0,
                    max=100,
                    step=5,
                    marks={i: f"${i}" for i in range(0, 101, 20)},
                    value=[0, 50],
                    className="mt-3 mb-1"
                )
            ], width=3, className="bg-light p-3 border rounded mr-1 ml-1")
        ])