import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('veriler.csv')


X = dataset.iloc[5:,1:-1].values #outlier(aykırı verileri almadım ilk beş satır.Modelimi bozduğu için)
y = dataset.iloc[5:,-1].values


x_train,x_test,y_train,y_test = train_test_split(X, y,test_size=0.33,random_state=0)

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()

dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)

from sklearn.metrics import accuracy_score,confusion_matrix

acc = accuracy_score(y_test, y_pred)
print("Accuracy Score :",acc)

matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix :  \n",matrix)