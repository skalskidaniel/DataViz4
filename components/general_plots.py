from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import extract_item_value, load_data

def create_general_plots():
    wines = load_data("wine")
    beers = load_data("beer")
    spirits = load_data("spirits")

    # Clean and filter wines
    wines["Price"] = wines["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
    wines["Price"] = pd.to_numeric(wines["Price"], errors="coerce")
    wines = wines[(wines["Price"] < 200) & (wines["Price"] > 0)]
    wines["ABV"] = wines["ABV"].astype(str).str.replace(r'[%]', '', regex=True)
    wines["ABV"] = pd.to_numeric(wines["ABV"], errors="coerce")
    wines = wines[wines["ABV"] < 100]

    # Clean and filter beers
    beers["Price"] = beers["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
    beers["Price"] = pd.to_numeric(beers["Price"], errors="coerce")
    beers = beers[(beers["Price"] < 200) & (beers["Price"] > 0)]
    beers["ABV"] = beers["ABV"].astype(str).str.replace(r'[%]', '', regex=True)
    beers["ABV"] = pd.to_numeric(beers["ABV"], errors="coerce")
    beers = beers[beers["ABV"] < 100]

    # Clean and filter spirits
    spirits["Price"] = spirits["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
    spirits["Price"] = pd.to_numeric(spirits["Price"], errors="coerce")
    spirits = spirits[(spirits["Price"] < 200) & (spirits["Price"] > 0)]
    spirits["ABV"] = spirits["ABV"].astype(str).str.replace(r'[%]', '', regex=True)
    spirits["ABV"] = pd.to_numeric(spirits["ABV"], errors="coerce")
    spirits = spirits[spirits["ABV"] < 100]

    return dbc.Row([
        html.H3("General alcohol categories overview"),
        html.Hr(),

        dbc.Row([
            dbc.Col([
                html.H4("Price distribution by alcohol type"),
                dcc.Graph(
                    id="price-distribution",
                    figure={
                        "data": [
                            {
                                "y": beers["Price"],
                                "text": beers["Name"],
                                "name": "Beer",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Price: %{y}<extra></extra>"
                            },
                            {
                                "y": wines["Price"],
                                "text": wines["Name"],
                                "name": "Wine",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Price: %{y}<extra></extra>"
                            },
                            {
                                "y": spirits["Price"],
                                "text": spirits["Name"],
                                "name": "Spirits",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Price: %{y}<extra></extra>"
                            }
                        ],
                        "layout": {
                            "title": "Price Distribution by Alcohol Type",
                            "yaxis": {"title": "Price"},
                            "boxmode": "group"
                        }
                    }
                ),
                html.P("Note: The price distribution had been limited to values below 200 USD to ensure clarity in the visualization. However wines and spirits can be found at much higher prices (even around 40000USD)"),
            ])
        ]),

        dbc.Row([
            dbc.Col([
                html.H4("Alcohol by Volume (ABV) distribution by alcohol type"),
                dcc.Graph(
                    id="abv-distribution",
                    figure={
                        "data": [
                            {
                                "y": beers["ABV"],
                                "text": beers["Name"],
                                "name": "Beer",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>"
                            },
                            {
                                "y": wines["ABV"],
                                "text": wines["Name"],
                                "name": "Wine",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>"
                            },
                            {
                                "y": spirits["ABV"],
                                "text": spirits["Name"],
                                "name": "Spirits",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>"
                            }
                        ],
                        "layout": {
                            "title": "ABV Distribution by Alcohol Type",
                            "yaxis": {"title": "ABV (%)"},
                            "boxmode": "group"
                        }
                    }
                )
            ])
        ]),

        dbc.Row([
            dbc.Col([
                html.H4("Rating distribution by alcohol type"),
                dcc.Graph(
                    id="rating-distribution",
                    figure={
                        "data": [
                            {
                                "y": beers["Rating"],
                                "text": beers["Name"],
                                "name": "Beer",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Rating: %{y}<extra></extra>"
                            },
                            {
                                "y": wines["Rating"],
                                "text": wines["Name"],
                                "name": "Wine",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Rating: %{y}<extra></extra>"
                            },
                            {
                                "y": spirits["Rating"],
                                "text": spirits["Name"],
                                "name": "Spirits",
                                "type": "box",
                                "hovertemplate": "%{text}<br>Rating: %{y}<extra></extra>"
                            }
                        ],
                        "layout": {
                            "title": "Rating Distribution by Alcohol Type",
                            "yaxis": {"title": "Rating"},
                            "boxmode": "group"
                        }
                    }
                )
            ])
        ]),
    ], class_name="bg-light border rounded m-3 p-3")