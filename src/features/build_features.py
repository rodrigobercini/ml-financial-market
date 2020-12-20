import pandas as pd

def load_data():
# Feature engineering
    data = pd.read_csv(r'..\ml-financial-market\data\external\stock_dataframe.csv')

    data.index = data.date
    df = data[['close', 'volume']]
    return df

def column_shifter(n_shift, df, column):
    for i in range(1, n_shift):
        df[f'{column}_minus{i}'] = df[column].shift(i)

def data_wrangle(df, positive_variation):
    for column in ['close', 'volume']: column_shifter(30, df, column)

    df.dropna(inplace=True)

    # Creating column to check if the stock price rose in the following X periods
    df['Rise'] = 1
    periods_ahead = 30
    positive_variation = positive_variation

    df['Rise']  = (df['close'].iloc[::-1].rolling(periods_ahead).max() / df['close']).gt(positive_variation).astype(int)

    return df

def save_data(df,testing_period):
    df[:-testing_period].to_csv(r'..\ml-financial-market\data\interim\interim_for_train.csv')
    df[-testing_period:].to_csv(r'..\ml-financial-market\data\interim\interim_for_portfolio.csv')

def build_features(positive_variation=1.02, testing_period=120):
    df = load_data()
    df = data_wrangle(df, positive_variation)
    save_data(df, testing_period)

build_features(positive_variation=1.02, testing_period = 90)