from dash import html, dcc
import dash_bootstrap_components as dbc

def create_tabs():
    return dbc.Tabs([
                dbc.Tab(label="Top Picks", tab_id="top-picks"),
                dbc.Tab(label="Map", tab_id="map"),
                dbc.Tab(label="Top Producers", tab_id="top-producers"),
                dbc.Tab(label="Top Categories", tab_id="top-categories"),
                dbc.Tab(label="Tasting Notes", tab_id="tasting-notes"),
            ], id="tabs", active_tab="top-picks"),