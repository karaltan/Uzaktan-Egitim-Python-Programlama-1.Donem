"""Girilen sayının karesini ve küpünü ekrana yazdırınız. Ekran çıktısı aşağıdaki gibi olsun.
....... sayısının karesi ......dır.
....... sayısının küpü .......dır.

"""

sayi=int(input("sayinizi giriniz:"))

karesi=sayi**2 		# veya karesi=sayi*sayi
kupu=sayi*sayi*sayi 	# veya kupu=sayi**3

print(sayi," sayısının karesi ",karesi," dir")
print(sayi," sayısının küpü ",kupu," dir")

#parametreli kullanım
print("{0} sayısının karesi {1} dir".format(sayi,karesi))
print("{0} sayısının küpü {1} dir".format(sayi,kupu))


