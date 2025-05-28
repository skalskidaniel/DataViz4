from dash import Input, Output, Dash
from data.loader import extract_unique_values, load_data

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
    
    #TODO add main table callbacks