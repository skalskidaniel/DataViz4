from dash import html, dcc
import dash_bootstrap_components as dbc

def create_title():
    return dbc.Row([
            html.H1("Welcome to the alcohol dashboard!", className="text-center"),
            html.P("The dashboard has been designed to help you find a proper drink for yourself. Our top picks are chosen based on your parameters, and sorted by ratings and price.", 
                  className="text-center")
        ], class_name="bg-light border rounded m-3 p-3")