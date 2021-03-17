""" Bir otelde kırk adet oda vardır. Her oda da ikişer yatak bulunmaktadır.
Dün akşam oteli kullanan müşteriler nedeniyle otel odalarının yarısı temizlik nedeniyle servis dışıdır.
Sabaha karşı yirmi yatak, personel tarafından temizlenerek hazır hale getirilmiştir.
Aynı zamanda otel 5 odalık müşterisini kabul etmiştir.
Bu durumda müşterilere kiralanabilecek kaç yatak vardır? """
# Değişkensiz Kullanım Örneği
sonuc = 40 * 2 / 2 + 20 - 5 * 2
print("Kiralanabilecek Yatak Sayısı: ", sonuc)

# Sonuç : Kiralanabilecek Yatak Sayısı:  50.0

# Değişkenli kullanım örneği
ToplamYatakSayisi = 40 * 2
ServisDisiYatakSayisi = 2
TemizlenenYatakSayisi = 20
KiralananYatakSayisi = 5 * 2
KalanYatakSayisi = (ToplamYatakSayisi / ServisDisiYatakSayisi) + TemizlenenYatakSayisi - KiralananYatakSayisi

print("Kiralanabilecek Yatak Sayısı: ", KalanYatakSayisi)
