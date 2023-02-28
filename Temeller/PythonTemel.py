#Sayilar ve Stringlere Giris
9
9.2
9+9
9*9

"Hello AI ERA"
print("Hello")

type(9)
type(9.2)
type("Yaser")

#Stringlere yakakindan bakalim

""
''

type(123)
type("123")

"a" + "b"
"a" "b"
"a" " b"
"a" + "-b"

"a"*3
"a "*3

#String Metodlara -Len()

gel_yaz = "gelecegi_yazanlar"
#del mvk

a = 9
b = 10
a*b

len(gel_yaz)

#String Metodlara - upper() & lower()

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
gel_yaz.isupper()

B = gel_yaz.upper()

B.isupper()


#String Metodlara - replace()

gel_yaz.replace("e","a")
gel_yaz.replace("a","e")


#String Metedlara - strip()

bio = " Yaser_Atalay "
bio2 = "**Yaser_Atalay**"

bio.strip()
bio2.strip("*")

#Metodlara Genel Bakis

dir(gel_yaz) #uzerine uygulanabilicek metodlar

gel_yaz.capitalize() #ilk harfi buyutur.
gel_yaz.title() #Her bir kelimenin ilk harfi buyuk olur


#SUBSTRINGLER

gel_yaz[0]

gel_yaz[0:3]

gel_yaz[9:17]

gel_yaz[3:7]

#degiskenler -- Variables

c = 9999
d = "ali_uzaya_git"

x = c*9
x*c

type(100)
type(100.20)
type(1+2j)

e = 100.25

#TYPE_DONUSUMLERI

toplama_bir = input() #input kullanicidan bilgi alir
toplama_iki = input()

type(toplama_bir)
type(toplama_iki)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)

int(11.0)

float(12)

str(12)

type(str(12))

#print fonkisyonu

print ("Hello AI ERA")

print ("Yaser","Atalay")

print ("Yaser","Atalay", sep = "_") #sep argumanýný kullandik.

print() # ?print bilgi alma islemi.


#ilk alistirmalara kadar olan bolum bitti..



#VERI YAPILARI

#Listeler

#[]
#list()

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,25]
type(liste)

list_genis = ["b",5,1.2,8,notlar]
len(list_genis)

type(list_genis[0])
type(list_genis[4])
type(list_genis[1])
list_genis[3]
list_genis[4]

tum_liste = [notlar,list_genis]

#del tum_liste


#Listeler - Eleman Islemleri

liste2 = [10,20,30,40,50]

liste2[1]

liste2[0:2]
liste2[:2]
liste2[2:]

liste3 = ["a",10,[20,30,40,50]]

liste3[2]

liste3[2][2]


#Listeler - Eleman degistirme


liste4 = ["ali","veli","ayþe","fatma"]
liste4[1] = "yaser"
liste4
liste4[:3] = "samet","selim","selin"
liste4
liste4 = liste4 + ["kemal"]

#del liste4[1]
liste4


#Listeler - liste metodlari

liste5 = ["irem","fadime","furkan"]

liste5.append("berk")
liste5

liste5.remove("berk")
liste5

liste5.insert(0, "ayse")
liste5 #irem 1 oldu ayse 0

liste5.insert(2, "kamil")
liste5 #degistirme degil ekleme yapar önce ki kayar

liste5.insert(len(liste5),"beren")
liste5 #listenin sonuna ekleme yapmýs olduk

liste5.pop(0)
liste5 #index ile silme islemi

liste6 = ["irem","fadime","ali","furkan","yaser","ali"]

liste6.count("ali") #kac tane ali var.

liste_yedek = liste6.copy() #Listenin bir kopyasý olusur.

liste6.extend(["a","b","c","d"])
liste6 #liste birlestirme metodu liste adý verilerek yada yazýlarak
liste_yedek #liste6ya yapýlan degisikler etkilemez

liste6.index("ali")

liste6.reverse()
liste6#elemanlarý terse çevermis olduk

liste6.sort()
liste6 #a-z sýralama yapmýs olduk sayýlarý kucukten buyuge sýralar


liste6.clear()
liste6 #listenin icini temizlemis olduk







#Veri yapilarý - Tuple

#tuple olusturma

