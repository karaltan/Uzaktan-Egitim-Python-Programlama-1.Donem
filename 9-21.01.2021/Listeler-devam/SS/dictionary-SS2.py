onemli_telefonlar = {'Acil Cagri Merkezi':'112', 'Polis Imdat':'155', 'Milli Egitim Bakanligi Iletisim Merkezi':'444 0 632' }

print(onemli_telefonlar) #a) önemli_tefonlar isimli sözlüğün değerlerini ekrana yazdırınız.



onemli_telefonlar.pop('Acil Cagri Merkezi') #c) önemli_telefonlar isimli sözlükten Acil Çağrı Merkezi anahtarını ve değerini siliniz.
print(onemli_telefonlar)

    
print('onemli_telefonlar' in 'Saglik Bakanligi') #ç) önemli_telefonlar isimli sözlükte Sağlık Bakanlığı İletişim Merkezi olup olmadığını sorgulayınız.


onemli_telefonlar.clear()#d) önemli_telefonlar isimli sözlüğü içi boş bir sözlük hâline getiriniz.
print(onemli_telefonlar)

#!!!!!! b şıkkı en sonda yazılmıştır !!!!!! 

del onemli_telefonlar #b) önemli_telefonlar isimli sözlüğü siliniz.
print(onemli_telefonlar)
