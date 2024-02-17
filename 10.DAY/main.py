import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('veriler.csv')

x = dataset.iloc[5:,1:-1].values # ilk 5 satırı çıkarttım outlier veriler var ayrkırı modelin düzgün çalışması için.
y = dataset.iloc[5:,-1].values # ilk 5 satırı çıkarttım outlier veriler var ayrkırı modelin düzgün çalışması için.


from sklearn.model_selection import train_test_split


x_train,x_test,y_train,y_test = train_test_split(x, y,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)



from sklearn.linear_model import LogisticRegression

logistic_reg = LogisticRegression(random_state=0)
logistic_reg.fit(X_train,y_train)

y_pred = logistic_reg.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score,confusion_matrix


accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


matrix = confusion_matrix(y_test, y_pred)
print(matrix)


plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
plt.xlabel('Tahmin Edilen Etiketler')
plt.ylabel('Gerçek Etiketler')
plt.show()