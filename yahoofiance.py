# -------------------------------
# Python Script for Power BI
# -------------------------------

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# The dataset comes from Power BI
df = dataset  # Power BI automatically provides your table as 'dataset'
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)
df.set_index('Date', inplace=True)

# -------------------------------
# Forecast Model (ARIMA)
# -------------------------------
forecast_days = 30  # Forecast 30 days ahead
model = ARIMA(df['Close'], order=(5,1,0))  # You can adjust the ARIMA order
model_fit = model.fit()

forecast = model_fit.forecast(steps=forecast_days)
forecast_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=forecast_days)

forecast_df = pd.DataFrame({
    'Date': forecast_dates,
    'Close': forecast,
    'Type': ['Forecast'] * forecast_days
})

# -------------------------------
# Prepare Historical Data
# -------------------------------
hist_df = df.reset_index()[['Date', 'Close']]
hist_df['Type'] = 'Historical'

# -------------------------------
# Combine Historical + Forecast
# -------------------------------
final_df = pd.concat([hist_df, forecast_df], ignore_index=True)
final_df.sort_values('Date', inplace=True)
final_df.reset_index(drop=True, inplace=True)

# Output for Power BI
final_df

