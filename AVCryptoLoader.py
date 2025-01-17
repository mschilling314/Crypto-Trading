import os
import requests
import pandas as pd

params = {"function": "CRYPTO_INTRADAY", "symbol": "BTC", "market": "USD", "interval": "1min", "apikey": os.environ["ALPHA_VANTAGE_API_KEY"]}
url = "https://www.alphavantage.co/query"
resp = requests.get(url=url, params=params)
df = pd.DataFrame(resp.json()["Time Series Crypto (1min)"]).transpose()
df.columns = ["Open", "High", "Low", "Close", "Volume"]
df.to_csv("data/BTC-USD.csv")