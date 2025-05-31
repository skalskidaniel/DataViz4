from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_map(data: pd.DataFrame):
    
    country_counts = data['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Producer_Count']
    
    fig = px.choropleth(
        country_counts,
        locations='Country',
        color='Producer_Count',
        locationmode='country names',
        color_continuous_scale='Blues',
        title='Number of Producers by Country',
        labels={'Producer_Count': 'Number of Producers'},
        hover_data={'Country': True, 'Producer_Count': True}
    )
    
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
        title_x=0.5,
        height=500,
        margin=dict(l=0, r=0, t=50, b=0)
    )
    
    return dbc.Row([
        html.H3("Map of producers"),
        html.Hr(),
        dcc.Graph(figure=fig, config={'displayModeBar': False})
    ], className="bg-light border rounded m-3 p-3")