from sklearn.metrics import accuracy_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 1, 0, 0]

accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)



from sklearn.metrics import precision_score

precision = precision_score(y_true, y_pred)
print("Precision:", precision)


from sklearn.metrics import recall_score

recall = recall_score(y_true, y_pred)
print("Recall:", recall)


from sklearn.metrics import f1_score

f1 = f1_score(y_true, y_pred)
print("F1 Score:", f1)


from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

mse = mean_squared_error(y_true, y_pred)
print("MSE:", mse)
