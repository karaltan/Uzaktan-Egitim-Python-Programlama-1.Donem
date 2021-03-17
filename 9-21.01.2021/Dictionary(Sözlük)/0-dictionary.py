# dictionary(sözlük):
""" Python programlama dilinde sırasız, değiştirilebilir ve belirli bir konuma sahip koleksiyonlar sözlük olarak
adlandırılır. Sözlükler süslü (ya da kırlangıç{}) parantezler arasına yazılır. """

# kullanımı: sozluk_adi={anahtar(key):deger(value)}
sozlugum={} # boş sözlük

sozluk = {"Mesleğiniz":"Öğrenci", "Alanınız":"Bilişim", "Yaşadığınız Yer":"Ankara"}
print(sozluk)
# {'Mesleğiniz': 'Öğrenci', 'Alanınız': 'Bilişim', 'Yaşadığınız Yer': 'Ankara'}
sozluk2 = {
            "Mesleğiniz":"Öğrenci", 
            "Alanınız":"Bilişim", 
            "Yaşadığınız Yer":"Ankara",
            "Yaş":35
        }
print(sozluk2)
# {'Mesleğiniz': 'Öğrenci', 'Alanınız': 'Bilişim', 'Yaşadığınız Yer': 'Ankara', 'Yaş': 35}

# key ve values
sozluk = {"Mesleğiniz":"Öğrenci", "Alanınız":"Bilişim", "Yaşadığınız Yer":"Ankara"}
print(sozluk.keys())
print(sozluk.values())
# dict_keys(['Mesleğiniz', 'Alanınız', 'Yaşadığınız Yer'])
# dict_values(['Öğrenci', 'Bilişim', 'Ankara'])


# Örnek: plakalar ve şehirler
palaka = {
            1:"ADANA", 
            2:"ADIYAMAN", 
            3:"AFYON",
            41:"KOCAELİ",
            81:"DÜZCE",           
        }
print(palaka)
# Örnek: str ve int
notlar = {
            "numara":729, 
            "adsoyad":"altan karaalp", 
            "fizik":[100,50,85],
            "bilişim":[40,50,55]
        }
print(notlar)

# ingilizce türkçe
kelimeler={
            "apple":"elma",
            "computer":"bilgisayar",
            "yellow":"sarı"
        }
print(kelimeler)

