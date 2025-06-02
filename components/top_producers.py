from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

def create_top_producers(data: pd.DataFrame):

    top_producers = data['Brand'].value_counts().head(5).reset_index()
    top_producers.columns = ['Producer', 'Count']
    top_producers = top_producers.sort_values(by='Count', ascending=False)
    
    
    return dbc.Row(
        [
            html.H3("Most Popular Producers", style={"color": "#2c3e50", "fontWeight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id='top-producers-bar-chart',
                figure={
                    'data': [
                        {
                            'x': top_producers['Count'],
                            'y': top_producers['Producer'],
                            'type': 'bar',
                            'orientation': 'h',
                            'marker': {
                                'color': px.colors.sequential.Blues_r[2:],
                            }
                        }
                    ],
                    'layout': {
                        'height': 40 * len(top_producers) + 80,
                        'xaxis': {
                            'title': {'text': 'Number of Products', 'standoff': 10},
                            'showtitle': True
                        },
                        'yaxis': {
                            'title': '',
                            'tickmode': 'array',
                            'tickvals': top_producers['Producer'],
                            'ticktext': top_producers['Producer'],
                            'autorange': "reversed",
                            'ticklabelposition': 'outside'
                        },
                        'plot_bgcolor': '#f8f9fa',
                        'paper_bgcolor': '#f8f9fa',
                        'margin': {'t': 60, 'b': 60, 'l': 200, 'r': 40},
                        'hovermode': False, 
                    }
                },
                config={'displayModeBar': False,
                        'staticPlot': True}
            )
        ],
        className="bg-light border rounded m-2 p-3"
    )