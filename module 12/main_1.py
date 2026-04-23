import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')
print(test.info())
print(test.head())
print(train.describe(include='all'))

missing_values = train.isnull().sum()
print(missing_values[missing_values > 0])
# print(train.shape)
# print(train.columns)
# print(train.info())
# print(train.head())

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

# for feature in df.columns:
#     plt.figure(figsize=(10,5))
#     sns.boxplot(x=df[feature])
#     plt.title(f'Boxplot of {feature}')
#     plt.savefig(f'boxplot_{feature}.png')
#     plt.close()

# sns.boxplot(data=df)

# plt.xticks(rotation=90)

# plt.savefig("boxplot.png")   # simpan gambar
# plt.close()

# for feature in numeric_features:
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x=df[feature])
#     plt.title(f'Box Plot of {feature}')
#     plt.show()

# Mengambil nilai kuartil 1 (25%) untuk setiap kolom numerik
Q1 = df[numeric_features].quantile(0.25)

# Mengambil nilai kuartil 3 (75%) untuk setiap kolom numerik
Q3 = df[numeric_features].quantile(0.75)

# Menghitung IQR (Interquartile Range), yaitu selisih antara Q3 dan Q1
IQR = Q3 - Q1

# Membuat kondisi/filter untuk memilih baris yang BUKAN outlier
# Rumus outlier:
# - lebih kecil dari Q1 - 1.5 * IQR
# - atau lebih besar dari Q3 + 1.5 * IQR
# Tanda ~ artinya membalik hasil, jadi yang diambil adalah data yang normal
# .any(axis=1) artinya jika dalam 1 baris ada minimal 1 kolom yang outlier,
# maka baris itu dianggap outlier
condition = ~((df[numeric_features] < (Q1 - 1.5 * IQR)) | (df[numeric_features] > (Q3 + 1.5 * IQR))).any(axis=1)

# Mengambil hanya kolom numerik dari baris-baris yang lolos filter
df_filtered_numeric = df.loc[condition, numeric_features]
 
# Mengambil nama-nama kolom kategorikal (tipe object), misalnya teks/string
categorical_features = df.select_dtypes(include=['object']).columns

# Menggabungkan kembali:
# - kolom numerik yang sudah dibersihkan dari outlier
# - kolom kategorikal dari baris yang sama
df = pd.concat([df_filtered_numeric, df.loc[condition, categorical_features]], axis=1)


# median = df['column_name'].median()
# df['column_name'] = df['column_name'].apply(lambda x: median if x < (Q1 - 1.5  IQR) or x > (Q3 + 1.5  IQR) else x)
# df['column_name'] = df['column_name'].apply(lambda x: (Q1 - 1.5  IQR) if x < lower_bound else (Q3 + 1.5  IQR) if x > (Q3 + 1.5 * IQR) else x)