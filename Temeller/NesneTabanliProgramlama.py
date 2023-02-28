# NESNE YONELIMLI PROGRAMLAMA

#Sinif nedir?
#Benzer ozellikler ortak amaclar tasiyan gruplar olusturmak icin kullanilir

class VeriBilimci3():
    print("Bu bir siniftir")

    
#Sinif Ozellikleri

class VeriBilimci2():
    bolum =""
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []
#Siniflarin ozelliklerine erismek
VeriBilimci2.bolum
VeriBilimci2.sql
#Siniflarin ozelliklerini degistirmek
VeriBilimci2.sql = "Hayır"
VeriBilimci2.sql


#Sinif orneklendirmesi
#Genel class ozelliklerini tasiyan alt kumeler olusturma islemine denir

ali = VeriBilimci2()

ali.sql
ali.deneyim_yili
ali.bolum

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci2()
veli.sql

veli.bildigi_diller
#ornekledigimiz bir deger uzerinden yapmis oldugumuz degisiklik genel anlamda
#sinifin özelliklerini eklidedi ve yine bu sinifin ozelliklerini tasiyan
#bir ornegin ozelliklerine erismek istedigimiz de bize bende de bu var dedi
#aslinda olmamasina ragmen


#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum =""
    sql = "Evet"
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
        self.sql = "Evet"
        self.deneyim_yili = 0
#Yukarida verdigimiz kod her bir ornegin kendi icinde degisen ozelliklerden
#olusabildiginin bilgisini vermek.
#self orneklemleri temsil eder baska bir sey yazilabilir tavsiye edilmez
#ornek ve normal isimler farkli olmasi istenir biz oyle yapmadik

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

veli.bildigi_diller.append("Python")
veli.bildigi_diller

ali.bildigi_diller
ali.bildigi_diller.append("R")
ali.bildigi_diller

VeriBilimci.bildigi_diller

VeriBilimci.bolum
ali.bolum
veli.bolum

ali.bolum = "istatistik"
veli.bolum = "ybs"

ali.bolum
veli.bolum
VeriBilimci.bolum




#Ornek metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
        self.sql = "Evet"
        self.deneyim_yili = 0
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

ali.dil_ekle("R")
veli.dil_ekle("PYTHON")







#Miras yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
#veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""
        
mar1 = Marketing()
#mar1.


class Employees():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
ali = Employees("Ali", "Kara", "Bandırma")
ali.Address
ali.LastName
        
