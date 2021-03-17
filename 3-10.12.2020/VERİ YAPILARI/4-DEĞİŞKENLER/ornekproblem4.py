#Örnek Problem:
"""
Cumartesi-Pazar günleri çalışmıyoruz.
Dolayısıyla ayda 22 gün çalışıyoruz.
Evden işe gitmek için kullandığımız vasıtanın ücreti 1.5 TL
İşten eve dönmek için kullandığımız vasıtanın ücreti 1.4 TL

Aylık yol masrafımızı hesaplayabilmek için gidiş ve dönüş ücretlerini toplayıp, 
bunları çalıştığımız gün sayısıyla çarpmamız yeterli olacaktır."""
günsayısı=22
gidişücreti=1.5
dönüşücreti=1.4

masraf = günsayısı*(gidişücreti + dönüşücreti)
print (masraf)
# kaynak: https://python-istihza.yazbel.com/etkilesimli_python.html#karakter-dizilerine-giris