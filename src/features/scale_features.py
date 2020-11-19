import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


df = pd.read_csv(r'..\ml-financial-market\data\interim\interim.csv')

X = df.drop('Rise', axis=1)
y = df['Rise']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=1949)

# Scaling data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

for df in [X_train, X_test, y_train, y_test]:
    pd.DataFrame(df).to_csv(r'..\ml-financial-market\data\processed\X_train.csv')    

pd.DataFrame(X_train).to_csv(r'..\ml-financial-market\data\processed\X_train.csv', index=False)
pd.DataFrame(X_test).to_csv(r'..\ml-financial-market\data\processed\X_test.csv', index=False)
y_test.to_csv(r'..\ml-financial-market\data\processed\y_test.csv', index=False)
y_train.to_csv(r'..\ml-financial-market\data\processed\y_train.csv', index=False)
