#Örnek Problem: 
"""Mustafa 16, Mehmet 15 ve Zehra 14 yaşlarında olmak üzere üç çocuk bir araya gelip, 
misket oynamak istemişler. Sahip oldukları kutuda toplam 120 adet misket bulunmaktadır. 
Oyunlarının kuralı gereği her çocuk yaşlarının iki katı kadar misket alarak 
oyunu oynayabildiklerine göre kutuda kaç adet misket kalmıştır?"""

toplamMisket = 120
mustafa = 16 * 2
mehmet = 15 * 2
zehra = 14 * 2

kalanMisket = toplamMisket - mustafa - mehmet - zehra

print("Kutuda kalan misket sayısı:", kalanMisket)


# kaynak: https://www.msoguz.com/2019/06/python-saysal-veri-tipleri.html