from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from data.loader import Loader
from callbacks.interactions import Callbacker
from components.sidebar import create_sidebar
from components.top_picks import create_top_picks
from components.header import create_header
from components.tabs import create_tabs

app = Dash(name="AlcoDash", external_stylesheets=[dbc.themes.BOOTSTRAP])

loader = Loader()
loader.load_data('Beer')
data = loader.get_data()

app.layout = dbc.Container([
    create_header(),
    
    dbc.Row([
        dbc.Col(width=3),
        dbc.Col([
            *create_tabs()
        ], width=9)
    ]),
    dbc.Row([
        dbc.Col([
            create_sidebar(*loader.extract_options_for_sidebar())
        ], width=3),

        dbc.Col([
            html.Div(id='tab-content', className="m-2", children=[create_top_picks(data)])
        ], width=9)
    ]),
    
    dbc.Row([
        
    ], id='overview', class_name="m-2")
    
], fluid=True, class_name="bg-light")

callbacker = Callbacker()

callbacker.register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False)