t = ("ali","veli",1,2,3,[1,2,3,4])

t = "ali","veli",1,2,3,[1,2,3,4]

t = ("eleman",)
type(t)


#Tuple eleman islemleri

t[0:3]
#tuplelarda degisiklik yapýlamaz orjinalde kalýr








#Veri yailari - Dictionary (sozluk)

#index islemi yapýlamaz sirali degildir

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
#key degerleri ile neleri tuttugu verilerek yazilir
#string deger olmak zorunda degildir

len(sozluk)

sozluk2 = {"REG" : ["Regresyon Modeli",10],
          "LOJ" : ["Lojistik Regresyon",20],
          "CART" : ["Classification and Reg",30]}
#dictionary ile dizili bir yapi olusturduk

sozluk
sozluk2

#dictionary eleman islemleri

sozluk["REG"]
sozluk["CART"]

sozluk2["REG"]

sozluk3 = {"REG" : {"reg1" : 10,
                    "reg2" : 20,
                    "reg3" : 30},
          "LOJ" : {"loj1" : 10,
                   "loj2" : 20,
                   "loj3" : 30},
          "CART" : {"cart1" : 10,
                    "cart2" : 20,
                    "cart3" : 30}}
#ic ice gecmis sozlukler de olusturabiliriz

sozluk3["REG"]["reg1"]
sozluk3["CART"]["cart3"]




#dictionary - eleman eklemek degistirmek

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk#ekleme yapmis olduk

sozluk["REG"] = "Coklu dogrusal regresyon"
sozluk # degisiklik yapmýs olduk
#key kýsýmýna listeler atanamaz key yazýlýp karsýsýna atanabilir
#degiskenlik olmayanlar keye atinabilir ornegin tuplelar













#Veri yapilari - Setler

#sirasizdir,tekrar eden veri yoktur.

s = set()
s

liste7 = [1,"a",5,"ali"]
s = set(liste7)
s
#icerisinde tuple ve liste kullanabiliriz

ali = "lutfen_ata_bakma_uzaya_git"
s = set(ali)
s #elemanlarin hepsini tek tek alır tekrar etmez

liste8 = ["ali","mehmet","ali","suleyman","naber","nasılsın"]
s = set(liste8)
s
len(s)



#Set eleman ekleme cikarma

liste9 = ["gelecegi","yazanlar"]
s = set(liste9)
s

s.add("yaser")
s #ekleme islemi yapmis olduk

s.remove("gelecegi")
s #silme islemi yaptık

s.discard("gelecegi")
#setin icinde yoksa hata verme remove ile silerken yoksa hata verir



#Setler Klasik kume islemleri

# ==================================================
# difference() ile kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde olmayanlar
# bu ifadelere atama yapmadikca sadece ekrane basar
# _uptade eklersek mesela intersection_update gibi
# o zaman atama yapmis olur _update kullanılınca
# ==================================================

set1 = set([1,3,5])
set2 = set([1,2,3])

set1 - set2
set1.difference(set2)
#farkli olan sayi geldi


set1.intersection(set2)
set1 & set2
#aynı olan elemanlar her iki kumede de olan elemanlar


set1.union(set2)
#birlesimlerini gösterir

set1.symmetric_difference(set2)
#ikisinde olmayanlar birinde var digerinde yoksa




#Setlerde sorgu islemleri

set3 = set([7,8,9])
set4 = set([5,6,7,8,9,10])

set3.isdisjoint(set4)
#iki setin kesisimi bos mu 

set3.issubset(set4)
#set3 set4dün icinde yer aliyor mu ? alt kumesi mi ?

set3.issuperset(set4)
#set3 set4 du kapsiyor mu













#Foksiyona giris ve Fonksiyon okuryazarligi

#foksiyon belirli amaclari yerine getiren islecler
#foksiyon okur yazarligi fonksiyona isilkin dokimantasyona ulasmak


def kare_al(y):
    print(y**2)
    
kare_al(3)
#fonksiyon olusturma islemi yaptik.

def kare_al2(y):
    print("Girilen Sayinin Karesi : "+ str(y**2))

kare_al2(4)

