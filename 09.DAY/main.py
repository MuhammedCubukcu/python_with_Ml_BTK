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
print(colmn)


# Kategorik değişkeni sayısal değere dönüştürme
title  =  df.iloc[:,0].values.reshape(-1,1)


from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
title_ohe = ohe.fit_transform(title).toarray()

# kategorik değişkeni dataframe yapma
title_df = pd.DataFrame(data=title_ohe,columns=["C-level","CEO","Cayci","Direktor","Mudur","Proje Yoneticisi","Sef","Sekreter","Uzman","Uzman Yardimcisi"])


# StandartScaler
from sklearn.preprocessing import StandardScaler 
other_columns = df.iloc[:,1::].values

sc = StandardScaler()
other_columns_sc = sc.fit_transform(other_columns)

# standart scaler dataframe yapma

other_columns_df = pd.DataFrame(data=other_columns_sc,columns=['UnvanSeviyesi', 'Kidem', 'Puan', 'maas'])

# Dataframeleri birleştirme.

merge_df = pd.concat([title_df,other_columns_df], axis=1)
print(merge_df)

# split data


X = merge_df.iloc[:, :-1].values
y = merge_df.iloc[:,-1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(X, y,test_size=0.33,random_state=0)

# Multiple Linear Model
from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()
linear_reg.fit(X_train,y_train)


y_pred = linear_reg.predict(X_test)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("Score : {} ".format(r2))






