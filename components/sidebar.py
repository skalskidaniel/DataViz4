from dash import html, dcc
import dash_bootstrap_components as dbc

def create_sidebar(categories, countries, taste, food):
    return  dbc.Row([
                html.H3("Parameters", style={"color": "#2c3e50", "fontWeight": "bold"}),
                html.Hr(),
                html.H4("Drink type", style={"color": "#34495e"}),
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
                    multi=True
                ),
                
                html.H4("Food Pairing", className='mt-3', style={"color": "#34495e"}), 
                dcc.Dropdown(
                    id='food-filter',
                    options=[{'label': c, 'value': c} for c in food],
                    multi=True
                ),
                
                html.H4("Price range (per liter)", className='mt-3', style={"color": "#34495e"}),
                dcc.RangeSlider(
                    id='price-range',
                    min=0,
                    max=1000,
                    step=5,
                    marks={i: f"${i}" for i in range(0, 1000, 200)}, #TODO adjust price range and allow to infinity
                    value=[0, 200]
                )
            ], className="bg-light border rounded m-2 p-3")