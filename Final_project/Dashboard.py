import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px

# Загружаем данные
deals_data = pd.read_excel('Deals1.xlsx')
spend_data = pd.read_excel('Spend.xlsx')

# 1. Фильтруем успешные сделки (Stage == 'Payment Done')
successful_deals = deals_data[deals_data['Stage'] == 'Payment Done']

# 2. Объединяем успешные сделки с данными по расходам на рекламу
successful_deals_with_spend = pd.merge(successful_deals, spend_data, left_on='Source', right_on='Source', how='left')

# 3. Группируем по рекламным каналам
ad_performance = successful_deals_with_spend.groupby('Source').agg(
    total_successful_deals=('Id', 'count'),
    total_spend=('Spend', 'sum'),
    average_deal_value=('Offer Total Amount', 'mean')
).reset_index()

# 4. Рассчитываем CAC (стоимость привлечения клиента)
ad_performance['CAC_per_source'] = ad_performance['total_spend'] / ad_performance['total_successful_deals']

# Юнит-экономика (расчеты):
total_revenue = ad_performance['average_deal_value'].sum()
total_customers = ad_performance['total_successful_deals'].sum()
total_spend = ad_performance['total_spend'].sum()
arpu = total_revenue / total_customers
cac = total_spend / total_customers
ltv = arpu  # Предполагаем LTV равным ARPU для упрощения

# Дерево метрик с описаниями для всплывающих подсказок
hierarchy_labels = [
    "Business Metrics", "ARPU (Средний доход на пользователя)", "CAC (Стоимость привлечения клиента)", "LTV (Жизненная ценность клиента)", 
    "Revenue (Общая выручка)", "Customers (Число клиентов)", "Spend (Затраты)", "New Customers (Новые клиенты)", "Retention (Удержание клиентов)"
]
parents = [
    "", "Business Metrics", "Business Metrics", "Business Metrics", 
    "ARPU (Средний доход на пользователя)", "ARPU (Средний доход на пользователя)", 
    "CAC (Стоимость привлечения клиента)", "CAC (Стоимость привлечения клиента)", "LTV (Жизненная ценность клиента)"
]
values = [10, 4, 3, 3, 5, 5, 5, 2, 3]

# Добавим текст подсказок о влиянии каждой метрики на бизнес
hover_text = {
    "Business Metrics": "Основные метрики бизнеса, которые влияют на прибыльность.",
    "ARPU (Средний доход на пользователя)": "Повышение ARPU увеличивает доход с каждого клиента, повышая прибыльность.",
    "CAC (Стоимость привлечения клиента)": "Снижение CAC снижает расходы на привлечение клиентов, повышая общую прибыль.",
    "LTV (Жизненная ценность клиента)": "Увеличение LTV означает, что клиент приносит больше дохода на протяжении его жизненного цикла.",
    "Revenue (Общая выручка)": "Общая выручка напрямую влияет на прибыль компании.",
    "Customers (Число клиентов)": "Увеличение числа клиентов приводит к росту выручки и бизнеса.",
    "Spend (Затраты)": "Затраты на привлечение клиентов. Высокие затраты могут снизить прибыль.",
    "New Customers (Новые клиенты)": "Привлечение новых клиентов помогает увеличить доходы и развивать бизнес.",
    "Retention (Удержание клиентов)": "Удержание клиентов увеличивает LTV и снижает зависимость от привлечения новых клиентов."
}

# Создаем интерактивный график Sunburst (иерархия метрик)
fig = px.sunburst(
    names=hierarchy_labels,
    parents=parents,
    values=values,
    hover_name=hierarchy_labels,
    hover_data={'hoverinfo': [hover_text[label] for label in hierarchy_labels]},
    color_discrete_map={'ARPU (Средний доход на пользователя)': 'green', 'CAC (Стоимость привлечения клиента)': 'green', 'LTV (Жизненная ценность клиента)': 'lightblue', 'Revenue (Общая выручка)': 'lightgray', 'Customers (Число клиентов)': 'lightgray', 'Spend (Затраты)': 'lightgray', 'New Customers (Новые клиенты)': 'lightgray', 'Retention (Удержание клиентов)': 'lightgray'}
)

