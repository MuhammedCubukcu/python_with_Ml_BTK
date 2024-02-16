from sklearn.datasets import fetch_california_housing, fetch_openml
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# California ev fiyatları veri setini yükleme
housing = fetch_california_housing()
X = housing.data
y = housing.target

# Veri setini eğitim ve test kümelerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Regressor modelini oluşturma ve eğitme
rf_regressor = RandomForestRegressor(n_estimators=10, random_state=42)
rf_regressor.fit(X_train, y_train)

# Test kümelerini kullanarak tahmin yapma
y_pred = rf_regressor.predict(X_test)

# Hata hesaplama
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Gerçek ve tahmin edilen fiyatlar arasındaki ilişkiyi görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
plt.xlabel('Gerçek Fiyatlar')
plt.ylabel('Tahmin Edilen Fiyatlar')
plt.title('Random Forest Regressor ile Ev Fiyatları Tahmini')
plt.show()
