import backtesting
import pandas as pd

from strategies.SimpleMovingAverage import SimpleMovingAverageStrategy


def scale(df, scaler=0.000001):
    els = ["Open", "Close", "High", "Low", "Dividends", "Volume"]
    for el in els:
        df[el] *= scaler
    return df


data = scale(pd.read_csv("data/BTC-USD.csv"))
backtest = backtesting.Backtest(data, SimpleMovingAverageStrategy)
results = backtest.run()

results.to_csv("results/BTC-USD.csv")