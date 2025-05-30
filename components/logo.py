from dash import html, dcc
import dash_bootstrap_components as dbc


def create_logo():
    return dbc.Col([
            html.Img(
                src="/assets/logo2.png",
                alt="Logo",
                style={"height": "250px"},
                className="m-3"
            )
        ],  width="auto",
            className="bg-light border rounded m-3 p-3")