# Homework Data Engineer Batch 9 - Week 2 - Digital Skola
# 1. Buat class Hewan yang memiliki class attributes nama_latin dan instance attributes nama dan umur:   
# a. Di class Hewan, memiliki instance method bangun, & class method change_nama_latin
# b. Buat child class Kucing yang memiliki value class attributes yang berbeda dengan parent class, 
# menggunakan class method change_nama_latin
# c. Di child class, override method bangun
# d. Di child class, buat method lari yang memiliki parameter kecepatan. 
# Jika value dari parameter kecepatan lebih dari 10, maka print cepat sekali selain itu print lambat

class Hewan:
    #class attributes: nama_latin
    nama_latin = "animalia"

    #instance attributes: nama dan umur
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    #instance method: bangun
    def bangun(self):
        return 'Hewan sedang bangun'

    #class method: change_nama_latin
    @classmethod
    def change_nama_latin (cls, nama):
        Hewan.nama_latin = nama
     
class Kucing(Hewan):

    #instance method: bangun
    def bangun(self):
        return 'Kucing sedang bangun'

    def lari(self, kecepatan):
        self.kecepatan = kecepatan
        if kecepatan > 10:
            print('Cepat sekali')
        else:
            print('Lambat')

# Instansiasi objek menggunakan parent class Hewan:
gajah = Hewan('Jumbo', 8)
Hewan.change_nama_latin('Elephas maximus')

print(gajah.nama)
print(gajah.nama_latin)
print(gajah.bangun())

kucing = Hewan('Kitty', 3)
Hewan.change_nama_latin('Felis catus')

print(kucing.nama)
print(kucing.nama_latin)
print(kucing.bangun())

# Instansiasi objek menggunakan child class Kucing:
kucing = Kucing('Kitty', 2)
Kucing.change_nama_latin('Felis catus')

print(kucing.nama)
print(kucing.nama_latin)
print(kucing.bangun())
kucing.lari(15)
