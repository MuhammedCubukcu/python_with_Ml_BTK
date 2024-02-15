# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# import data csv
dataset = pd.read_csv('maaslar.csv')
print(dataset)


X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values


# split

"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=8,random_state=0)
"""
from sklearn.linear_model import LinearRegression

# LinearRegression
reg = LinearRegression()
reg.fit(X,y) 


"""
plt.scatter(X, y, c='blue')
plt.plot(X, reg.predict(X),c='red')
"""
# polyminal regression

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

linear_reg = LinearRegression()
linear_reg.fit(X_poly, y)

#Graph
plt.scatter(X, y)
plt.plot(X, linear_reg.predict(poly_reg.fit_transform(X)))


#predicts
#linear reg predict
print(reg.predict([[11]]))
# polyminal reg predict
print(linear_reg.predict(poly_reg.fit_transform([[6.6]])))