#Географический анализ
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates



Deals1 = pd.read_excel('Deals1.xlsx')
Calls = pd.read_excel('Calls (Done) (1).xlsx')
Spend = pd.read_excel('Spend (Done) (2).xlsx')


# # Initialize geolocator
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Get the geographical coordinates for each city
# def get_coordinates(city):
#     try:
#         location = geolocator.geocode(city)
#         return location.latitude, location.longitude
#     except:
#         return None, None

# # Group by city to calculate the total deals and successful deals
# city_analysis = deals_df.groupby('City').agg({
#     'Id': 'count',  # Total deals
#     'Stage': lambda x: (x == 'Payment Done').sum()  # Successful deals
# }).reset_index()

# # Calculate success rate for each city
# city_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
# city_analysis['Success Rate'] = city_analysis['Successful Deals'] / city_analysis['Total Deals']

# # Apply this function to the cities to get coordinates
# city_analysis['Latitude'] = city_analysis['City'].apply(lambda x: get_coordinates(x)[0])
# city_analysis['Longitude'] = city_analysis['City'].apply(lambda x: get_coordinates(x)[1])

# # Remove cities where coordinates could not be found
# city_analysis.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# # Create a base map
# map_ = folium.Map(location=[51.1657, 10.4515], zoom_start=6)  # Centered around Germany

# # Plot each city with bubbles sized by total deals
# for _, row in city_analysis.iterrows():
#     folium.CircleMarker(
#         location=(row['Latitude'], row['Longitude']),
#         radius=row['Total Deals'] * 0.5,  # Adjust size for better visualization
#         color='blue',
#         fill=True,
#         fill_color='blue',
#         fill_opacity=0.6,
#         popup=(f"City: {row['City']}<br>Total Deals: {row['Total Deals']}<br>Success Rate: {row['Success Rate']:.2f}")
#     ).add_to(map_)

# # Save to an HTML file and display the map
# map_.save("deals_bubble_map.html")


# from folium.plugins import HeatMap

# # Create a base map
# heatmap = folium.Map(location=[51.1657, 10.4515], zoom_start=6)  # Centered around Germany

# # Create a list of coordinates for the heatmap
# heat_data = [[row['Latitude'], row['Longitude'], row['Total Deals']] for index, row in city_analysis.iterrows()]

# # Add heatmap layer
# HeatMap(heat_data, radius=15).add_to(heatmap)

# # Save to an HTML file and display the map
# heatmap.save("deals_heatmap.html")




# # Plotting the number of deals by city
# fig, ax1 = plt.subplots(figsize=(12, 6))
# ax1.bar(Deals1['City'], Deals1['Total Deals'], color='skyblue', label='Total Deals')
# ax1.set_xlabel('City')
# ax1.set_ylabel('Total Deals')
# ax1.set_title('Number of Deals by City')
# plt.xticks(rotation=45)
# plt.show()

# # Plotting the success rate by city
# fig, ax2 = plt.subplots(figsize=(12, 6))
# ax2.bar(Deals1['City'], Deals1['Success Rate'], color='green', label='Success Rate')
# ax2.set_xlabel('City')
# ax2.set_ylabel('Success Rate')
# ax2.set_title('Success Rate by City')
# plt.xticks(rotation=45)
# plt.show()



# Group by city to calculate the total deals and successful deals
city_analysis = Deals1.groupby('City').agg({
    'Id': 'count',  # Total deals
    'Stage': lambda x: (x == 'Payment Done').sum()  # Successful deals
}).reset_index()

# Calculate success rate for each city
city_analysis.rename(columns={'Id': 'Total Deals', 'Stage': 'Successful Deals'}, inplace=True)
city_analysis['Success Rate'] = city_analysis['Successful Deals'] / city_analysis['Total Deals']

# Sort cities by the total number of deals for better visualization
city_analysis.sort_values(by='Total Deals', ascending=False, inplace=True)

# Plotting the number of deals by city
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(city_analysis['City'], city_analysis['Total Deals'], color='skyblue', label='Total Deals')
ax1.set_xlabel('City')
ax1.set_ylabel('Total Deals')
ax1.set_title('Number of Deals by City')
plt.xticks(rotation=45)
plt.show()

# Plotting the success rate by city
fig, ax2 = plt.subplots(figsize=(12, 6))
ax2.bar(city_analysis['City'], city_analysis['Success Rate'], color='green', label='Success Rate')
ax2.set_xlabel('City')
ax2.set_ylabel('Success Rate')
ax2.set_title('Success Rate by City')
plt.xticks(rotation=45)
plt.show()


