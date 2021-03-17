# 4.VERİ YAPILARI
# 4.3.3 Listeler
# İndeks kullanımı
# Aralık Alma
# Sıra Sizde Soruları
# liste[başlama:bitiş:atlama]

asal_sayilar=[2, 3, 5, 7, 11, 13, 17, 19, 23]
print(asal_sayilar[::2]) # baştan sona 2 atlayarak demektir
# [2, 5, 11, 17, 23]

tek_sayilar=[3, 5, 7, 9, 11, 13, 15, 17, 19]
print(tek_sayilar[0:6]) # [3, 5, 7, 9, 11, 13]
print(tek_sayilar[2:5]) # [7, 9, 11]
print(tek_sayilar[3:8]) # [9, 11, 13, 15, 17]
print(tek_sayilar[:5])  # [3, 5, 7, 9, 11]
print(tek_sayilar[3:])  # [9, 11, 13, 15, 17, 19] 
print(tek_sayilar[0:8:2]) # [3, 7, 11, 15]
print(tek_sayilar[::3]) # [3, 9, 15]

# bizim örneğimiz
print(tek_sayilar[::2]) # [3, 7, 11, 15, 19]