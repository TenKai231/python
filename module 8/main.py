class mobil :
    warna = 'merah'

mobil1 = mobil()
print(mobil1.warna)

mobil1 = mobil()
print(mobil1.warna)

mobil.warna = 'biru'

mobil1 = mobil()
print(mobil1.warna)

mobil1 = mobil()
print(mobil1.warna)

class mobil :
    # atribut distance 
    def __init__(self):
        self.warna = 'Hijau'

mobil1 = mobil()
print(mobil1.warna)

class mobil :
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tembahakan_kecepatan(self):
        self.kecepatan += 10

mobil1 = mobil('merah', 'Dicoding', 160)
print ("sebelum di tambahakan keceptan")
print (mobil1.kecepatan)

mobil1.tembahakan_kecepatan()

print("setelah di tambahkan kecepatan")
print(mobil1.kecepatan)

print(mobil1.warna)
print(mobil1.merek)
print(mobil1.kecepatan)

# pewarisan class

class mobilSprot(mobil):
    def turbo(self):
        self.kecepatan += 50

mobil_sport = mobilSprot('kuning', 'Ferrari', 200)
print(mobil_sport.kecepatan)
mobil_sport.turbo()
print(mobil_sport.kecepatan)



def derektori(func):
    def wrapper():
        print("Sebelum fungsi dijalankan")
        func()
        print("Setelah fungsi di eksesukasi")
    return wrapper 

#disrketori funsgi yang di jalankan 

@derektori
def katakan_hallo():
    print ("hallo dunai ! ")

katakan_hallo()


# class mathod 
class mobil :
    def __init__(self, nama):
        print ("ini adalah mathod init")
    
    @classmethod
    def into_mobil(cls):
        print ("ini adalah  dari kelas mathod class")

mobil.into_mobil()
mobil_1 = mobil("dicoding")
mobil_1.into_mobil() 


