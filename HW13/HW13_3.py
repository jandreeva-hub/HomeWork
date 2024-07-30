#Задача 3: Создайте линейный график с несколькими линиями для сравнения тенденций. 

import plotly.express as px

gapminder = px.data.gapminder()
#print(gapminder.head())
#print(gapminder['country'].unique())
filtered_gapminder = gapminder[gapminder['country'].isin(['Canada', 'Germany'])]


fig = px.line(
      filtered_gapminder, 
      x='year', 
      y='gdpPercap', 
      color='country',  
      line_dash='country',
      title='gdpPercap by years'
  )
fig.show()