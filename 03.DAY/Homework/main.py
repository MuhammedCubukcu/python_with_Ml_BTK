#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot

dataset = pd.read_csv('odev_tenis.csv')
print(dataset)

outlook = dataset.iloc[:,0:1].values
windy = dataset.iloc[:,3:-1].values
play = dataset.iloc[:,-1].values.reshape(-1,1)
other_columns = dataset.iloc[:,1:3].values

# One Hot Encooder
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
outlook = ohe.fit_transform(outlook).toarray()
windy = ohe.fit_transform(windy).toarray()
play = ohe.fit_transform(play).toarray()

print(outlook)
print(windy)


# create dataframe
outlook_df = pd.DataFrame(data=outlook,columns=['overcast','rainy','sunny'])

windy_df = pd.DataFrame(data=windy,columns=['isWindy','false'])
#dummy variable 1 = TRUE, 0 = FALSE
windy_df = windy_df.drop(['false'], axis=1) # Delete column 

#dummy variable 1 = yes 0 = no
play_df = pd.DataFrame(data=play, columns=['isPlay','false'])
play_df = play_df.drop(['false'], axis=1)

other_columns_df = pd.DataFrame(data=other_columns, columns=['temperature','humidity'])


#concat method with all merge dataframe 

df = pd.concat([outlook_df,other_columns_df,windy_df,play_df], axis=1)



# Split data

X = df.iloc[:,0:-1].values 
y = df.iloc[:,6:7].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=0)


# model
from sklearn.linear_model import LinearRegression #LogisticRegression

reg = LinearRegression()
reg.fit(x_train, y_train)


y_pred = reg.predict(x_test)

for y,p in zip(y_test,y_pred):  
    print(f" y_test : {y} ----- y_pred : {p}")



"""
from sklearn.metrics import accuracy_score
# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
"""
















