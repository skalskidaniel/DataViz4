from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from data.loader import extract_item_value, load_data


def create_abv_by_type():
    
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
                html.H3("Alcohol by Volume by the type of alcohol"),
                html.Hr(),
                html.P("Spirits tend to have much more alcohol percentage than the others."),
                dcc.Graph(
                    id="abv-distribution",
                    figure={
                        "data": [
                            {
                                "y": beers["ABV"],
                                "text": beers["Name"],
                                "name": "Beer",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>",
                                'marker': {'color': '#0dcaf0', 'size': 10} 
                            },
                            {
                                "y": wines["ABV"],
                                "text": wines["Name"],
                                "name": "Wine",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>",
                                'marker': {'color': '#0dcaf0', 'size': 10} 
                            },
                            {
                                "y": spirits["ABV"],
                                "text": spirits["Name"],
                                "name": "Spirits",
                                "type": "box",
                                "hovertemplate": "%{text}<br>ABV: %{y}<extra></extra>",
                                'marker': {'color': '#0dcaf0', 'size': 10} 
                            }
                        ],
                        "layout": {
                            "title": "ABV Distribution by Alcohol Type",
                            "yaxis": {"title": "ABV (%)"},
                            "boxmode": "group",
                            'plot_bgcolor': '#f8f9fa',
                            'paper_bgcolor': '#f8f9fa',
                            'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40},
                            'showlegend': False
                        }
                    },
                    config={'displayModeBar': False}
                )
            ], className="bg-light border rounded m-3 p-3")