from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def create_top_producers(data: pd.DataFrame):
    # bar chart of top producers by number of dataset entries
    top_producers = data['Brand'].value_counts().head(10).reset_index()
    top_producers.columns = ['Producer', 'Count']
    top_producers = top_producers.sort_values(by='Count', ascending=False)
    return dbc.Col(
        [
            html.H3("Top Producers", className="fs-italic"),
            html.P("This chart shows the top 10 producers by the number of entries in the dataset."),
            html.Hr(),
            dcc.Graph(
                id='top-producers-bar-chart',
                figure={
                    'data': [
                        {
                            'x': top_producers['Producer'],
                            'y': top_producers['Count'],
                            'type': 'bar',
                            'name': 'Producers',
                            'marker': {'color': '#0dcaf0'}
                        }
                    ],
                    'layout': {
                        'title': 'Top 10 Producers by Number of Entries',
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