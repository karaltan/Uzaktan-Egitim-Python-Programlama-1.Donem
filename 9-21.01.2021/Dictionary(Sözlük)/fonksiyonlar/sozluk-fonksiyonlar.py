# sözlükte kullanılan fonksiyonlar:
############################################################################
# Yeni değer eklemek
donanim = {"Türü":"RAM", "Tipi":"DDR4", "Kapasitesi":"8 GB"}
donanim["Hızı"]="2400 MHz" #burada ekleme işlemi yapılmıştır.
print(donanim)
# Ekran Çıktısı: {‘Türü’: ‘RAM’, ‘Tipi’: ‘DDR4’, ‘Kapasitesi’: ‘8 GB’, ‘Hızı’: ‘2400 MHz’}
############################################################################
# POP(): anahtar silmek
donanim = {"Türü":"RAM", "Tipi":"DDR4", "Kapasitesi":"8 GB"}
donanim.pop("Kapasitesi") #burada silme işlemi yapılmıştır.
print(donanim)
# Ekran Çıktısı: {‘Türü’: ‘RAM’, ‘Tipi’: ‘DDR4’}
############################################################################
# DEL(): sözlüğü tamamen silmek
donanim = {"Türü":"RAM", "Tipi":"DDR4", "Kapasitesi":"8 GB"}
del donanim
print(donanim) # name 'donanim' is not defined
############################################################################
# CLEAR() : içindekileri silmek
donanim = {"Türü":"RAM", "Tipi":"DDR4", "Kapasitesi":"8 GB"}
donanim.clear()
print(donanim)
############################################################################
# COPY(): kopyalamak
donanim = {"Türü":"RAM", "Tipi":"DDR4", "Kapasitesi":"8 GB"}
yeni_donanim=donanim.copy()
print(yeni_donanim)
############################################################################