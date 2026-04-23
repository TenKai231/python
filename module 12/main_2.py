from  sklearn.preprocessing import StandardScaler
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')

missing_values = train.isnull().sum()

less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index

numeric_features = train[less].select_dtypes(include=['number']).columns
train[numeric_features] = train[numeric_features].fillna(train[numeric_features].median())

ketegorical_features = train[less].select_dtypes(include=['object', 'string','category']).columns

for column in ketegorical_features:
    train[column] = train[column].fillna(train[column].mode()[0])

df = train.drop(columns=over)

missing_values = df .isnull().sum()
missing_values[missing_values > 0]

# Mengambil nilai kuartil 1 (25%) untuk setiap kolom numerik
Q1 = df[numeric_features].quantile(0.25)

# Mengambil nilai kuartil 3 (75%) untuk setiap kolom numerik
Q3 = df[numeric_features].quantile(0.75)

# Menghitung IQR (Interquartile Range), yaitu selisih antara Q3 dan Q1
IQR = Q3 - Q1

condition = ~((df[numeric_features] < (Q1 - 1.5 * IQR)) | (df[numeric_features] > (Q3 + 1.5 * IQR))).any(axis=1)

scaler = StandardScaler()
df[numeric_features] = scaler.fit_transform(df[numeric_features])

duplicare = df.duplicated().sum()
print("Jumlah data duplikat:", duplicare)
df = df.drop_duplicates()
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(train[numeric_features[3]], kde=True)
plt.title("Histogram sebelum standardisasi")

# sesudah
df['LotArea_log'] = np.log1p(train['LotArea'])

plt.subplot(1,2,2)
df['LotArea_log'] = np.log1p(train['LotArea'])
sns.histplot(df['LotArea_log'], kde=True)
plt.title("LotArea setelah log transform")

plt.tight_layout()
plt.show()
# print(train[numeric_features[3]].describe())
# print(df[numeric_features[3]].describe())
