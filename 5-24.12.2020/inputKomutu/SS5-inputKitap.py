"""
Kullanıcıya adını ve bu yıl kaç kitap okuduğunu sorunuz. 
Aşağıdaki gibi ekran çıktısı üretiniz
…(ad)….., bu yıl …… kitap okudu.
"""
ad=input("adınız nedir?:") #metinsel
kitap=int(input("bu yıl kaç kitap okudunuz")) #sayısal

print("{0}, bu yıl {1} kitap okudu".format(ad,kitap))

print(ad," bu yıl ",kitap," kitap okudu")
