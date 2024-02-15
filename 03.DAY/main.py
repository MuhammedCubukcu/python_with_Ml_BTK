# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Impor data csv
dataset = pd.read_csv('veriler.csv')
print(dataset)

country = dataset.iloc[:,:1].values
gender = dataset.iloc[:,-1].values.reshape(-1,1)
other_columns = dataset.iloc[:,1:-1].values



# OneHot encoding
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()
country = ohe.fit_transform(country).toarray()
gender = ohe.fit_transform(gender).toarray() 





# convert dataframe
country_df = pd.DataFrame(data=country,columns=['us','fr','tr'])
gender_df = pd.DataFrame(data=gender, columns=['cinsiyet','k']) # dummy variable
gender_df = gender_df.drop(['k'],axis=1)
other_columns_df = pd.DataFrame(data=other_columns, columns=['boy','kilo','yas'])

# merge dataframes
df = pd.concat([country_df,other_columns_df,gender_df],axis=1)
print(df)

# Split train and test data
from sklearn.model_selection import train_test_split

X = df.iloc[:,:-1].values
y = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=0)

# Model
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x_train,y_train)

y_pred = reg.predict(x_test)



gender = df.iloc[:,-1].values

result_df = pd.DataFrame({'Tahmin':y_pred,'gercek_deger':y_test})
print(result_df)


import statsmodels.api as sm

X = np.append(arr=np.ones((22,1)).astype(int), values=df,axis=1)

X_1 = df.iloc[:,[0,1,2,3,4,5]].values
X_1 = np.array(X_1,dtype=float)
model = sm.OLS(gender,X_1).fit()
print(model.summary())

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.626
Model:                            OLS   Adj. R-squared:                  0.509
Method:                 Least Squares   F-statistic:                     5.361
Date:                Thu, 15 Feb 2024   Prob (F-statistic):            0.00440
Time:                        15:56:22   Log-Likelihood:                -5.1425
No. Observations:                  22   AIC:                             22.29
Df Residuals:                      16   BIC:                             28.83
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             2.2338      1.174      1.903      0.075      -0.254       4.722
x2             2.2461      1.075      2.089      0.053      -0.033       4.525
x3             1.8514      1.122      1.651      0.118      -0.526       4.229
x4            -0.0204      0.010     -2.098      0.052      -0.041       0.000
x5             0.0308      0.008      3.682      0.002       0.013       0.048
x6            -0.0077      0.010     -0.813      0.428      -0.028       0.012
==============================================================================
Omnibus:                        0.140   Durbin-Watson:                   1.516
Prob(Omnibus):                  0.932   Jarque-Bera (JB):                0.212
Skew:                          -0.158   Prob(JB):                        0.899
Kurtosis:                       2.637   Cond. No.                     4.53e+03
==============================================================================
"""


X_1 = df.iloc[:,[0,1,3,4,5]].values
X_1 = np.array(X_1,dtype=float)
model = sm.OLS(gender,X_1).fit()
print(model.summary())

"""
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.781
Model:                            OLS   Adj. R-squared (uncentered):              0.717
Method:                 Least Squares   F-statistic:                              12.15
Date:                Thu, 15 Feb 2024   Prob (F-statistic):                    4.04e-05
Time:                        15:59:31   Log-Likelihood:                         -6.8721
No. Observations:                  22   AIC:                                      23.74
Df Residuals:                      17   BIC:                                      29.20
Df Model:                           5                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.3319      0.233      1.421      0.173      -0.161       0.825
x2             0.5229      0.269      1.943      0.069      -0.045       1.091
x3            -0.0054      0.004     -1.495      0.153      -0.013       0.002
x4             0.0201      0.006      3.607      0.002       0.008       0.032
x5            -0.0071      0.010     -0.707      0.489      -0.028       0.014
==============================================================================
Omnibus:                        0.032   Durbin-Watson:                   1.572
Prob(Omnibus):                  0.984   Jarque-Bera (JB):                0.218
Skew:                           0.066   Prob(JB):                        0.897
Kurtosis:                       2.531   Cond. No.                         724.
==============================================================================
"""





