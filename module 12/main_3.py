import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.calibration import LabelEncoder
from sklearn.preprocessing import StandardScaler

test = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/test.csv')
train = pd.read_csv('/home/tenkai/Downloads/home-data-for-ml-course/train.csv')

missing_values = train.isnull().sum()

less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index

df = train.drop(columns=over)

label_encoder = LabelEncoder()
df_laucher = pd.DataFrame(df)

categorical_features = train[less].select_dtypes(include=['object', 'string','category']).columns

for col in categorical_features:
    df_laucher[col] = label_encoder.fit_transform(df_laucher[col])


df_laucher