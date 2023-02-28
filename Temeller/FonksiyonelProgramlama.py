#Fonksiyonel Programlama

# =============================================================================
# Fonksiyonlar dilin baslangicidir.
# (birinci sinif nesnelerdir)
# Yan etkisiz foksiyonlar. (stateless, girdi-cikti)
# yuksek seviye fonksiyonlar.
# Vektorel operasyonlar.
# =============================================================================


#Yan etkisiz fonksiyonlar

#Ornek1 : Bagimsizlik

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6) #yan etkili

pure_sum(3, 4) #yan etkisiz



#Ornek2 : Olumcul yan etkiler
#OOP

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename,"r")
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()    

print(lc.lines)
print(lc.count())


#Fonksiyonel programlama ile yapalim birde

def read(filename):
    with open(filename, "r") as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count
#Bagimsiz birbirinin icinde pespese kullanilabilen daha rahat ancak girdi verildin
#de cikti veren bir yapidir fonksiyonel programlama






#Isimsiz fonksiyonlar (Anonymous Functions)

def old_sum(a,b):
    return a + b
old_sum(4, 3)


new_sum = lambda a , b : a + b
new_sum(3, 5)

sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x : x[1])








#Vektorel Operasyonlar (Vectorel Operations)

#OOP

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab
    
    
#FP

import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b







# map     filter     reduce

#map

liste = [1,2,3,4,5]

for i in liste:
    print(i + 10 )   


list(map(lambda x : x + 10,liste))
#map verilen bir vektorun icerisinde belirli bir fonkisyonu calistirma imkani
#verir




#filter

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x : x % 2 == 0,liste))    
#filter sayesinde bolumden kalanin 0 olanlari inceledi
#orjinal degerlerini getirdi. sartlari saglayanlari filtreledi





#reduce

from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

reduce(lambda a,b : a + b,liste)
#sirali bir sekilde toplama yaptirmis olduk her ifadeyi topladik








#Modul Olusturmak

#moduller belirli amaclari getirmek icin birarada bulunan fonksiyonlar
#toplulugudur.



# =============================================================================
# import HesapModulu 
# 
# HesapModulu.yeni_maas(1000)
# 
# HesapModulu.yeni_maas(2000)
# 
# import HesapModulu as hm
# 
# hm.yeni_maas(5000)
# 
# from HesapModulu import yeni_maas
# 
# yeni_maas(10000)
# 
# import HesapModulu as hm
# 
# hm.maaslar
# 
# =============================================================================







#Hatalar / istisnalar (exceptions)

a = 10
b = 0 

#a/b #0 payda da olamaz hata verir.


try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da 0 olamaz.")




a = 10
b = "2"

#a+b

try:
    print(a+b)
except TypeError:
    print("Degisken tipleri uygun degil")
    
