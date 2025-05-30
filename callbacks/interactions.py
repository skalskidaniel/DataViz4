from dash import Input, Output, Dash, html
from data.loader import extract_unique_values, load_data, get_filtered_items, get_top_scored_items
import pandas as pd
from components.overview import create_overview

def register_callbacks(app: Dash):
    
    @app.callback(
        Output('category', 'value'),
        Output('country', 'value'),
        Output('taste-filter', 'value'),
        Output('food-filter', 'value'),
        Input('type', 'value')
    )
    def changed_drink_type(type):
        return None, None, None, None
    
    @app.callback(
    Output('category', 'options'),
    Output('country', 'options'),
    Output('taste-filter', 'options'),
    Output('food-filter', 'options'),
    Output('food-filter', 'disabled'),
    Output('top-picks-table', 'children'),
    Input('type', 'value'),
    Input('category', 'value'),
    Input('country', 'value'),
    Input('taste-filter', 'value'),
    Input('food-filter', 'value'),
    Input('price-range', 'value')
    )
    def sidebar_callbacks(type, category, country, tastes, foods, price_range):
        data = load_data(type)
        filtered_data = get_filtered_items(data, category, country, tastes, foods, price_range)
        categories = extract_unique_values(filtered_data, 'Categories')
        countries = extract_unique_values(filtered_data, 'Country')
        taste = extract_unique_values(filtered_data, 'Tasting Notes')
        food = extract_unique_values(filtered_data, 'Food Pairing') if type == 'Wine' else []
        
        top_items = get_top_scored_items(filtered_data)
        cols = ["Name", "Country", "Price", "Rating", "Score"]
        top_items = top_items[cols].head(13)
        
        if top_items.empty:
            return [
                html.Thead(html.Tr([html.Th(col) for col in ["Name", "Type", "Price", "Rating"]])),
                html.Tbody(html.Tr([html.Td('No results found.', colSpan=4, className="text-center")]))
            ]
        
        header = html.Thead(html.Tr([html.Th(col) for col in top_items.columns]))
        
        rows = []
        for _, row in top_items.iterrows():
            rows.append(html.Tr([html.Td(row[col]) for col in top_items.columns]))
        body = html.Tbody(rows)
        
        return categories, countries, taste, food, len(food) <= 0, [header, body]
    
        
    # @app.callback(
    #     Output('overview', 'children'),
    #     Input('type', 'value'),
    #     Input('category', 'value'),
    #     Input('country', 'value'),
    #     Input('taste-filter', 'value'),
    #     Input('food-filter', 'value'),
    #     Input('price-range', 'value')
    # )
    # def generate_overview(type: str, category: str, country: str, tastes: list[str], food: list[str], price_range: list[int]):
        
    #     data = load_data(type)
    #     filtered_data = get_filtered_items(data, category, country, tastes, food, price_range)
    #     top_item = get_top_scored_items(filtered_data).iloc[0]
        
    #     return create_overview(top_item, data)