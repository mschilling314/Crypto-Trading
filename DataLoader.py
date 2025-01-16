import yfinance as yf
import os
import pandas as pd


class DataLoader():
    # TODO: extend so that it can deal with different starts/ends/intervals without ALWAYS reloading?

    def __init__(self, ticker: str="BTC-USD", start: str="2020-01-01", end: str="2025-01-01", interval: str="1d") -> None:
        self.ticker = ticker
        self.start = start
        self.end = end
        self.interval = interval


        filename = f"{self.ticker}.csv"
        self.pathname = os.path.join(".", "data", filename)


    def fetch(self) -> pd.DataFrame:
        yf_ticker = yf.Ticker(ticker=self.ticker)
        data = yf_ticker.history(start = self.start, end = self.end, interval = self.interval)
        data.index = data.index.tz_localize(None)
        return data


    def load(self) -> None:
        if os.path.exists(self.pathname):
            self.data = pd.read_csv(self.pathname)
        else:
            self.data = self.fetch()
            self.write()
        

    def write(self):
        self.data.to_csv(self.pathname)
        

if __name__=="__main__":
    loader = DataLoader(start="2024-01-01", end="2024-07-01")
    data = loader.load()
    