from yahooquery import Ticker
#import pandas as pd

ticker = "ABEV3.SA"

petr = Ticker(ticker)
df = petr.history(period='60d',  interval = "5m")
df.reset_index(inplace=True)
df.to_csv(r"..\ml-financial-market\data\external\stock_dataframe.csv")