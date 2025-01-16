import backtrader as bt


class SimpleMovingAverageStrategy(bt.Strategy):


    def __init__(self):
        self.short_sma = bt.indicators.MovingAverageSimple(self.data.Close, period=5)
        self.long_sma = bt.indicators.MovingAverageSimple(self.data.Close, period=20)


    def next(self):
        if self.short_sma > self.long_sma and not self.position:
            self.buy()

        if self.short_sma < self.long_sma and self.position:
            self.sell()