from dash import Input, Output, html, dcc, Dash
import dash_bootstrap_components as dbc
from data.loader import Loader
from components.top_picks import create_top_picks
from components.map import create_map
from components.top_producers import create_top_producers
from components.top_categories import create_top_categories
from components.tasting_notes import create_notes_bubble_chart
from components.overview import create_overview

class Callbacker:
    def __init__(self) -> None:
        self.loader = Loader()
        self.loader.load_data('Beer')
        self.loader.compute_score()
        
    def register_callbacks(self, app: Dash):
        
        @app.callback(
            Output('category', 'options'),
            Output('country', 'options', allow_duplicate=True),
            Output('taste-filter', 'options', allow_duplicate=True),
            Output('food-filter', 'options', allow_duplicate=True),
            Output('price-range', 'max', allow_duplicate=True),
            Output('price-range', 'marks', allow_duplicate=True),
            Output('price-range', 'value', allow_duplicate=True),
            Output('food-filter', 'disabled'),
            Input('type', 'value'),
            prevent_initial_call=True
        )
        def changed_drink_type(type):
            self.loader.load_data(type)
            disabled = len(self.loader.extract_unique_values("Food Pairing")) == 0
            return *self.loader.extract_options_for_sidebar(), disabled
        
        
        @app.callback(
            Output('country', 'options', allow_duplicate=True),
            Output('taste-filter', 'options', allow_duplicate=True),
            Output('food-filter', 'options', allow_duplicate=True),
            Input('category', 'value'),
            Input('country', 'value'),
            Input('taste-filter', 'value'),
            Input('food-filter', 'value'),
            Input('price-range', 'value'),
            prevent_initial_call=True
        )
        def changed_sidebar_option(category, country, taste_filter, food_filter, price_range):
            self.loader.filter_items(category, country, taste_filter, food_filter, price_range)
            return self.loader.extract_options_for_sidebar()[1:-3]
        
        @app.callback(
            Output('tab-content', 'children'),
            Output('overview', 'children', allow_duplicate=True),
            Input('tabs', 'active_tab'),
            Input('category', 'value'),
            Input('country', 'value'),
            Input('taste-filter', 'value'),
            Input('food-filter', 'value'),
            Input('price-range', 'value'),
            prevent_initial_call=True
        )
        def change_tab(active_tab, category, country, taste_filter, food_filter, price_range):
            # reapply all sidebar filters before recreating the current tab
            self.loader.filter_items(category, country, taste_filter, food_filter, price_range)
            if active_tab == "top-picks":
                return create_top_picks(self.loader.get_data()), []
            elif active_tab == "map":
                return create_map(self.loader.get_data()), []
            elif active_tab == "top-producers":
                return create_top_producers(self.loader.get_data()), []
            elif active_tab == "top-categories":
                return create_top_categories(self.loader.get_data()), []
            elif active_tab == "tasting-notes":
                return create_notes_bubble_chart(self.loader.get_data()), []
            else:
                raise ValueError(f"Unknown tab {active_tab}")
            
        
        @app.callback(
            Output('overview', 'children', allow_duplicate=True),
            Input('top-picks-table', 'selected_rows'),
            prevent_initial_call=True
        )
        def select_row(selected_rows):
            # if nothing is selected, clear the overview
            if not selected_rows:
                return []
            return create_overview(selected_rows, self.loader.get_data())