import sklearn 
from sklearn import linear_model
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split


# Load data 
test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')

# Drop kollom missing value lebih dari 1000
missing_values = train.isnull().sum()
over = missing_values[missing_values >= 1000].index

#target & fiitur 
df = train.drop(columns=over)
df_Lencoded = pd.get_dummies(df, drop_first=True)

missing_values = df_Lencoded.isnull().sum()
missing_percetage = (missing_values / len(df_Lencoded)) * 100

missing_values = df_Lencoded.isnull().sum()
missing_percentage = (missing_values / len(df_Lencoded)) * 100

missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
}).sort_values(by='Missing Values', ascending=False)
 
missing_data[missing_data['Missing Values'] > 0] 
X = df_Lencoded.drop(columns=['SalePrice'])
y = df_Lencoded['SalePrice']    

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

x_train = pd.get_dummies(x_train,drop_first=True)
x_test = pd.get_dummies(x_test,drop_first=True) 

#samakan kolom Train
x_train, x_test = x_train.align(x_test, join='left', axis=1, fill_value=0)

x_train = x_train.select_dtypes(include=[np.number])
x_test = x_test.select_dtypes(include=[np.number])

#handel msiing values
imputer = SimpleImputer(strategy='median')

x_train_imputed = np.asarray(imputer.fit_transform(x_train))
x_test_imputed = np.asarray(imputer.transform(x_test))

x_train = pd.DataFrame(x_train_imputed, columns=x_train.columns, index=x_train.index)
x_test = pd.DataFrame(x_test_imputed,columns=x_test.columns, index=x_test.index)

# print("jumlah data : ", len(X))
# print("jumlah data latih: ", len(x_train))
# print("jumlah data test: ", len(x_test))

# print("Train shape:", x_train.shape)
# print("Test shape:", x_test.shape)

# print((x_train.columns == x_test.columns).all())

lars = linear_model.Lars(n_nonzero_coefs=1).fit(x_train, y_train)

from sklearn.linear_model import LinearRegression
LR = LinearRegression().fit(x_train, y_train)

from sklearn.ensemble import GradientBoostingClassifier
GBR = GradientBoostingClassifier(random_state=184)
GBR.fit(x_train, y_train)  

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

pred_lars = lars.predict(x_test)
mae_lars = mean_absolute_error(y_test, pred_lars)
mse_lars = mean_squared_error(y_test, pred_lars)
r2_lars = r2_score(y_test, pred_lars)

data = {
    'MAE': [mae_lars],
    'MSE': [mse_lars],
    'R2': [r2_lars]
}

df_results = pd.DataFrame(data, index=['Lars'])
print(df_results)

pred_LR = LR.predict(x_test)
mae_LR = mean_absolute_error(y_test, pred_LR)
mse_LR = mean_squared_error(y_test, pred_LR)
r2_LR = r2_score(y_test, pred_LR)

df_results.loc['Linear Regression'] = [mae_LR, mse_LR, r2_LR]
print(df_results)

pred_GBR = GBR.predict(x_test)
mae_GBR = mean_absolute_error(y_test, pred_GBR)
mse_GBR = mean_squared_error(y_test, pred_GBR)
r2_GBR = r2_score(y_test, pred_GBR)

df_results.loc['Gradient Boosting'] = [mae_GBR, mse_GBR, r2_GBR]
print(df_results)

import joblib
import pickle

joblib.dump(lars, 'model_lars.pkl')
with open('model_lars.pkl', 'wb') as file:
    pickle.dump(lars, file)