def kare_al3(y):
    print("Girilen Sayi : "+ str(y) +" Girilen Sayinin Karesi : "+ str(y**2))
    
kare_al3(5)
#Cikti notlari üretme bu sikelide yapiliyor


def carpma_yap(e,r):
    print(e*r)
    
carpma_yap(2, 4)
#2 argumanlı fonksiyon

def carpma_yap2(k,o=5):
    print(k*o)

carpma_yap2(2)
carpma_yap(2,8)
#on tanimli argumanlı fonksiyon


def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
    
direk_hesap(50, 20, 80)
#fonksiyonlarin ciktilarini direkt kullanamayiz kullanmak icin return kullanılır

def direk_hesap2(isi,nem,sarj):
    return (isi+nem)/sarj

direk_hesap2(50, 10, 80)
#return kullanarak cikti olarak alinip kaydedilebilir islem yapilabilir













#local ve global degiskenler

x = 10
y = 20
#global degisken


def carpma(x,y):
    return x*y
#local degisken bir foksiyonun etkisinde
carpma(2,5)



#local etki alanindan global etki alanini degistirmek

x1 = []

def eleman_ekle(y):
    x1.append(y)
    print(str(y)+ " İfadesi eklendi")
#once kendi icinde arar localde bulamayinca foksiyonun icinde yani
#bulamadiginda global alana bakar ve ektiler
eleman_ekle(1)
eleman_ekle("ali")











#Karar kontrol yapilari


#true false sorgulari

sinir = 50000

sinir == 4000
#sinir 4000 mi




#if

gelir = 10000

if gelir < sinir:
    print("Gelir sinirdan kucuk")



#else


if gelir > sinir:
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk")
    


if gelir == sinir:
    print("Gelir sinira esittir")
else:
    print("Gelir sinira esit degildir")




#elif

sinir =50000
gelir1 =60000
gelir2 =50000
gelir3 =35000

if gelir1 > sinir:
    print("Tebrikler")
elif gelir1 < sinir:
    print("Uyarı")
else:
    print("Takibe devam")


if gelir3 > sinir:
    print("Tebrikler")
elif gelir3 < sinir:
    print("Uyarı")
else:
    print("Takibe devam")
    
if gelir2 > sinir:
    print("Tebrikler")
elif gelir2 < sinir:
    print("Uyarı")
else:
    print("Takibe devam")
    




#Mini uygulama

sinir = 50000
magaza_adi = input("Magaza adi nedir ? ")
gelir =int(input("Gelirinizi giriniz : "))

if gelir > sinir:
    print("Tebrikler "+magaza_adi+" promosyon kazandınız")
elif gelir < sinir:
    print("Uyarı cok dusuk gelir : "+ str(gelir))
else:
    print("Takibe devam")













#DONGULER - for

ogrenci = ["ali","berk","asli","irem"]

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)
    
maaslar = [10000,12000,13000,13500,15000]

for i in maaslar:
    print(i)
    
    
    

#dongu ve fonksiyon birlikte kullanim

#maaslara %20 zama yapilacak

def maas_zam(x):
    print(x*20/100+x)
    
for i in maaslar:
    maas_zam(i)
    



#if for ve fonksiyon birlikte kullanimi

maaslar = [10000,12000,13000,13500,15000]

#maaslari 13binden fazla olana %10 az olanlara %20 zam

def maas_ust(x):
    print(x*10/100+x)
    
def maas_alt(x):
    print(x*20/100+x)
    
for i in maaslar:
    if i <= 13000:
        maas_alt(i)
    else:
        maas_ust(i)
        
        
        
        
        
        
        
        
        
#break ve continue

#dongulerde belirli sart saglandiginda ifade yakanlanmak yada 
#gormezden gelinmesi istenebilir

maaslar = [10000,12000,13000,13500,15000,12000,18000,11000,19000]
maaslar.sort()
maaslar

for i in maaslar:
    if i ==13000:
        print("Kesildi")
        break
    print(i)
#break donguyu durdurur
    
for i in maaslar:
    if i ==13000:
        continue
    print(i)    
#continue sarti saglayani atla devam et






#while
#while oldugu surece bu sart saglandigi surece

sayi = 1

while sayi <10:
    sayi += 1
    print(sayi)

