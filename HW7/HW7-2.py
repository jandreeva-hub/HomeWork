import pandas
import matplotlib.pyplot as plt
import matplotlib



data = {

    'Name': ['Анна', 'Антон', 'Мария', 'Макс', 'Макс', 'Алекс', 'Антон', 'Мария', 'Макс', 'Алекс', 'Антон', 'Анна'],

     'Points': [145, 2524, 343, 4212, 5212, 6421, 745, 842, 524, 3224, 212, 1214]      

}
df = pandas.DataFrame(data)
print (df)
grouped = (df.groupby("Name").agg(["min", "max", "mean"])).round(1)
print (grouped)

ax = grouped.plot(kind="bar", y="Points", figsize=(12, 6) )
ax.set_xlabel("geymer's name")
ax.set_ylabel("point") 
ax.set_title("min, max and average points of each player") 
plt.xticks(rotation=45) 
plt.grid(True)
plt.show() 
