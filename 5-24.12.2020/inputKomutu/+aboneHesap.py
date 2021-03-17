
birimfiyat=4

abonenumarası=input ("abone numamarsını giriniz:")
tuketim=int(input ("tüketim bilgisini giriniz:"))

fatura_tutarı=birimfiyat*tuketim

print ("Sayın {0}, nisan ayı faturanız {1} tl dir".format(abonenumarası,fatura_tutarı))