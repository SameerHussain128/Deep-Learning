# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part 1 - Data Preprocessing

# Importing the dataset
df = pd.read_csv(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\Projects\Imbalance dataset\creditcard.csv')

df.head()
df['Class'].value_counts()

pd.value_counts(df['Class']).plot.bar()


df.columns()
len(df.columns)

# Seperating x,y

x = df.iloc[:,1:30]
y = df.iloc[:,-1]

x.head()
y.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.30, random_state=0)

y_train.value_counts()


import tensorflow as tf
import tensorflow.keras.layers import Dense
import tensorflow.keras.models import Sequential

len(df.columns)
n_inputs=29

# Initializing the ANN
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=1, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=50, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Part 3 - Training the ANN

# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the Training set
ann.fit(x_train, y_train, epochs = 10)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred1)
print(cm)

from sklearn.metrics import roc_auc_score
y_pred1 = ann.predict(x_test)

print(roc_auc_score(y_test, y_pred1))



# Weighted Neural Network with Keras
# define weights
# fit the model with those specific weights

weights_assigned = {0:1,1:550}

# Initializing the ANN                                       ## 2
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=1, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=50, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Part 3 - Training the ANN

# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the Training set
ann.fit(x_train, y_train, class_weight=weights_assigned, epochs = 10)

y_pred = ann.predict(x_test)

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_pred))


