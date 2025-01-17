import yfinance as yf
import datetime


data = yf.download("BTC-USD", start= datetime.datetime(year=2025, month=1, day=8), end=datetime.datetime(year=2025, month=1, day=15), interval="1m")
data.to_csv("data/BTC-USD.csv")