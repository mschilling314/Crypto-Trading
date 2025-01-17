import backtesting as bt
import pandas as pd

class ExponentialMovingAverageStrategy(bt.Strategy):
    def init(self):
        self.short_ema = self.I(self.EMA, self.data.Close, 3)
        self.long_ema = self.I(self.EMA, self.data.Close, 20)


    def next(self):
        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2]:
            self.buy()
        if self.short_ema[-1] < self.long_ema[-1]  and self.short_ema[-2] >= self.long_ema[-2]:
            self.sell()


    def EMA(self, series, period):
        pd_series = pd.Series(series)
        return pd_series.ewm(span=period).mean()