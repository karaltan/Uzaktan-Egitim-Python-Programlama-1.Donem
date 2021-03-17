#Örnek Problem:
"""Bir manavda Muzun kilosu 1.75 Türk Lirası olduğunu varsayalım. 
A müşterisi 2.5 kg, 
B müşterisi 2 kg, 
C müşterisi ise 4.25 kg Muz aldığında, 
manavın üç müşterisinden elde ettiği kazanç nedir? """
# Muzun Kilo Fiyatı
muzFiyati = 1.75

# Müştelerin Aldığı Muzların Kilo Hesabı
musteriA = 2.5
musteriB = 2
musteriC = 4.25

# Müşterilerin aldığı kilo fiyatı
kazancA = musteriA * muzFiyati
kazancB = musteriB * muzFiyati
kazancC = musteriC * muzFiyati

# Manavın Kazancını Hesaplama
toplamKazanc = kazancA + kazancB + kazancC
print("Manavın Kazancı:", toplamKazanc, "TL")
print("Veri tipi:", type(toplamKazanc))



# kaynak: https://www.msoguz.com/2019/06/python-saysal-veri-tipleri.html