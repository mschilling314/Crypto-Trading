import backtesting as bt


class GridStrategy(bt.Strategy):
    diff = 0.000000000005

    def init(self):
        self.buy_bound = self.data.Close[0] - self.diff
        self.sell_bound = self.data.Close[0] + self.diff


    def next(self):
        if self.buy_bound > self.data.Close[0] and not self.position:
            self.buy()
            self.sell_bound = self.data.Close[0] + self.diff
        if self.sell_bound < self.data.Close[0] and self.position:
            self.sell()
            self.buy_bound = self.data.Close[0] - self.diff