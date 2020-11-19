import pandas as pd
import numpy as np
from tensorflow import keras

model = keras.models.load_model(r'..\ml-financial-market\models')
df = pd.read_csv(r'..\ml-financial-market\data\interim\interim.csv')
X_test = pd.read_csv(r'..\ml-financial-market\data\processed\X_test.csv')

portfolio = pd.DataFrame(index=df.index, columns=['position', 'stocks_owned', 'bank'])
portfolio['position'] = 'Sold'
portfolio['bank'] = 10000
portfolio['stocks_owned'] = 0
portfolio['Model Recommendation'] = 0
portfolio['close'] = df['close']
portfolio.head()

price_bought = 0

positive_variation = 0.02

for i in range(len(portfolio)-1):
	buy_or_not = model.predict_classes(np.array([X_test[i],]))[0][0]
	portfolio['Model Recommendation'].iloc[i] = buy_or_not
	if portfolio['position'].iloc[i] == 'Sold':
		if buy_or_not == 1:
			portfolio['stocks_owned'].iloc[i+1] = int(portfolio['bank'].iloc[i]/portfolio['close'].iloc[i])
			portfolio['bank'].iloc[i+1] = (portfolio['bank'].iloc[i] % portfolio['close'].iloc[i])
			portfolio['position'].iloc[i+1] = 'Bought'
			price_bought = portfolio['close'].iloc[i]
			print('Comprou por {}'.format(price_bought))
		else:
			portfolio['position'].iloc[i+1] = portfolio['position'].iloc[i]
			portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i]
			portfolio['stocks_owned'].iloc[i+1] = portfolio['stocks_owned'].iloc[i]
			print('Não comprou')
	elif portfolio['close'].iloc[i] < (0.95) * price_bought:
		portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i] + portfolio['close'].iloc[i] * portfolio['stocks_owned'].iloc[i]
		portfolio['stocks_owned'].iloc[i+1] = 0
		portfolio['position'].iloc[i+1] = 'Sold'
		print("Vendeu por {}".format(portfolio['close'].iloc[i]))
	elif portfolio['close'].iloc[i] > positive_variation * price_bought:
		portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i] + portfolio['close'].iloc[i] * portfolio['stocks_owned'].iloc[i]
		portfolio['stocks_owned'].iloc[i+1] = 0
		portfolio['position'].iloc[i+1] = 'Sold'
		print("Vendeu por {}".format(portfolio['close'].iloc[i]))
	else:
		portfolio['position'].iloc[i+1] = portfolio['position'].iloc[i]
		portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i]
		portfolio['stocks_owned'].iloc[i+1] = portfolio['stocks_owned'].iloc[i]
		print("Não vendeu.")

portfolio['Total$'] = portfolio['stocks_owned'] * portfolio['close'] + portfolio['bank']
portfolio['Total$'].describe()