import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')
missing_values = train.isnull().sum()

less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index
df = train.drop(columns=over)

df_encoded = pd.get_dummies(df, drop_first=True)


missing_values = df_encoded.isnull().sum()
missing_percetage = (missing_values / len(df_encoded)) * 100

imputer = SimpleImputer(strategy='median')
df_encoded[missing_values.index] = imputer.fit_transform(df_encoded[missing_values.index])
scaler = StandardScaler()
df_encoded[df_encoded.columns] = scaler.fit_transform(df_encoded[df_encoded.columns])


missing_data = pd.DataFrame({
    'missing_values' : missing_values,
    'missing_percentage' : missing_percetage
}).sort_values(by='missing_percentage', ascending=False)

missing_data[missing_data['missing_percentage'] > 0]

features = ['Id', 'MSSubClass', 'LotFrontage', 'LotArea']

plt.figure(figsize=(16,4))

for i, col in enumerate(features, 1):
    plt.subplot(1,4,i)
    sns.histplot(df_encoded[col], kde=True)
    plt.title(col)

plt.tight_layout()
plt.show()


# num_vars = df_encoded.shape[1]

# n_cols = 4
# n_rows = -(-num_vars // n_cols)

# fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 4))

# axes = axes.flatten()

# for i, column in enumerate(df_encoded.columns):
#     sns.histplot(df_encoded[column], ax=axes[i], kde=True)
#     axes[i].set_title(f'Distribution of {column}')
#     axes[i].set_xlabel(column)
#     axes[i].set_ylabel('Frequency')

# for j in range(i + 1, len(axes)):
#     fig.delaxes(axes[j])

# plt.tight_layout()
# plt.show()