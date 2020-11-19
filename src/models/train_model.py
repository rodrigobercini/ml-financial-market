import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

X_train = np.array(pd.read_csv(r'..\ml-financial-market\data\processed\X_train.csv'))
y_train = pd.read_csv(r'..\ml-financial-market\data\processed\y_train.csv')

early_stop = EarlyStopping(monitor='val_loss', mode='auto', verbose=1, patience=25)

# Building the model
model = Sequential()
model.add(Dense(units=28,activation='relu'))
model.add(Dense(units=14,activation='relu'))
model.add(Dense(units=7,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
             metrics=['accuracy'])


# Fitting the model
model.fit(x=X_train, 
        y=y_train,
        epochs=2000, verbose=0.1,
        validation_data=(X_train,y_train),
        callbacks=[early_stop])

model.save(r'..\ml-financial-market\models')
pd.DataFrame(model.history.history).to_csv(r'..\ml-financial-market\models\history.csv')