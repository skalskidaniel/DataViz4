from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import circlify 

def create_notes_bubble_chart(data: pd.DataFrame):
    df = data.copy()
    if 'Tasting Notes' not in df.columns:
        return dbc.Row(
            [html.H3("Tasting Notes"), html.Hr(), html.P("No tasting notes data available.")],
            className="bg-light border rounded m-3 p-3"
        )

    df['Tasting Notes'] = df['Tasting Notes'].astype(str).str.split(',')
    df = df.explode('Tasting Notes')
    df['Tasting Notes'] = df['Tasting Notes'].str.strip()
    df = df[df['Tasting Notes'].str.lower().isin(['', 'nan']) == False]
    
    if df.empty or df['Tasting Notes'].nunique() == 0:
        return dbc.Row(
            [html.H3("Tasting Notes"), html.Hr(), html.P("Not enough data for tasting notes chart.")],
            className="bg-light border rounded m-3 p-3"
        )

    top_notes = df['Tasting Notes'].value_counts().nlargest(25).reset_index()
    top_notes.columns = ['Tasting Note', 'Count']

    data_for_packing = [{'id': row['Tasting Note'], 'datum': row['Count']} for index, row in top_notes.iterrows()]
    try:
        circles = circlify.circlify(
            data_for_packing, 
            show_enclosure=False,
            target_enclosure=circlify.Circle(x=0, y=0, r=1)
        )
    except Exception as e:
         return dbc.Row(
            [html.H3("Tasting Notes"), html.Hr(), html.P(f"Error generating bubble chart: {e}")],
            className="bg-light border rounded m-3 p-3"
        )


    x_coords = [c.x for c in circles]
    y_coords = [c.y for c in circles]
    radii = [c.r for c in circles]
    labels = [c.ex['id'] for c in circles] 
    counts = [c.ex['datum'] for c in circles] 

    if not radii: 
        scaled_diameters = []
    else:
        max_r_val = max(radii) if radii else 1
        pixel_scale_factor = 300 
        scaled_diameters = [r * 2 * pixel_scale_factor for r in radii]


    bubble_texts = [f"{label}<br>Count: {count}" for label, count in zip(labels, counts)]

    # Create a better color palette - using darker blues and lighter blues for contrast
    blues_palette = ['#08519c', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#1565c0', '#1976d2']
    
    # Map colors based on bubble size (larger bubbles get darker colors)
    sorted_indices = sorted(range(len(counts)), key=lambda i: counts[i], reverse=True)
    bubble_colors = ['#f0f0f0'] * len(labels)  # default light color
    
    for i, idx in enumerate(sorted_indices):
        color_idx = i % len(blues_palette)
        bubble_colors[idx] = blues_palette[color_idx]

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_coords,
                y=y_coords,
                mode='markers+text',
                marker=dict(
                    size=scaled_diameters, 
                    sizemode='diameter',
                    color=bubble_colors,
                    opacity=0.8,
                    line=dict(width=1, color='#2c3e50') 
                ),
                text=[label for label in labels],  # Show only label names
                textposition="middle center",
                textfont=dict(
                    color='#2c3e50',  # Dark text for better visibility
                    size=10,
                    family="Arial Black",
                    weight='normal'
                ),
                hovertemplate='<b>%{text}</b><br>Count: %{customdata}<extra></extra>',
                customdata=counts,
                hoverinfo='text'
            )
        ]
    )

    fig.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, visible=False, range=[-1.1, 1.1]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, visible=False, range=[-1.1, 1.1]), 
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa',
        height=500,
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=False,
        uniformtext_minsize=8,
        uniformtext_mode='show'
    )

    return dbc.Row(
        [
            dcc.Graph(id='tasting-notes-bubble-chart', figure=fig, config={'displayModeBar': False})
        ],
        className="m-2"
    )