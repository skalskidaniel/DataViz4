from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def create_map(data: pd.DataFrame):
    
    data = data.copy()
    data['Price_num'] = (
        data['Price']
        .astype(str)
        .str.replace(r'[\$,]', '', regex=True)
        .astype(float, errors='ignore')
    )
    
    countries = (
        data
        .groupby('Country')
        .agg(
            Count=('Name','count'),
            Avg_Rating=('Rating','mean'),
            Avg_Price=('Price_num','mean')
        )
        .reset_index()
    )
    countries['Count_log'] = np.log1p(countries['Count'])
    
    
    fig = px.choropleth(
        countries,
        locations='Country',
        color='Count_log',
        locationmode='country names',
        color_continuous_scale=px.colors.sequential.Blues, 
        labels={'Count_log': 'Number of products (Log scale)'},
        hover_data={
            'Count': True,
            'Avg_Rating':':.2f',
            'Avg_Price':':.2f'
        },
        custom_data=['Count', 'Avg_Rating', 'Avg_Price']
    )
    
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        showland=True,
        landcolor="#f8f9fa",
        resolution=50,
        fitbounds='locations',
        scope='world',
        bgcolor="#f8f9fa"
    )
    
    fig.update_traces(
        hovertemplate=(
            '<b>%{location}</b><br>'
            'Number of products: %{customdata[0]}<br>'
            'Mean rating: %{customdata[1]:.2f}<br>'
            'Mean price: %{customdata[2]:.2f}<br>'
            '<extra></extra>'
        )
    )
    
    fig.update_layout(
        geo=dict(projection_type='robinson'),
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#f8f9fa",
        autosize=True,
        coloraxis_colorbar=dict(
            title="Product Count (logarithmic scale)",
            orientation='h',           
            x=0.5,                     
            xanchor='center',
            y=-0.02,                      
            yanchor='top',
            thickness=15,
            len=0.5,
            tickvals=[1, 9],
            ticktext=['1', '9']
        )
    )
    
    return dbc.Row([
        html.H3("Map of producers", style={"color": "#2c3e50", "fontWeight": "bold"}),
        html.Hr(className="mb-3"),
        dcc.Graph(figure=fig, 
                  style={"width": "100vw", "height": "90vh"},
                  config={
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'lasso2d', 'toImage'],
                        'scrollZoom': False
                    }
                 )
    ], className="bg-light border rounded m-2 p-3")