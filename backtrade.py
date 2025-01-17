import backtrader as bt

from strategies.SimpleMovingAverage import SimpleMovingAverageStrategy
from DataLoader import DataLoader


# data = bt.feeds.GenericCSVData(dataname="data/BTC-USD.csv", dtformat="%Y-%m-%d")
loader = DataLoader()
df = loader.load()
data = bt.feeds.PandasData(dataname=df)


cerebro = bt.Cerebro()
cerebro.adddata(data)
print(f"Data added.\n")
cerebro.addstrategy(SimpleMovingAverageStrategy)
print(f"Strategy added, starting backtest.\n")
results = cerebro.run()
print(f"Backtest complete, plotting.\n")

cerebro.plot()