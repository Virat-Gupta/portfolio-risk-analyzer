import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    if data.empty:
        raise ValueError("No data fetched. Please check tickers and date range.")
    # Use 'Close' instead of 'Adj Close' due to yfinance auto_adjust=True
    if isinstance(data.columns, pd.MultiIndex):
        close = data['Close']
    else:
        close = data['Close']
    return close

def preprocess_data(data):
    returns = data.pct_change().dropna()
    return returns