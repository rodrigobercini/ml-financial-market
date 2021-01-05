import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib

def load_data():
    df = pd.read_csv(r'..\ml-financial-market\data\interim\interim_for_train.csv')
    df_portfolio = pd.read_csv(r'..\ml-financial-market\data\interim\interim_for_portfolio.csv')
    return df, df_portfolio

def scale_data(df, df_portfolio):
    X = df.drop(['Rise','date'], axis=1)
    df_portfolio = df_portfolio.drop(['Rise','date'], axis=1)
    y = df['Rise']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1949)

# Scaling data
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    df_portfolio = scaler.transform(df_portfolio)

    joblib.dump(scaler, r'..\ml-financial-market\models\scaler')

    return df, X_train, X_test, y_train, y_test, df_portfolio

def save_data(df, X_train, X_test, y_train, y_test, df_portfolio):
    pd.DataFrame(X_train).to_csv(r'..\ml-financial-market\data\processed\X_train.csv', index=False)
    pd.DataFrame(X_test).to_csv(r'..\ml-financial-market\data\processed\X_test.csv', index=False)
    y_train.to_csv(r'..\ml-financial-market\data\processed\y_train.csv', index=False)
    y_test.to_csv(r'..\ml-financial-market\data\processed\y_test.csv', index=False)
    pd.DataFrame(df_portfolio).to_csv(r'..\ml-financial-market\data\processed\portfolio.csv', index=False)


def scale_features():
    df, df_portfolio = load_data()
    df, X_train, X_test, y_train, y_test, df_portfolio = scale_data(df, df_portfolio)
    save_data(df, X_train, X_test, y_train, y_test, df_portfolio)

if __name__ == '__main__':
    scale_features()
