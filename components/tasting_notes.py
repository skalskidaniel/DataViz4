from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

def create_notes_heatmap(data: pd.DataFrame):
    df = data.copy()
    df['Tasting Notes'] = df['Tasting Notes'].str.split(',')
    df = df.explode('Tasting Notes')
    df['Tasting Notes'] = df['Tasting Notes'].astype(str).str.strip()
    df = df[df['Tasting Notes'] != '']
    df = df[df['Tasting Notes'] != 'nan']

    top_notes = df['Tasting Notes'].value_counts().head(20).reset_index()
    top_notes.columns = ['Tasting Note', 'Count']
    top_notes = top_notes.sort_values(by='Count', ascending=False)

    fig = go.Figure(
        data=go.Heatmap(
            z=[top_notes['Count'].tolist()],
            x=top_notes['Tasting Note'],
            y=['Frequency'],
            colorscale='Blues',
            showscale=True,
            hovertemplate='Tasting Note: %{x}<br>Count: %{z}<extra></extra>'
        )
    )

    fig.update_layout(
        xaxis=dict(title='', tickangle=-60),
        yaxis=dict(title=''),
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa',
        height=400
    )

    return dbc.Row(
        [
            html.H3("Tasting Notes"),
            html.Hr(),
            dcc.Graph(figure=fig,
                      config={'displayModeBar': False})
        ],
        className="bg-light border rounded m-3 p-3"
    )
