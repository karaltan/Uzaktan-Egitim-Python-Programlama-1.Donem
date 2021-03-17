
#Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği
# vizenin yüzde30u, finalin yüzde70ini al

vize =float( input('Vize Notunuz : '))
final = float (input('Final Notunuz : '))

ortalama=(vize*30/100)+(final*0.7)

print("Ortalama :{0} ".format(ortalama))
