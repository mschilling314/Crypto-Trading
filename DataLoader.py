import yfinance as yf
import os
import pandas as pd


class DataLoader():
    # TODO: extend so that it can deal with different starts/ends/intervals without ALWAYS reloading?

    def __init__(self, ticker: str="BTC-USD", start: str="2024-12-21", end: str="2025-01-16", interval: str="1m") -> None:
        self.ticker = ticker
        self.start = start
        self.end = end
        self.interval = interval


        filename = f"{self.ticker}.csv"
        self.pathname = os.path.join(".", "data", filename)


    def fetch(self) -> pd.DataFrame:
        yf_ticker = yf.Ticker(ticker=self.ticker)
        data = yf_ticker.history(start = self.start, end = self.end, interval = self.interval)
        data["Datetime"] = data.index.tz_localize(None)
        data.reset_index(drop=True)
        return data


    def load(self) -> pd.DataFrame:
        if os.path.exists(self.pathname):
            self.data = pd.read_csv(self.pathname)
        else:
            self.data = self.fetch()
            self.write()
        return self.data
        

    def write(self):
        self.data.to_csv(self.pathname)
        

if __name__=="__main__":
    loader = DataLoader()
    data = loader.load()
    