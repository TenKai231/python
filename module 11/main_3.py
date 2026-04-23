import seaborn as sns 
import matplotlib.pyplot as plt


# contoh 
tips = sns.load_dataset("tips") 


# contoh ploot

sns.histplot(tips["total_bill"], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frekuensi')
plt.savefig("histogram_total_bill.png")

