from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

def create_top_categories(data: pd.DataFrame):

    df = data.copy()
    df['Categories'] = df['Categories'].str.split(',')
    df = df.explode('Categories')
    df['Categories'] = df['Categories'].astype(str).str.strip()
    df = df[df['Categories'] != '']
    top_categories = df['Categories'].value_counts().head(10).reset_index()
    top_categories.columns = ['Category', 'Count']
    top_categories = top_categories.sort_values(by='Count', ascending=False)

    colors = px.colors.sequential.Blues_r[2:]

    return dbc.Row(
        [
            dcc.Graph(
                id='top-categories-bar-chart',
                figure={
                    'data': [
                        {
                            'x': top_categories['Category'],
                            'y': top_categories['Count'],
                            'type': 'bar',
                            'marker': {
                                'color': colors,
                            },
                            'hovertemplate': 'Category: %{x}<br>Count: %{y}<extra></extra>'
                        }
                    ],
                    'layout': {
                        'height': 500,
                        'xaxis': {
                            'title': '',
                            'tickmode': 'array',
                            'tickvals': top_categories['Category'],
                            'ticktext': top_categories['Category'],
                            'tickangle': -60
                        },
                        'yaxis': {'title': 'Number of Entries'},
                        'plot_bgcolor': '#f8f9fa',
                        'paper_bgcolor': '#f8f9fa',
                        'margin': {'t': 100, 'b': 200, 'l': 60, 'r': 40},
                    }
                },
                config={'displayModeBar': False,
                        'staticPlot': True}
            )
        ],
        className="m-2"
    )