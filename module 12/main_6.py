import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')
missing_values = train.isnull().sum()
less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index
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

