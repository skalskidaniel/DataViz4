from dash import html, dcc
import dash_bootstrap_components as dbc

def create_about_section():
    return dbc.Col([
            html.H3("About the Dashboard"),
            html.Hr(),
            html.P([
                html.B("1. "),
                "This dashboard is designed to assist you in discovering suitable drink options tailored to your preferences."
            ]),
            html.P([
                html.B("2. "),
                "Use the filters in the left sidebar to narrow down your drink selection based on various criteria."
            ]),
            html.P([
                html.B("3. "),
                "Top recommendations are selected based on a computed score: MAX{(ABV × 10) + (Rating × RateCount) − (Price × 2), 0}."
            ]),
            html.P([
                html.B("4. "),
                "Clicking on a product in the table will display a detailed overview below."
            ]),
            html.P([
                html.B("5. "),
                "Comprehensive data analytics are available in the lower section of the dashboard."
            ])
        ], class_name="bg-light border rounded m-3 p-3")