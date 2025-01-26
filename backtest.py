import backtesting as bt
import pandas as pd

from strategies.SimpleMovingAverage import SimpleMovingAverageStrategy
from strategies.ExponentialMovingAverage import ExponentialMovingAverageStrategy
from strategies.Grid import GridStrategy
from strategies.MACD import MACDStrategy
from strategies.VWAP import VWAPStrategy


def scale(df, scaler=0.000001):
    els = ["Open", "Close", "High", "Low", "Volume"]
    for el in els:
        df[el] *= scaler
    return df


def do_backtest(strat: bt.Strategy):
    data = scale(pd.read_csv("data/BTC-USD.csv"))
    backtest = bt.Backtest(data, strat)
    results = backtest.run()

    results.to_csv(f"results/BTC-USD-{strat}.csv")


if __name__=="__main__":
    strats = [SimpleMovingAverageStrategy, ExponentialMovingAverageStrategy, GridStrategy, MACDStrategy]
    for strat in strats:
        do_backtest(strat=strat)


