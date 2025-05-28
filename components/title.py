from dash import html, dcc
import dash_bootstrap_components as dbc

def create_title():
    return dbc.Col([
            html.H1("Welcome to the alcohol dashboard!", className="display-4 text-center"),
            html.P("The dashboard has been designed to help you find a proper drink for yourself", 
                  className="text-center")
        ], width=12)