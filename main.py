from src.data import make_dataset
from src.features import build_features, scale_features
from src.models import train_model
from src.portfolio import portfolio_simulation

def simulate_neural_network(ticker = 'PETR4.SA', period='2y', interval='60m', positive_variation = 1.02, testing_period = 120):
    make_dataset.make_dataset(ticker, period, interval)
    build_features.build_features(positive_variation=positive_variation, testing_period=testing_period)
    print('features built')
    scale_features.scale_features()
    print('features scaled')
    train_model.train_model()
    print('model trained')
    return portfolio_simulation.portfolio_simulation(positive_variation=positive_variation)

if __name__ == '__main__':
    simulate_neural_network()