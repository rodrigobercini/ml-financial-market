from src.data import make_dataset
from src.features import build_features, scale_features
from src.models import train_model
from src.portfolio import portfolio_simulation

positive_variation = 1.01

make_dataset.make_dataset(ticker = 'PETR4.SA', period='1mo', interval='5m')
build_features.build_features(positive_variation=positive_variation, testing_period = 120)
print('features built')
scale_features.scale_features()
print('features scaled')
train_model.train_model()
print('model trained')
portfolio_simulation.portfolio_simulation(positive_variation=positive_variation)