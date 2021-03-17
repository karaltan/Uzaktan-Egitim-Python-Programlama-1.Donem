
# abonenin numarasını ve tüketim miktarını alın. 
# birim fiyat 4 lira ise toplam faturasını hesaplayın

#problemde verilen değer
birimfiyat=4
# dışarıdan girilecekler
abonenumarası=input ("abone numamrasını giriniz:")
tuketim=int(input ("tüketim bilgisini giriniz:"))

fatura_tutarı=birimfiyat*tuketim

print ("Sayın {0}, nisan ayı faturanız {1} tl dir".format(abonenumarası,fatura_tutarı))