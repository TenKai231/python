
import matplotlib.pyplot as plt
import pandas as pd 


data = {
    "nama": ['Alice', 'Bob', 'Charlie'],
    "usia": [25, 30, 35],
    "pekerjaan": ['Data Scientist', 'Software Engineer', 'Product Manager']
}
df = pd.DataFrame(data)

print(df)

     
    # Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
     
    # Membuat plot garis
plt.plot(x, y)
     
    # Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
     
    # Menampilkan plot
plt.savefig("grafik.png")