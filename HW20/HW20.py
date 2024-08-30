import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

data = pd.read_csv('PRSA_Data_Aotizhongxin_20130301-20170228.csv')
print(data.columns)

data['date'] = pd.to_datetime(data[['year', 'month', 'day']])

data = data[['date', 'PM2.5']].dropna()
data.set_index('date', inplace=True)
monthly_data = data.resample('M').mean()

arima_model = ARIMA(monthly_data, order=(5, 1, 0))
arima_fit = arima_model.fit()

sarima_model = SARIMAX(monthly_data, order=(5, 1, 0), seasonal_order=(1, 1, 0, 12))
sarima_fit = sarima_model.fit()
forecast_steps = 12

arima_forecast = arima_fit.get_forecast(steps=forecast_steps).predicted_mean

sarima_forecast = sarima_fit.get_forecast(steps=forecast_steps).predicted_mean
combined_forecast = (arima_forecast + sarima_forecast) / 2
import matplotlib.pyplot as plt

forecast_index = pd.date_range(start=monthly_data.index[-1] + pd.DateOffset(months=1), periods=forecast_steps, freq='M')

plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data, label="Historical data")
plt.plot(forecast_index, combined_forecast, label="Combined forecast", color='red')
plt.title("Combined concentration forecast PM2.5")
plt.xlabel("Date")
plt.ylabel("Concentration PM2.5")
plt.legend()
plt.grid(True)
plt.show()
