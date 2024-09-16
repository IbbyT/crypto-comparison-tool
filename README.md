# Cryptocurrency Price Comparison

This Python script compares the historical prices of various cryptocurrencies. It retrieves price data, fills missing values, plots the data, calculates daily returns, and generates a correlation matrix heatmap.

## Features

- **Download Historical Data:** Retrieves historical price data for multiple cryptocurrencies using `yfinance`.
- **Handle Missing Data:** Fills missing values with forward fill.
- **Plot Prices:** Visualizes the price trends of cryptocurrencies on a logarithmic scale.
- **Calculate Daily Returns:** Computes daily percentage returns for each cryptocurrency.
- **Correlation Analysis:** Generates and visualizes a correlation matrix of daily returns.

## Requirements

- Python 3.x
- `yfinance`
- `matplotlib`
- `pandas`
- `datetime`
- `seaborn`

You can install the required packages using pip:

```bash
pip install yfinance matplotlib pandas seaborn
```

## Usage
1. Run the script:
   ```bash
   python compare_crypto_prices.py
2. Paremeters:
- currency: Currency for price representation (default is "USD").
- metric: Price metric to use (default is "Close").
- start: Start date for historical data (default is January 1, 2018).
- end: End date for historical data (default is the current date).
- crypto: List of cryptocurrency tickers to compare (default includes 'BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD', 'DASH-USD', 'SC-USD').

3. Output:
- Price Plot: A plot showing the price trends of selected cryptocurrencies over time.
- Daily Returns: Prints the daily percentage returns for each cryptocurrency.
- Correlation Matrix: Prints and visualizes the correlation matrix of daily returns.

## Code Overview
- Download Data: Uses yfinance to download historical price data for each cryptocurrency.
- Missing Data: Checks for and fills missing data using forward fill.
- Plot Prices: Plots the historical prices on a logarithmic scale for better visualization of price trends.
- Calculate Returns: Computes daily percentage returns and prints the first few rows.
- Correlation Matrix: Calculates and visualizes the correlation between daily returns of different cryptocurrencies.
