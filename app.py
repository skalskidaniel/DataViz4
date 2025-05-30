from dash import Dash, html
import dash_bootstrap_components as dbc
from data.loader import load_data, extract_unique_values
from components.sidebar import create_sidebar
from components.top_picks import create_top_picks
from callbacks.interactions import register_callbacks
from components.title import create_title
from components.overview import create_overview
from components.mock_graph import create_mock_graph_panel
from components.abv_plot import create_abv_by_type
from components.prices_plot import create_price_distribution
from components.ratings_plot import create_ratings_plot
from components.about import create_about_section
from components.logo import create_logo

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

data = load_data('Beer')
categories = extract_unique_values(data, 'Categories')
countries = extract_unique_values(data, 'Country')
taste = extract_unique_values(data, 'Tasting Notes')
food = []
selected_item = data.iloc[0]

app.layout = dbc.Container([

    create_title(),
    
    dbc.Row([
        create_about_section(),
        create_logo()
    ], className="m-1"),
    
    dbc.Row([
        create_sidebar(categories, countries, taste, food),
        create_top_picks(data)
    ], className="m-1"),
    
    html.Div([
        create_overview(selected_item, data)
    ], id='overview'),
    
    dbc.Row([
        dbc.Col(create_mock_graph_panel()),
        dbc.Col(create_mock_graph_panel())
    ]),
    
    dbc.Row([
        dbc.Col(create_mock_graph_panel()),
        dbc.Col(create_mock_graph_panel())
    ])
    
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)