import pandas as pd
import numpy as np
from tensorflow import keras
def load_data():
	model = keras.models.load_model(r'..\ml-financial-market\models')
	df = pd.read_csv(r'..\ml-financial-market\data\interim\interim_for_portfolio.csv')
	scaled_portfolio = pd.read_csv(r'..\ml-financial-market\data\processed\portfolio.csv')

	return model, df, scaled_portfolio

def simulate(model,df,scaled_portfolio, positive_variation):
	portfolio = pd.DataFrame(index=df.index, columns=['position', 'stocks_owned', 'bank'])
	portfolio['date'] = df['date']
	portfolio['position'] = 'Sold'
	portfolio['bank'] = 10000
	portfolio['stocks_owned'] = 0
	portfolio['Model Recommendation'] = 0
	portfolio['close'] = df['close']
	portfolio.head()

	price_bought = 0
	
	for i in range(len(portfolio)-1):
		buy_or_not = model.predict_classes(np.array([scaled_portfolio.iloc[i],]))[0][0]
		portfolio['Model Recommendation'].iloc[i] = buy_or_not
		if portfolio['position'].iloc[i] == 'Sold':
			if buy_or_not == 1:
				portfolio['stocks_owned'].iloc[i+1] = int(portfolio['bank'].iloc[i]/portfolio['close'].iloc[i])
				portfolio['bank'].iloc[i+1] = (portfolio['bank'].iloc[i] % portfolio['close'].iloc[i])
				portfolio['position'].iloc[i+1] = 'Bought'
				price_bought = portfolio['close'].iloc[i]
				#print('Comprou por {}'.format(price_bought))
			else:
				portfolio['position'].iloc[i+1] = portfolio['position'].iloc[i]
				portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i]
				portfolio['stocks_owned'].iloc[i+1] = portfolio['stocks_owned'].iloc[i]
				#print('Não comprou')
		elif portfolio['close'].iloc[i] < (0.98) * price_bought:
			portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i] + portfolio['close'].iloc[i] * portfolio['stocks_owned'].iloc[i]
			portfolio['stocks_owned'].iloc[i+1] = 0
			portfolio['position'].iloc[i+1] = 'Sold'
			#print("Vendeu por {}".format(portfolio['close'].iloc[i]))
		elif portfolio['close'].iloc[i] >= positive_variation * price_bought:
			portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i] + portfolio['close'].iloc[i] * portfolio['stocks_owned'].iloc[i]
			portfolio['stocks_owned'].iloc[i+1] = 0
			portfolio['position'].iloc[i+1] = 'Sold'
			#print("Vendeu por {}".format(portfolio['close'].iloc[i]))
		else:
			portfolio['position'].iloc[i+1] = portfolio['position'].iloc[i]
			portfolio['bank'].iloc[i+1] = portfolio['bank'].iloc[i]
			portfolio['stocks_owned'].iloc[i+1] = portfolio['stocks_owned'].iloc[i]
			#print("Não vendeu.")

	portfolio['Total$'] = portfolio['stocks_owned'] * portfolio['close'] + portfolio['bank']
	portfolio.to_csv(r'..\ml-financial-market\data\portfolio\final_portfolio.csv')

def portfolio_simulation(positive_variation):
	model,df,scaled_portfolio = load_data()
	simulate(model,df,scaled_portfolio, positive_variation = 1.02)