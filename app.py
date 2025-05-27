from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from data.loader import load_data, extract_unique_values
from components.sidebar import create_sidebar
from components.content import create_content_area
from callbacks.interactions import register_callbacks

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

data_beer, data_spirits, data_wine = load_data()


categories = taste = food = []

@app.callback(
    Output('some-output-id', 'children'),
    Input('some-input-id', 'value')
)
def set_drink_type(drink_type):
    if drink_type == 'Beer':
        data = data_beer
    elif drink_type == 'Spirits':
        data = data_spirits
    else:
        data = data_wine
    categories = extract_unique_values(data, 'Categories')
    taste = extract_unique_values(data, 'Tasting Notes')
    food = extract_unique_values(data, 'Food Pairing') if drink_type == 'Wine' else []

app.layout = dbc.Container([
    # Title row
    dbc.Row([
        dbc.Col([
            html.H1("Welcome to the alcohol dashboard!", className="display-4 text-center"),
            html.P("The dashboard has been designed to help you find a proper drink for yourself", 
                  className="text-center")
        ], width=12)
    ], className="mt-3 mb-4"),
    
    # Main content row
    dbc.Row([
        create_sidebar(categories, taste, food),
        create_content_area()
    ])
], fluid=True)

# Register callbacks
register_callbacks(app)

# Run server
if __name__ == '__main__':
    app.run(debug=False)