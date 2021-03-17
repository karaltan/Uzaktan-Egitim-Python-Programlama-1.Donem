paketFiyat = 10
kdv = 0.08
paketSay = int(input("Kaç Paket Alınacak: "))
fiyat = paketFiyat*paketSay

if paketSay < 10:
    indirim = 0
elif paketSay>=10 and paketSay<50:
    indirim = fiyat*0.05
elif paketSay>=50 and paketSay<100:
    indirim = fiyat*0.1
else:
    indirim = fiyat*0.15
    
fatura = fiyat-indirim
fatura = fatura + (fatura*kdv)  
print(fatura)

