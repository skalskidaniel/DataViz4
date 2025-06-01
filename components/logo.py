from dash import html, dcc
import dash_bootstrap_components as dbc


def create_logo():
    return dbc.Row([
            html.Img(
                src="/assets/logo2.png",
                alt="Logo",
                style={"height": "225px"},
                className="m-3"
            )
        ],
        className="bg-light border rounded m-2 p-3")