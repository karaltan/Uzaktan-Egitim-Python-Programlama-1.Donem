isim = input("isminizi yazınız: ")
sayac = 1
while True:
    if isim=="X":
        print("Programdan Çıkılıyor...")
        break
    else:
        print("merhaba {} sen {}. kişisin" .format(isim,sayac))
        sayac = sayac + 1
        isim = input("isminizi yazınız: ")

