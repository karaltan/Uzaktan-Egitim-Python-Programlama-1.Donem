# 4.VERİ YAPILARI
# 4.3.3 Listeler
# Listelerin Fonksiyonları
# Sıra Sizde Soruları
# 1. Adı ders, elemanları sırasıyla B,İ,L,İ,Ş,İ,M olan bir liste oluşturarak aşağıdaki işlemleri yapınız.

ders=['b','i','l','i','ş','i','m']
# a) Listeyi alfabetik olarak sıralayınız.
ders.sort()
print(ders)
# b) Listeyi tersten yazdırınız.
ders=['b','i','l','i','ş','i','m']
ders.reverse()
print(ders)
# c) Listede kaç tane İ elemanı olduğunu bulunuz.
ders=['b','i','l','i','ş','i','m']
print(ders.count('i'))
# d) Gerekli harfleri silerek listeyi B,İ,L,İ,M hâline getiriniz.
ders=['b','i','l','i','ş','i','m']
ders.pop(5)
print(ders)
ders.pop(4)
print(ders)
# e) ders listesini alan listesine kopyalayarak ekrana alan listesini yazdırınız.
ders=['b','i','l','i','ş','i','m']
alan=ders.copy()
print("alan={0}".format(alan))
# f) Listenin tüm elemanlarını siliniz.
ders=['b','i','l','i','ş','i','m']
ders.clear()
print(ders)
# g) L elemanının indeksini bulunuz
ders=['b','i','l','i','ş','i','m']
print(ders.index('l'))