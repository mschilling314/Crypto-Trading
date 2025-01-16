import backtrader as bt

from SimpleMovingAverage import SimpleMovingAverageStrategy


data = bt.feeds.GenericCSVData(dataname="data/BTC-USD.csv", dtformat="%Y-%m-%d")


cerebro = bt.Cerebro()
cerebro.adddata(data)
print(f"Data added.\n")
cerebro.addstrategy(SimpleMovingAverageStrategy)
print(f"Strategy added, starting backtest.\n")
cerebro.run()
print(f"Backtest complete, plotting.\n")

cerebro.plot()