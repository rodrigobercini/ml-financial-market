import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

def load_data():
        X_train = np.array(pd.read_csv(r'..\ml-financial-market\data\processed\X_train.csv'))
        y_train = pd.read_csv(r'..\ml-financial-market\data\processed\y_train.csv')
        return X_train, y_train

def train(X_train, y_train):

        early_stop = EarlyStopping(monitor='val_loss', mode='auto', verbose=1, patience=25)

        # Building the model
        model = Sequential()
        model.add(Dense(units=64,activation='relu'))
        model.add(Dense(units=32,activation='relu'))
        model.add(Dense(units=16,activation='relu'))
        model.add(Dense(units=8,activation='relu'))
        model.add(Dense(units=1,activation='sigmoid'))
        model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])


        # Fitting the model
        model.fit(x=X_train, 
                y=y_train,
                epochs=1000, verbose=0.1,
                validation_data=(X_train,y_train),
                callbacks=[early_stop])

        return model

def save_model(model):
        model.save(r'..\ml-financial-market\models')
        pd.DataFrame(model.history.history).to_csv(r'..\ml-financial-market\models\history.csv')

def train_model():
        X_train, y_train = load_data()
        model = train(X_train, y_train)
        save_model(model)

if __name__ == '__main__':
        train_model()
