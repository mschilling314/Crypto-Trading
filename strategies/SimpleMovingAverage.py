import backtesting as bt
import pandas as pd

from backtesting.test import SMA


class SimpleMovingAverageStrategy(bt.Strategy):


    def init(self):
        self.short_sma = self.I(SMA, self.data.Close, 1)
        self.long_sma = self.I(SMA, self.data.Close, 3)


    def next(self):
        if self.short_sma > self.long_sma and not self.position:
            self.buy()

        if self.short_sma < self.long_sma and self.position:
            self.sell()