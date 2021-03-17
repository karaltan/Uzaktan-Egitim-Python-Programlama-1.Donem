x = int(input("1.sayıyı yaz: "))
y = int(input("2.Sayıyı Yaz: "))
sayiToplam = 0
for i in range(x+1,y):
    sayiToplam = sayiToplam + int(i)
print("{} ile {} arasındaki sayıların toplamı: {}" .format(x,y,sayiToplam))




