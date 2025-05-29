from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def create_mock_graph_panel():
    return dbc.Row([
        html.H3("There will be a graph", className="fs-italic"),
        html.Hr(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    ], className="bg-light border rounded m-3 p-3")