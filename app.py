from dash import Dash
import dash_bootstrap_components as dbc
from data.loader import load_data, extract_unique_values
from components.sidebar import create_sidebar
from components.top_picks import create_top_picks
from callbacks.interactions import register_callbacks
from components.title import create_title
from components.overview import create_overview
from components.general_plots import create_general_plots

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

data = load_data('Beer')
categories = extract_unique_values(data, 'Categories')
taste = extract_unique_values(data, 'Tasting Notes')
food = []
selected_item = data.iloc[0]

app.layout = dbc.Container([

    create_title(),

    create_general_plots(),
    
    dbc.Row([
        create_sidebar(categories, taste, food),
        create_top_picks(data)
    ], className="m-1"),
    
    create_overview(selected_item, data),
    
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False)