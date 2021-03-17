
# Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği
# vizenin yüzde30u, finalin yüzde70ini al

vize =float( input('Vize Notunuz : '))
final = float (input('Final Notunuz : '))

# vizenin yüzde30u demek= vize*30/100=vize*0.3
# finalin yüzde70i demek= final*70/100=final*0.7
ortalama=(vize*30/100)+(final*0.7)

print("Ortalama : ",ortalama)
print("Ortalama :{0} ".format(ortalama))

#BOOL değişkeni: TRUE(evet) veya FALSE(hayır)
print(ortalama>=50) #ortalama 50ye eşit veya büyükse True yazsın, aksi False yazsın