"""Soru: Beden kütle endeksi kilo/(boy^2) formülü ile hesaplanarak bireyin kilolu 
normal zayıf veya obez sınıfına girdiği ile ilgili sonuç verir. 
Kütle endeksi kodunu yazınız."""

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

endeks  = kilo/(boy**2)

print('beden kütle endeksin=',endeks)
# normalde if konusu yok ama bu program için aşağıdaki gibidir...
endeks=endeks*10000
if endeks<18.5:
    print("n Zayıf")
elif endeks > 18.5 and endeks <=25:
    print("n Normal")
elif endeks > 25 and endeks <=30:
    print("n Kilolu")
elif endeks > 30:
    print("n Obez")