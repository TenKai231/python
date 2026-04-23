import pickle
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
     

# contoh_direcetori = {"Alice": 25, "Bob": 30, "Charlie": 35}
# pickle_keluar = open("contoh_direcetori.pkl", "wb")
# pickle.dump(contoh_direcetori, pickle_keluar)
# pickle_keluar.close()

# pickle_masuk = open("contoh_direcetori.pkl", "rb")
# contohDictionary = pickle.load(pickle_masuk)
# pickle_masuk.close()
     
# print(contohDictionary)


# url = "https://python.org"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title.text)

#     # Pengambilan konten
# url = "http://python.org/"

# req =  requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# page = urlopen(url)
# html = page.read()
     
#     # Membuat objek BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# if soup.title:
#     print(soup.title.text)
# else :
#     print("Title not found")


# # Pengambilan konten
# url = "http://python.org/"
# page = urlopen(url)
# html = page.read().decode("utf-8")
 
# # Mencari indeks awal dan akhir
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
 
# # Mengekstrak dan mencetak judul halaman
# title = html[start_index:end_index]
# print(title)

print (input("Masukkan nama Anda: "))