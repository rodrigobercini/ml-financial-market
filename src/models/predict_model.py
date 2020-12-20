import pandas as pd
from sklearn.metrics import classification_report,confusion_matrix
import matplotlib.pyplot as plt
from tensorflow import keras

def predict_model():
    model = keras.models.load_model(r'..\ml-financial-market\models')
    model_history = pd.read_csv(r'..\ml-financial-market\models\\history.csv')

    X_test = pd.read_csv(r'..\ml-financial-market\data\processed\X_test.csv')
    y_test = pd.read_csv(r'..\ml-financial-market\data\processed\y_test.csv')

    # Getting loss and accuracy plot
    model_loss = pd.DataFrame(model_history)
    model_loss.plot()

    # Getting predictions metrics
    predictions = model.predict_classes(X_test)
    print(classification_report(y_test,predictions))
    print(confusion_matrix(y_test,predictions))

predict_model()