from dash import html, dcc
import dash_bootstrap_components as dbc

def create_title():
    return dbc.Row([
            html.H1("Welcome to Alcohol Selection Dashboard", className="text-center")
        ], class_name="bg-light border rounded m-3 p-3")