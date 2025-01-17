import backtesting as bt
import pandas as pd

from backtesting.test import SMA


class SimpleMovingAverageStrategy(bt.Strategy):


    def init(self):
        self.short_sma = self.I(SMA, self.data.Close, 1)
        self.long_sma = self.I(SMA, self.data.Close, 3)


    def next(self):
        if self.short_sma[-1] > self.long_sma[-1] and self.short_sma[-2] <= self.long_sma[-2]:
            self.buy()

        if self.short_sma[-1] < self.long_sma[-1] and self.short_sma[-2] >= self.long_sma[-2]:
            self.sell()