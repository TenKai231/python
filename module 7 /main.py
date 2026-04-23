from hello  import mencari_luas_persegi_panjang, nama 
persegi = mencari_luas_persegi_panjang(5, 10)
print(persegi)
print(nama)

# def luas_persegi(panjang, lebar):
#     rumus = panjang * lebar 
#     return rumus

# persegi = luas_persegi(5, 10)
# print(persegi)

# def penjumlahan(a, b, /):
#     return a + b

# a = 10 
# b = 12

# print(penjumlahan(12, 10))

# def cetak_info(**kwargs):
#     info = ""
#     for key, value in kwargs.items():
#         info += key + ': ' + value + ", "
#     return info

# print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
    

#     Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
# - Menerima dua buah argumen berupa number, yaitu a dan b.
# - Mengembalikan nilai terkecil antara a atau b.
# - Bila nilai keduanya sama, kembalikan dengan nilai a.
# """

def minimal(a, b):
    if a < b:
        return a
    elif a > b :
        return b
    else: 
        return a
    
print(minimal(10, 12)) 