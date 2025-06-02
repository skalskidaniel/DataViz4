import os
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from data.loader import load_data, extract_unique_values
from components.sidebar import create_sidebar
from components.top_picks import create_top_picks
from callbacks.interactions import register_callbacks
from components.header import create_header
from components.overview import create_overview
from components.map import create_map
from components.top_producers import create_top_producers
from components.top_categories import create_top_categories
from components.tasting_notes import create_notes_bubble_chart

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

data = load_data('Beer')
categories = extract_unique_values(data, 'Categories')
countries = extract_unique_values(data, 'Country')
taste = extract_unique_values(data, 'Tasting Notes')
food = []
selected_item = data.iloc[0]

app.layout = dbc.Container([
    
    dcc.Store(id='selected-item-store'),

    create_header(),
    
    dbc.Row([
        dbc.Col(create_sidebar(categories, countries, taste, food), width=3),
        dbc.Col(create_top_picks(data), width=9)
    ]),
    
    html.Div([
        create_overview(selected_item, data)
    ], id='overview'),
    
    dbc.Row([
        dbc.Col(html.Div(create_top_categories(data), id='top-categories')),
        dbc.Col(html.Div(create_notes_bubble_chart(data), id='tasting-notes-chart'))
    ], align='stretch'),
    
    html.Div(create_map(data), id='map'),

    html.Div(create_top_producers(data), id='top-producers'),
    
], fluid=True)

register_callbacks(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)), debug=False)