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
            showscale=True
        )
    )

    fig.update_layout(
        xaxis=dict(title='', tickangle=45),
        yaxis=dict(title=''),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=300
    )

    return dbc.Col(
        [
            html.H3("Tasting Notes Heatmap", className="fs-italic"),
            html.P("This heatmap shows the top 20 tasting notes by the number of entries in the dataset."),
            html.Hr(),
            dcc.Graph(figure=fig)
        ],
        className="bg-light border rounded m-3 p-3"
    )