# Создаем дашборд с помощью Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Аналитика рекламы: Юнит-экономика и точки роста", style={'text-align': 'center'}),
    
    # Выбор метрики
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Total Successful Deals', 'value': 'total_successful_deals'},
            {'label': 'Total Spend', 'value': 'total_spend'},
            {'label': 'CAC per Source', 'value': 'CAC_per_source'}
        ],
        value='total_successful_deals',
        clearable=False,
        style={'width': '50%', 'margin': 'auto'}
    ),

    # График с метриками
    dcc.Graph(id='combined-chart'),

    # Юнит-экономика (визуализация)
    html.Div([
        html.H3("Юнит-экономика по продуктам", style={'text-align': 'center'}),
        html.Div(f"Средний доход на пользователя (ARPU): {arpu:.2f}"),
        html.Div(f"Стоимость привлечения клиента (CAC): {cac:.2f}"),
        html.Div(f"Средний жизненный цикл клиента (LTV): {ltv:.2f}"),
        html.Div("**Точки роста бизнеса**: Увеличение вложений в Facebook Ads и оптимизация креативов в Google Ads приведет к росту ARPU и снижению CAC.")
    ], style={'text-align': 'center', 'margin-top': '30px'}),

    # Иерархия метрик (Sunburst Graph)
    html.Div([
        html.H3("Иерархическое дерево метрик бизнеса с подсветкой точек роста", style={'text-align': 'center'}),
        dcc.Graph(figure=fig)
    ], style={'margin-top': '30px'}),

    # Гипотезы и решения
    html.Div([
        html.H3("Гипотезы и решения", style={'text-align': 'center'}),
        html.Div([
            html.P("1. Оптимизация таргетинга в Facebook Ads увеличит конверсию на 10%, снизив CAC."),
            html.P("2. Улучшение креативов для Google Ads приведет к снижению CPA на 15%."),
            html.P("3. Перераспределение бюджета от менее эффективных каналов (CRM, Webinar) к более успешным (Facebook Ads, Google Ads) увеличит общую маржу.")
        ], style={'text-align': 'center'})
    ], style={'margin-top': '30px'}),
    
    # Выводы и рекомендации
    html.Div([
        html.H3("Выводы и рекомендации", style={'text-align': 'center'}),
        html.P("Рекомендуется оптимизировать вложения в наиболее эффективные рекламные каналы, такие как Facebook Ads и Google Ads, для увеличения ARPU и снижения CAC."),
        html.P("Необходимо провести A/B тестирование для проверки гипотез по оптимизации креативов и таргетинга в этих каналах.")
    ], style={'text-align': 'center', 'margin-top': '20px'})
])

# Callback для обновления графика
@app.callback(
    Output('combined-chart', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_dashboard(selected_metric):
    # Столбчатый график для метрики
    bar_fig = go.Bar(x=ad_performance['Source'], y=ad_performance[selected_metric], name=selected_metric)

    # Линейный график для общего spend
    line_fig = go.Scatter(x=ad_performance['Source'], y=ad_performance['total_spend'], 
                          mode='lines+markers', name='Total Spend', yaxis='y2')

    # Объединенный график (двойная ось)
    fig = go.Figure([bar_fig, line_fig])
    fig.update_layout(
        title=f'{selected_metric} и Total Spend по рекламным источникам',
        xaxis_title='Source',
        yaxis_title=selected_metric,
        yaxis2=dict(title='Total Spend', overlaying='y', side='right'),
        legend=dict(x=0, y=-0.2, orientation="h"),
        height=600
    )

    return fig

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)




