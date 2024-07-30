#Задача 4: Создать тепловую карту для визуализации корреляции между 
# несколькими переменными с помощью интерактивных функций. 

import plotly.express as px

iris = px.data.iris()
#print(iris.head())
selected_columns = ['sepal_width', 'sepal_length']
numeric_iris = iris[selected_columns]

corr_matrix = numeric_iris.corr()
#print (corr_matrix)
 
fig = px.imshow(
     corr_matrix, 
     text_auto=True,  
     title='Correlation Heatmap of Iris Dataset',
     labels=dict(x='sepal_length', y='sepal_width') 
 )
fig.show()