import backtesting as bt
import pandas as pd

class MACDStrategy(bt.Strategy):
    def init(self):
        self.short_ema = self.I(self.EMA, self.data.Close, 12)
        self.long_ema = self.I(self.EMA, self.data.Close, 26)
        self.macd_line = self.I(self.sub, self.long_ema, self.short_ema)
        self.signal_line = self.I(self.EMA, self.macd_line, 9)


    def next(self):
        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2]:
            self.buy()
        if self.short_ema[-1] < self.long_ema[-1]  and self.short_ema[-2] >= self.long_ema[-2]:
            self.sell()


    def EMA(self, series, period):
        pd_series = pd.Series(series)
        return pd_series.ewm(span=period).mean()
    

    def sub(self, series1, series2):
        return series1 - series2