from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

header = html.Header(html.H1('My Dashboard', className='header-title'))

sidebar = html.Div([
    html.H2('Navigation', className='sidebar-title'),
    html.Ul([
        html.Li(html.A('Главная', href='/')),
        html.Li(html.A('Страница 1', href='/page-1')),
        html.Li(html.A('Страница 2', href='/page-2'))
    ])
], className='sidebar')

main_content = html.Section([
    html.Article([
        html.H3('Заголовок основного контента'),
        html.P('Некоторые важные материалы или визуализации данных находятся здесь.')
    ], className='main-article')
], className='main-content')
footer = html.Footer([
    html.P('Copyright (c) 2024 My Dashboard'),
    html.P('Больше информации здесь')
], className='footer')

graph_component = dcc.Graph(
    id='example-graph',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type':'bar', 'name':'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type':'bar', 'name':'Montréal'}
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
)

dropdown_component = dcc.Dropdown(
    id='my-dropdown',
    options=[
        {'label': 'San Francisco', 'value': 'SF'},
        {'label': 'Montreal', 'value': 'MTL'}
    ],
    value='SF'
)

slider_component = dcc.Slider(
    min=0,
    max=20,
    step=0.5,
    value=10,
    marks={i: str(i) for i in range(21)}
)

app.layout = html.Div([
    header,
    sidebar,
    main_content,
    footer,
    graph_component,
    dropdown_component,
    slider_component
], className='dashboard-container')

if __name__ == '__main__':
    app.run_server(debug=True)
app.run_server(debug=True)

