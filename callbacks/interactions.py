from dash import Input, Output, Dash, html
from data.loader import extract_unique_values, load_data, query_data
import pandas as pd

def register_callbacks(app: Dash):
    
    @app.callback(
    Output('category', 'options'),
    Output('taste-filter', 'options'),
    Output('food-filter', 'options'),
    Output('food-filter', 'disabled'),
    Input('type', 'value')
    )
    def set_drink_type(type):
        data = load_data(type)
        categories = extract_unique_values(data, 'Categories')
        taste = extract_unique_values(data, 'Tasting Notes')
        food = extract_unique_values(data, 'Food Pairing') if type == 'Wine' else []
        
        return categories, taste, food, len(food) <= 0
    
    
    @app.callback(
        Output('top-picks-table', 'children'),
        Input('type', 'value'),
        Input('category', 'value'),
        Input('taste-filter', 'value'),
        Input('food-filter', 'value'),
        Input('price-range', 'value')
    )
    def generate_top_picks(type: str, category: str, tastes: list[str], food: list[str], price_range: list[int]):
        
        data = load_data(type)
        q = query_data(data, category, tastes, food, price_range)
        
        if q.empty:
            return [
                html.Thead(html.Tr([html.Th(col) for col in ["Name", "Type", "Price", "Rating"]])),
                html.Tbody(html.Tr([html.Td('No results found.', colSpan=4, className="text-center")]))
            ]
        
        header = html.Thead(html.Tr([html.Th(col) for col in q.columns]))
        
        rows = []
        for _, row in q.iterrows():
            rows.append(html.Tr([html.Td(row[col]) for col in q.columns]))
        body = html.Tbody(rows)
        
        return [header, body]
    
    #TODO add overview callbacks