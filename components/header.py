from dash import html, dcc
import dash_bootstrap_components as dbc

def create_header():
    return dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(
                    src="/assets/logo_put.png",
                    alt="Logo",
                    style={
                        "maxWidth": "100%",
                        "height": "auto",
                        "maxHeight": "150px"
                    },
                    className="img-fluid"
                )
            ], className="d-flex justify-content-center mb-4"),
            
            html.H1("Alcohol Selection Dashboard", 
                   className="display-4 fw-bold mb-3 text-center",
                   style={"color": "#2c3e50"}),
            html.P([
                "Discover and analyze alcoholic beverages with respect to complete ranges of their values in a comprehensive dashboard. ",
                "Explore the properties of popular drink categories, analyze regional distribution, and examine tasting profiles. ",
                "Filter and compare products to find your perfect match based on price, rating, and personal preferences."
            ], className="lead mb-4 text-center", style={"color": "#34495e", "lineHeight": "1.6"}),
            html.P([
                "Use the sidebar controls to filter products, explore different beverage types, and discover top-rated selections. ",
                "The interactive visualizations provide insights into geographic distribution, popular categories, and tasting note patterns."
            ], className="text-center", style={"color": "#7f8c8d", "fontSize": "1rem"}),
            
        ], width=12)
    ], className="bg-light border rounded m-2 p-3")
