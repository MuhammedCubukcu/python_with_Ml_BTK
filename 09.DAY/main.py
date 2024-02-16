#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Veri Önişleme (Data Preorıcessig)
# Data setini yükleme
dataset = pd.read_csv('maaslar_yeni.csv')

# pandas dataframe oluşturma
df = pd.DataFrame(dataset)
colmn = df.columns

# sütun silme 
df = df.drop(['Calisan ID'],axis=1)



# Kategorik değişkeni sayısal değere dönüştürme
title  =  df.iloc[:,0].values.reshape(-1,1)


from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
title_ohe = ohe.fit_transform(title).toarray()

# kategorik değişkeni dataframe yapma
title_df = pd.DataFrame(data=title_ohe,columns=["C-level","CEO","Cayci","Direktor","Mudur","Proje Yoneticisi","Sef","Sekreter","Uzman","Uzman Yardimcisi"])

other_columns = df.iloc[:,1::].values
#StandartScaler
from sklearn.preprocessing import StandardScaler 


sc = StandardScaler()
other_columns_sc = sc.fit_transform(other_columns)

# standart scaler dataframe yapma"""

other_columns_df = pd.DataFrame(data=other_columns,columns=['UnvanSeviyesi', 'Kidem', 'Puan', 'maas'])

# Dataframeleri birleştirme.

merge_df = pd.concat([title_df,other_columns_df], axis=1)


# split data


X = merge_df.iloc[:, :-1].values
y = merge_df.iloc[:,-1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(X, y,test_size=0.1,random_state=0)

# Multiple Linear Model
from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()
linear_reg.fit(X_train,y_train)


y_pred = linear_reg.predict(X_test)


from sklearn.metrics import r2_score

r2_mlr = r2_score(y_test, y_pred)
print("Multiple Regresyon için R2 skoru: ",r2_mlr)
ceo1 = linear_reg.predict([[0,0,1,0,0,0,0,0,0,0,10,0,100]])





# Polynimal Regression(PR)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)

linear_reg_poly = LinearRegression()
linear_reg_poly.fit(X_poly, y_train)

# Polinom regresyon modelinin tahminlerini yapma
y_pred_poly = linear_reg_poly.predict(poly_reg.fit_transform(X_test))

# R2 skorunu hesaplama
r2_poly = r2_score(y_test, y_pred_poly)
print("Polinom Regresyonu için R2 skoru:", r2_poly)

ceo2 = linear_reg_poly.predict(poly_reg.fit_transform([[0,0,1,0,0,0,0,0,0,0,10,0,100]]))




# Support Vector Regression
from sklearn.svm import SVR

svr_model = SVR(kernel='rbf')  # RBF (Gaussian) kernel kullanıldı
svr_model.fit(X_train, y_train)

# Tahminler yapma
y_pred = svr_model.predict(X_test)


# Modelin performansını değerlendirme
r2 = r2_score(y_test, y_pred)
print("SVR modeli için R2 skoru:", r2)
ceo3 = svr_model.predict([[0,0,1,0,0,0,0,0,0,0,10,0,100]])




# Desicion Tree
from sklearn.tree import DecisionTreeRegressor

dt_regressor = DecisionTreeRegressor(random_state=2)  # Rastgele bir tohum (seed) kullanarak tekrarlanabilir sonuçlar elde etme.
dt_regressor.fit(X_train, y_train)
# Tahminler yapma
y_pred = dt_regressor.predict(X_test)

# Modelin performansını değerlendirme
r2 = r2_score(y_test, y_pred)
print("Karar Ağacı modeli için R2 skoru:", r2)
ceo4 = dt_regressor.predict([[0,0,1,0,0,0,0,0,0,0,10,0,100]])



# Random Forest
from sklearn.ensemble import RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=9,random_state=2)  # 100 karar ağacı kullanılacak

rf_regressor.fit(X_train, y_train)

# Tahminler yapma
y_pred = rf_regressor.predict(X_test)

# Modelin performansını değerlendirme
r2 = r2_score(y_test, y_pred)
print("Random Forest modeli için R2 skoru:", r2)

ceo5 = rf_regressor.predict([[0,0,1,0,0,0,0,0,0,0,10,0,100]])




predict_one_value_result = { 
        'ceo_MLR': ceo1,
        'ceo_PR': ceo2,
        'ceo_SVR': ceo3,
        'ceo_DT': ceo4,
        'ceo_RR': ceo5
}

print("İstenilen tahminin sonuçları:")
for key, value in predict_one_value_result.items():
    print("{0} : {1} ".format(key, value))







# R2 Skorları Grafiği
models = ['Multiple Regression', 'Polynomial Regression', 'SVR', 'Decision Tree', 'Random Forest']
r2_scores = [0.615, 0.707, -0.070, 0.979, 0.987]

plt.figure(figsize=(10, 6))
plt.bar(models, r2_scores, color='blue')
plt.xlabel('Models')
plt.ylabel('R2 Score')
plt.title('R2 Scores of Different Regression Models')
plt.ylim(-0.1, 1.1)
plt.xticks(rotation=45)
plt.show()

plt.show()






