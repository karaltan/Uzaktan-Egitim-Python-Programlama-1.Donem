# LEN() FONKSİYONU:
# Listelerin eleman sayısına ulaşmak için İngilizce uzunluk anlamına gelen 
# length kelimesinin kısaltması olan len() fonksiyonu kullanılır

sayi=[20, 40, 60, 80]
print(len(sayi))
print('{0} adet sayı vardır'.format(len(sayi)))


listem=[5,9,10,"altan",82.5]
print(len(listem))

# eleman sayısının 1 eksiği son indisi verir, eleman sayısı:5, son indis:4

##############################################################33
# SORU: Altan KARAALP yazıldığında
# A************ şeklinde yazsın

isim=input('isminiz:')

print(isim[0])
# string değerlerde * operatörü türetme yapar
# print('a'*9)

print ('Merhaba sayın ', isim[0]+'*'*(len(isim)-1))