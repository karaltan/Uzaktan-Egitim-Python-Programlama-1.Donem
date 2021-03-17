import os
from time import sleep

# Terminal Penceresini Temizleyen fonksiyon
def clear():
    """
        Bu fonksiyon terminal penceresini ilk haline getirir.
    """
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim sistemi Linux veya Mac ise
    else:
        _ = os.system('clear')

def anaMenu():
    clear()
    print("---------------   Proje-1'e Hoşgeldiniz...   ---------------")
    print("Şirketinizde bulunan personellerin" \
        " kaydını tutan bir program.\n")
    print("İşlem Seçenekleri;")
    print("1. Yeni Personel")
    print("2. Personel Bilgisi")
    print("3. Personel Sil")
    print("4. Programı Sonlandır.")

while (True):
    anaMenu()
    veri = input("Lütfen yapmak istediğiniz işlemi seçin: ")
    if(veri == '4'):
        print("Program başarılı bir şekilde sonlandırıldı.")
        break
    else:
        print("Bu seçenek henüz hazır değil.")
        print("Lütfen daha sonra deneyiniz.")
        sleep(3)