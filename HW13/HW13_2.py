#Задача 2: Создать гистограмму с расширенными возможностями настройки. 

import plotly.express as px

tips = px.data.tips()
#print(tips.head())

fig = px.histogram(
      tips,
      x ='day',
      y = 'total_bill',
      color = 'day',
      category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']},
      nbins=20,
      title = 'total_bill by days'   
  )
fig.show()