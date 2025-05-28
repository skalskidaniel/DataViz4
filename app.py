from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from data.loader import load_data, extract_unique_values
from components.sidebar import create_sidebar
from components.content import create_content_area
from callbacks.interactions import register_callbacks
from components.title import create_title

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

data = load_data('Beer')
categories = extract_unique_values(data, 'Categories')
taste = extract_unique_values(data, 'Tasting Notes')
food = []

app.layout = dbc.Container([

    dbc.Row([
        create_title()
    ], className="m-3"),
    
    dbc.Row([
        create_sidebar(categories, taste, food),
        create_content_area(data)
    ], class_name="m-3")
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False)