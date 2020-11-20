import pandas as pd

# Feature engineering
data = pd.read_csv(r'..\ml-financial-market\data\external\stock_dataframe.csv')

df = data[['close', 'volume']]

def column_shifter(n_shift, df, column):
    for i in range(1, n_shift):
        df[f'{column}_minus{i}'] = df[column].shift(i)

for column in ['close', 'volume']: column_shifter(28, df, column)

df.dropna(inplace=True)

# Creating column to check if the stock price rose in the following X periods
df['Rise'] = 1
periods_ahead = 24
positive_variation = 1.02

df['Rise']  = (df['close'].iloc[::-1].rolling(periods_ahead).max() / df['close']).gt(positive_variation).astype(int)

# We don't know if the last records rose or not, so we will remove them from the dataset
df = df.iloc[:-periods_ahead]

df.to_csv(r'..\ml-financial-market\data\interim\interim.csv')
