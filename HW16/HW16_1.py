mean_sales = 500
std_sales = 50
value_sales = 550

mean_satisfaction = 80
std_satisfaction = 10
value_satisfaction = 85

mean_punctuality = 95
std_punctuality = 5
value_punctuality = 90

z_sales = (value_sales - mean_sales) / std_sales
z_satisfaction = (value_satisfaction - mean_satisfaction) / std_satisfaction
z_punctuality = (value_punctuality - mean_punctuality) / std_punctuality

print(f"z_sales: {z_sales}")
print(f"z_satisfaction: {z_satisfaction}")
print(f"z_punctuality: {z_punctuality}")

z_scores = {
    "sales": z_sales,
    "satisfaction": z_satisfaction,
    "punctuality": z_punctuality
}

best_metric = max(z_scores, key=z_scores.get)
print(f"best_metric: {best_metric}")
