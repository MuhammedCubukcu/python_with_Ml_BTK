# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# import data csv 

dataset = pd.read_csv('satislar.csv')
print(dataset)


X = dataset.iloc[:,:1].values
y = dataset.iloc[:,-1].values



# Split train and test data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# split data
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=0)

# Standard scaler
sc = StandardScaler()

X_train = sc.fit_transform(x_train.reshape(-1, 1))
X_test = sc.transform(x_test.reshape(-1, 1))
Y_train = sc.fit_transform(y_train.reshape(-1, 1))
Y_test = sc.transform(y_test.reshape(-1, 1))

# Simple Linear Regression Model

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train,Y_train) # x_trainden y_train i öğrendi.

predict = lr.predict(X_test) # X_test den kendi tahmin sonucunu çıkardı. 


predict = sc.inverse_transform(predict)
y_pred_test = sc.inverse_transform(Y_test.reshape(-1,1))


# Scatter Plot
plt.scatter(y_pred_test,predict,c='blue')
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Edilen Değerler")
plt.title("Gerçek Değerler vs. Tahmin Edilen Değerler")
# eğilim çizgisi ekle
z = np.polyfit(y_pred_test.flatten(), predict.flatten(), 1)
p = np.poly1d(z)
plt.plot(y_pred_test, p(y_pred_test), color='red', label='Eğilim Çizgisi')