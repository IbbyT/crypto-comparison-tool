#comparing crypto prices
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

#parameters
currency = "USD"
metric = "Close"
start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()
crypto = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD', 'DASH-USD', 'SC-USD']

#initialize empty DataFrame
combined = pd.DataFrame()

#Download data
for ticker in crypto:
    try:
        data = yf.download(ticker, start=start, end=end)
        combined[ticker] = data[metric]
    except Exception as e:
        print(f"Error downloading {ticker}: {e}")

#missing data check
if combined.isnull().values.any():
    print("Warning: Missing data detected. Filling missing values with forward fill.")
    combined.fillna(method='ffill', inplace=True)

#plot
plt.figure(figsize=(14, 7))
plt.yscale('log')

for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.title('Cryptocurrency Prices Over Time')
plt.xlabel('Date')
plt.ylabel(f'Price in {currency} (Log Scale)')
plt.legend(loc="upper left")
plt.grid(True)
plt.show()

#daily returns
returns = combined.pct_change().dropna()
print("\nDaily Returns:")
print(returns.head())

#correlation matrix
correlation = returns.corr()
print("\nCorrelation Matrix:")
print(correlation)

#correlation heatmap
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Cryptocurrency Correlation Matrix')
plt.show()