from dash import html, dcc
import dash_bootstrap_components as dbc

def create_title():
    return dbc.Card(
            dbc.Row([
            html.H1("Welcome to the alcohol dashboard!", className="display-4 text-center"),
            html.P("The dashboard has been designed to help you find a proper drink for yourself", 
                  className="text-center")
        ]), class_name="bg-light border rounded m-3") #TODO fix alignment