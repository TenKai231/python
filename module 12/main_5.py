import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import numpy as np

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

# Visualisasi distribusi data untuk beberapa kolom
# columns_to_plot = ['OverallQual', 'YearBuilt', 'LotArea', 'SaleType', 'SaleCondition']
     
# plt.figure(figsize=(15, 10))
# for i, column in enumerate(columns_to_plot, 1):
#     plt.subplot(2, 3, i)
#     sns.histplot(df[column], kde=True, bins=30)
#     plt.title(f'Distribution of {column}')
     
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(12, 10))
correlation_matrix = df_Lencoded.corr()
 
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

corr_with_target = df_Lencoded.corr()['SalePrice'].sort_values(ascending=False)

print("=== TOP 15 VARIABEL PALING BERPENGARUH (Positif) ===")
print(corr_with_target.head(16))  # head(16) karena index 0 = SalePrice itu sendiri

print("\n=== TOP 10 VARIABEL PENGARUH NEGATIF ===")
print(corr_with_target.tail(10))

print("\n=== VARIABEL PENGARUH LEMAH (bisa dibuang) ===")
lemah = corr_with_target[(corr_with_target.abs() < 0.2) & (corr_with_target.index != 'SalePrice')]
print(lemah)

# 2. Visualisasi bar chart korelasi terhadap SalePrice
top_features = corr_with_target[1:21]  # ambil 20 teratas (skip SalePrice sendiri)
plt.figure(figsize=(10, 8))
top_features.sort_values().plot(kind='barh', color=['red' if x < 0 else 'steelblue' for x in top_features.sort_values()])
plt.title('Top 20 Korelasi terhadap SalePrice')
plt.xlabel('Nilai Korelasi')
plt.tight_layout()
plt.show()

# 3. Cek multikolinearitas (fitur yang terlalu mirip satu sama lain)
print("\n=== PASANGAN FITUR DENGAN KORELASI TINGGI (> 0.8) ===")
corr_matrix = df_Lencoded.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

high_corr_pairs = [(col, row, upper.loc[row, col]) 
                   for col in upper.columns 
                   for row in upper.index 
                   if upper.loc[row, col] > 0.8]

if high_corr_pairs:
    for pair in high_corr_pairs:
        print(f"{pair[0]} <-> {pair[1]} : {pair[2]:.2f}")
else:
    print("Tidak ada pasangan fitur dengan korelasi > 0.8")


target_corr = df_Lencoded.corr()['SalePrice']
 
# (Opsional) Mengurutkan hasil korelasi berdasarkan korelasi
target_corr_sorted = target_corr.abs().sort_values(ascending=False)
 
plt.figure(figsize=(10, 6))
target_corr_sorted.plot(kind='bar')
plt.title(f'Correlation with SalePrice')
plt.xlabel('Variables')
plt.ylabel('Correlation Coefficient')
plt.show()

print(df_Lencoded.columns.tolist())