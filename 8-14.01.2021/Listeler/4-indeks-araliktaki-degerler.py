# Listeden belli bir aralık almak

# liste[başlangıç indeksi:bitiş indeksi] yapısı kullanılır

asal_sayilar=[2, 3, 5, 7, 11, 13, 17, 19, 23]

print(asal_sayilar[0:3]) # [2, 3, 5]

print(asal_sayilar[1:4])
''' indeksi 1 olan elemandan başlayarak indeksi 4 olan elemana (4 dâhil değil) kadar ekrana yazdırır.
Dolayısıyla ekran çıktısı [3, 5, 7] olacaktır. '''

print(asal_sayilar[5:]) # 5ten sonraki hepsi demektir [13, 17, 19, 23]

print(asal_sayilar[:5]) # baştan 5.indise kadar demektir(5. dahil değildir) [2, 3, 5, 7, 11]

# ATLAYARAK ALMAK
asal_sayilar2=[2, 3, 5, 7, 11, 13, 17, 19, 23]
print(asal_sayilar2[0:6]) # [2, 3, 5, 7, 11, 13]
print(asal_sayilar2[0:6:2]) # baştan 6.ya kadar 2 atlayarak getirir (6.dahil değil)
# [2, 3, 5, 7, 11, 13] ELEMANLARINI 2 ADIM ATLAYARAK AL = [2, 5, 11]

print(asal_sayilar2[0:7:2]) # [2, 3, 5, 7, 11, 13, 17] -> [2,5,7,13]


