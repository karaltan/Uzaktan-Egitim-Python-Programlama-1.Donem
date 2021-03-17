# Bir marketteki bir paket çayın fiyatı 10 TL’dir.  
# Müşterinin kaç çay aldığını soran ve ödeyeceği tutarı hesaplayan prg.
# toplam tutara KDV %8 eklenir

cay=10
kdvorani=8/100 # kdv=0.08

adet=int(input('kaç adet çay aldınız:'))

tutar=adet*cay
print('kdv öncesi tutar:',tutar)

ekodenecektutar=(cay*adet)*kdvorani
print('ödenecek kdv tutarı=',ekodenecektutar)

anatutar=tutar+(tutar*kdvorani)
print('ödenecek tutar=',anatutar)
#######################################################
print('ödenecek tutar=',(cay*adet)+ekodenecektutar)
