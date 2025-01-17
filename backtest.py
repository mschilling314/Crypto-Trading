import backtesting
import pandas as pd

from strategies.SimpleMovingAverage import SimpleMovingAverageStrategy
from strategies.ExponentialMovingAverage import ExponentialMovingAverageStrategy
from strategies.Grid import GridStrategy
from strategies.MACD import MACDStrategy


def scale(df, scaler=0.000001):
    els = ["Open", "Close", "High", "Low", "Volume"]
    for el in els:
        df[el] *= scaler
    return df


data = scale(pd.read_csv("data/BTC-USD.csv"))
backtest = backtesting.Backtest(data, MACDStrategy)
results = backtest.run()

results.to_csv("results/BTC-USD.csv")