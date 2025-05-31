from dash import Input, Output, Dash, html
from data.loader import extract_unique_values, load_data, get_filtered_items, get_top_scored_items
import pandas as pd
from components.overview import create_overview
from components.top_categories import create_top_categories
from components.top_producers import create_top_producers
from components.tasting_notes import create_notes_heatmap

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
    Output('top-picks-table', 'data'),
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
        top_items = top_items[cols].head(100)
        
        table_data = top_items.to_dict('records') if not top_items.empty else []
        
        return categories, countries, taste, food, len(food) <= 0, table_data
    
    @app.callback(
        Output('overview', 'children'),
        Input('type', 'value'),
        Input('category', 'value'),
        Input('country', 'value'),
        Input('taste-filter', 'value'),
        Input('food-filter', 'value'),
        Input('price-range', 'value'),
        Input('top-picks-table', 'selected_rows')
    )
    def generate_overview(type: str, category: str, country: str, tastes: list[str], food: list[str], price_range: list[int], selected_rows):
        
        data = load_data(type)
        filtered_data = get_filtered_items(data, category, country, tastes, food, price_range)
        selected_item = pd.Series()
        
        if selected_rows and len(selected_rows) > 0:
            top_items = get_top_scored_items(filtered_data)
            if not top_items.empty and selected_rows[0] < len(top_items):
                selected_item = top_items.iloc[selected_rows[0]]
            else:
                selected_item = get_top_scored_items(filtered_data).iloc[0] if not filtered_data.empty else data.iloc[0]
        else:
            if not filtered_data.empty:
                selected_item = get_top_scored_items(filtered_data).iloc[0]
            else:
                selected_item = pd.Series()
        
        return create_overview(selected_item, filtered_data)
    
    
    @app.callback(
        Output('top-producers-categories-row', 'children'),
        Output('notes-heatmap', 'children'),
        Input('type', 'value')
    )
    def update_top_producers_categories(type: str):
        data = load_data(type)
        
        top_producers = create_top_producers(data)
        top_categories = create_top_categories(data)
        
        return [top_producers, top_categories], create_notes_heatmap(data)