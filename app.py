from dash import Dash, html, dcc
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
    
    dcc.Store(id='selected-item-store'),

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
        dbc.Col([
        html.H3("Top producers", className="fs-italic"), # take into account only full data, no sidebar adjustments, sort by ratings or popularity
        html.Hr(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    ], className="bg-light border rounded m-3 p-3"),
        
        dbc.Col([
        html.H3("Top categories", className="fs-italic"), # take into account only full data, bar chart
        html.Hr(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    ], className="bg-light border rounded m-3 p-3")
    ]),
    
    dbc.Row([
        dbc.Col([
        html.H3("Heatmap of tasting notes", className="fs-italic"), # take into account filtered data
        html.Hr(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    ], className="bg-light border rounded m-3 p-3"),
        
        dbc.Col(create_mock_graph_panel())
    ]),
    
    dbc.Row([
        html.H3("Geographical map of producers", className="fs-italic"),
        html.Hr(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    ], className="bg-light border rounded m-3 p-3")
    
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)