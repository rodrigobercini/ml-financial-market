from yahooquery import Ticker
#import pandas as pd

def make_dataset(ticker = 'ABEV3.SA', period='1y', interval='1d'):
    ticker_data = Ticker(ticker)
    df = ticker_data.history(period=period,  interval = interval)
    df.reset_index(inplace=True)
    df.to_csv(r"..\ml-financial-market\data\external\stock_dataframe.csv")

make_dataset()