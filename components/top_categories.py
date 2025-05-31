from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def create_top_categories(data: pd.DataFrame):
    # bar chart of top categories by number of dataset entries
    df = data.copy()
    df['Categories'] = df['Categories'].str.split(',')
    df = df.explode('Categories')
    df['Categories'] = df['Categories'].astype(str).str.strip()
    df = df[df['Categories'] != '']
    top_categories = df['Categories'].value_counts().head(10).reset_index()
    top_categories.columns = ['Category', 'Count']
    top_categories = top_categories.sort_values(by='Count', ascending=False)
    return dbc.Col(
        [
            html.H3("Top Categories", className="fs-italic"),
            html.P("This chart shows the top 10 categories by the number of entries in the dataset."),
            html.Hr(),
            dcc.Graph(
                id='top-categories-bar-chart',
                figure={
                    'data': [
                        {
                            'x': top_categories['Category'],
                            'y': top_categories['Count'],
                            'type': 'bar',
                            'name': 'Categories',
                            'marker': {'color': '#0dcaf0'}
                        }
                    ],
                    'layout': {
                        'title': 'Top 10 Categories by Number of Entries',
                        'xaxis': {
                            'title': '',
                            'showticklabels': False
                        },
                        'yaxis': {'title': 'Number of Entries'},
                        'plot_bgcolor': 'rgba(0,0,0,0)',
                        'paper_bgcolor': 'rgba(0,0,0,0)'
                    }
                }
            )
        ],
        className="bg-light border rounded m-3 p-3"
    )