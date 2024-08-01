import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
        dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': continent, 'value': continent} for continent in df['continent'].unique()],
        value=df['continent'].unique()[0],
        clearable=False
    ),
    dcc.Graph(id='life-exp-histogram')
])

@app.callback(
    Output('life-exp-histogram', 'figure'),
    [Input('continent-dropdown', 'value')]
)
def update_histogram(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]

    
    fig = px.histogram(
        filtered_df,
        x='lifeExp',
        title=f'Distribution of life expectancy in {selected_continent}',
        labels={'lifeExp': 'Life expectancy'}
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
