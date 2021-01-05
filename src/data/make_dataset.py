from yahooquery import Ticker

def make_dataset(ticker, period, interval):
    ticker_data = Ticker(ticker)
    df = ticker_data.history(period=period,  interval = interval)
    df.reset_index(inplace=True)
    df.to_csv(r"..\ml-financial-market\data\external\stock_dataframe.csv")
    return df

if __name__ == '__main__':
    make_dataset(ticker = 'PETR4.SA', period = '2y', interval = '60m')