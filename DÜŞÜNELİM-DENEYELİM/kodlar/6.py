negatifSay = 0
pozitifSay = 0
while True:
    x = int(input("bir sayı gir: "))
    if x ==0:
        break  
    if x<0:
       negatifSay = negatifSay + 1
    else:
        pozitifSay = pozitifSay + 1
print("Toplam negatif sayı:",negatifSay)
print("Toplam pozitif sayı:",pozitifSay)
    
