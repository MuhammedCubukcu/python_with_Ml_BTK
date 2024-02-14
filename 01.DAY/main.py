# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





# import data from csv
dataset = pd.read_csv("veriler.csv")
print(dataset)


# data preprocessing


# get country colum
#country = dataset[['ulke']]
#print(country)


# get height and weight column

get_height_and_weight = dataset[['boy','kilo']]
print(get_height_and_weight)



# Missing Values

missing_value_dataset = pd.read_csv('eksikveriler.csv')
print(missing_value_dataset)


# sum of missing data
print(missing_value_dataset.isna().sum()) # there are two empty values in yas column

# filling in missing data with averaging
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
age = missing_value_dataset.iloc[1:4].values
imputer = imputer.fit(age[:,1:4])
age[:,1:4] = imputer.transform(age[:,1:4])
print(age)



# Label encoder and OneHot encoder

from sklearn.preprocessing import LabelEncoder,OneHotEncoder


# label encoder
le = LabelEncoder()
country = dataset.iloc[:,0:1].values
print(country)
country[:,0] = le.fit_transform(country[:,0])
print(country)

# OneHot encoder
one_hot_encoder = OneHotEncoder()
country = one_hot_encoder.fit_transform(country).toarray()
print(country)





country_df = pd.DataFrame(data=country,columns=['fr','tr','us'])
print(country_df)

age = dataset.iloc[:,1:4].values


age_df = pd.DataFrame(data=age, columns=['boy','kilo','yas'])
print(age_df)


gender = dataset.iloc[:,-1].values
print(gender)
gender = le.fit_transform(gender)
print(gender)


gender_df = pd.DataFrame(data=gender, columns=['cinsiyet']) #0 = erkek, 1=kadın

# concat method
df = pd.concat([country_df,age_df,gender_df], axis=1)
print(df)

# data split train and test
from sklearn.model_selection import train_test_split

X= df.iloc[:,0:-1].values
y = df.iloc[:,-1].values


x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=0)



from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)





