#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




dataset = pd.read_csv('maaslar.csv')


X = dataset.iloc[:,1:-1].values.reshape(-1,1)
y = dataset.iloc[:,-1].values.reshape(-1,1)


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

"""from sklearn.preprocessing import PolynomialFeatures

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
"""




from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# svr scaller ile kullanılmak zorundadır.
sc = StandardScaler()
X_sc = sc.fit_transform(X)
y_sc = sc.fit_transform(y)

svr_reg = SVR(kernel='rbf')
svr_reg.fit(X_sc, y_sc)


# Grafik 

# Sc geri alma 
# Tahminleri gerçek değerlerle karşılaştır (isteğe bağlı)
# X_sc = sc_y.inverse_transform(X_sc)
# y_sc = sc_y.inverse_transform(y_sc)


# Grafik 
# Tahminlerin görselleştirilmesi (isteğe bağlı)
plt.scatter(X, y, color='red', label='Gerçek Değerler')
plt.plot(X_sc, svr_reg.predict(y_sc), color='blue', label='Tahminler')
plt.title('SVR Tahminleri')
plt.xlabel('Bağımsız Değişken')
plt.ylabel('Bağımlı Değişken')
plt.legend()
plt.show()















