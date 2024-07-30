#Задание 1: Расширенная диаграмма рассеяния

import plotly.express as px
tips = px.data.tips()
#print(tips.head())
print(tips['size'].unique())
fig = px.scatter(
     tips, 
     x='total_bill', 
     y='tip', 
     color='time', 
     size='size',
     trendline='ols',
     title='total_bill vs tip relationship'
 )
fig.show()