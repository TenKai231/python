import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load data
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')

# Drop kolom missing besar
missing_values = train.isnull().sum()
over = missing_values[missing_values >= 1000].index
df = train.drop(columns=over)

# Split dulu
X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Encoding setelah split
# Encoding
x_train = pd.get_dummies(x_train, drop_first=True)
x_test = pd.get_dummies(x_test, drop_first=True)

# Ambil numeric DULU
x_train = x_train.select_dtypes(include=[np.number])
x_test = x_test.select_dtypes(include=[np.number])

# 🔥 ALIGN TERAKHIR
x_train, x_test = x_train.align(x_test, join='left', axis=1, fill_value=0)

# Imputer
imputer = SimpleImputer(strategy='median')

x_train = pd.DataFrame(
    imputer.fit_transform(x_train),
    columns=x_train.columns,
    index=x_train.index
)

x_test = pd.DataFrame(
    imputer.transform(x_test),
    columns=x_train.columns,  # wajib sama
    index=x_test.index
)

print("jumlah data :", len(X))
print("jumlah data latih:", len(x_train))
print("jumlah data test:", len(x_test))

print("Train shape:", x_train.shape)
print("Test shape:", x_test.shape)

print((x_train.columns == x_test.columns).all())