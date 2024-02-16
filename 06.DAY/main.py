import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


dataset = pd.read_csv("veriler.csv")
print(dataset)


dataset = pd.DataFrame(dataset)
dataset = dataset.drop(['ulke','cinsiyet'],axis=1)




# Bağımsız değişkenler (X) ve bağımlı değişken (y) olarak veriyi ayırma
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı regresyon modelini oluşturma
model = DecisionTreeRegressor()

# Modeli eğitme
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Ortalama Kare Hatasını (MSE) hesaplama
mse = mean_squared_error(y_test, y_pred)
print("Ortalama Kare Hatası (MSE):", mse)


# Gerçek ve tahmin edilen değerleri içeren bir veri çerçevesi oluşturma
result_df = pd.DataFrame({'Gerçek Değerler': y_test, 'Tahmin Edilen Değerler': y_pred})

# Grafik çizimi
plt.figure(figsize=(10, 6))
plt.scatter(result_df['Gerçek Değerler'], result_df['Tahmin Edilen Değerler'], color='blue')
plt.title('Karar Ağacı Regresyon Modeli Tahminleri')
plt.xlabel('Gerçek Değerler')
plt.ylabel('Tahmin Edilen Değerler')
plt.show()
