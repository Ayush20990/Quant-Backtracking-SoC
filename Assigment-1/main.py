from data_fetch import download_historical_data
from performance import plot_data
symbol='RELIANCE.NS'
timeframe='1d'
data=download_historical_data(symbol,'2024-06-01','2024-06-18',timeframe)
print(data)
plot_data(data,symbol)