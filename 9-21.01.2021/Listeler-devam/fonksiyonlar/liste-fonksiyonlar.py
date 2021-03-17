# LİSTE FONKSİYONLARI

donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
print(donanim)
##################################################################################
# 1.Append(eklemek): Listenin sonuna eleman eklemek için kullanılır
donanim.append("monitör") #burada append fonksiyonu ile eleman eklenmiştir.
print(donanim)

# sayısal değer eklenebilir mi?
donanim.append(55) # evet eklenebilir
print(donanim) 
# Çıktı: ['yazıcı', 'klavye', 'işlemci', 'bellek', 'sabit disk', 'monitör', 55]
##################################################################################
# 2.Extend(uzatmak/genişletmek): Listeleri birleştirmek için kullanılır. 
yazilim=["işletim sistemi", "web tarayıcı"]
#donanim.extend(yazilim) #burada extend fonksiyonu ile listeler birleştirilmiştir.
#print(donanim)

yenilistem=donanim+yazilim # bu şekilde de olabilirdi
print(yenilistem)
##################################################################################
# 3.Insert: Listenin belirtilen konumuna (indeksine) eleman eklemek için kullanılır
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
print(donanim)
donanim.insert(2, "tarayıcı") #indeksi 2 olan konuma(klavye ile işlemci arasına) tarayıcı eklenmiştir.
print(donanim)
# Çıktı: ['yazıcı', 'klavye', 'tarayıcı', 'işlemci', 'bellek', 'sabit disk']
# SORU: en sona eleman eklemek
donanim=["yazıcı","araeleman1","araeleman2","klavye", "işlemci", "bellek", "sabit disk"]
donanim.insert(len(donanim),"mouse")
print(donanim)
# Çıktı: ['yazıcı', 'araeleman1', 'araeleman2', 'klavye', 'işlemci', 'bellek', 'sabit disk', 'mouse']
##################################################################################
# 4.Remove: Listenin içindeki değeri verilen elemanı siler.
# Örnek : Listedeki klavye elemanını siliniz.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
donanim.remove("klavye") # değeri klavye olan eleman silinmiştir.
print(donanim)
# Ekran çıktısı: [‘yazıcı’, ‘işlemci’, ‘bellek’, ‘sabit disk’] 

# NOT: Liste içindeki herhangi bir eleman indis numarasına göre de silinebilir.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
donanim.remove(donanim[1]) # indis numarası 1 olan eleman “klavye” silinmiştir.
print(donanim)
# Ekran çıktısı: [‘yazıcı’, ‘işlemci’, ‘bellek’, ‘sabit disk’] 
##################################################################################
# 5.Pop: Listede belirtilen konumdaki (indeks) elemanı siler
# Örnek: indeksi 3 olan elemanı siliniz.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
silinen=donanim.pop(3)
print('silinen='+silinen)
print(donanim)
# Çıktı: [‘yazıcı’, ‘klavye’, ‘işlemci’, ‘sabit disk’]

# NOT: pop fonksiyonu ile indeks belirtilmezse son eleman silinir. 
# donanim.pop() yazılırsa son eleman olan sabit disk silinir.
##################################################################################
# 6.Clear: Listenin tüm elemanlarını siler ve boş bir liste ortaya çıkarır.
# Örnek : Listenin tüm elemanlarını siliniz.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
donanim.clear()
print(donanim)
# Ekran Çıktısı: [ ]
##################################################################################
# 7.Index: Bir elemanın listedeki konumunu bulur.
# Örnek : Listedeki "sabit disk" elemanının indeksini bulunuz.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
print(donanim.index("sabit disk"))
# Ekran Çıktısı: 4

# print(donanim.index("mouse")) # listede olmayan elemanı sorgularsak
# ValueError: 'mouse' is not in list
##################################################################################
# 8.Count: Listede belirtilen elemandan kaç adet olduğunu bulur.
# Örnek : Listenin en sonuna bir tane daha klavye elemanı ekleyiniz ve count ile kaç tane klavye elemanı
# olduğunu bulunuz.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk","klavye"]
say=donanim.count("klavye")
print(say)
# Ekran Çıktısı: 2

# NOT: listenin eleman sayısını len() fonksiyonu ile buluyorduk...
##################################################################################
# 9. Sort: Listenin içindeki elemanları sıralar. Burada liste elemanlarının string, int vb. veri tiplerine uygun
# olarak sıralanacağı unutulmamalıdır.
# Örnek : donanim listesini sıralayınız.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
donanim.sort()
print(donanim)
# Ekran Çıktısı: [‘bellek’, ‘işlemci’, ‘klavye’, ‘sabit disk’, ‘yazıcı’]

# NOT: Sıralamanın küçükten büyüğe değil de tam tersi olması için reverse=True parametresi verilebilir. 
# İlgili kod satırını donanim.sort(reverse=True) şeklinde değiştirerek deneyiniz.
donanim.sort(reverse=True)
print(donanim)
# Çıktı: ['yazıcı', 'sabit disk', 'klavye', 'işlemci', 'bellek']

# sorted(liste_adi) bize siralanmis bir sekilde parametre olarak verilen listeyi döndürecektir
harfler = ['d', 'c','b','a','eee','fb','gs']
siralanmis_liste= sorted(harfler)
print harfler
print siralanmis_liste
# Sonuc
# ['d', 'c', 'b', 'a', 'eee', 'fb', 'gs']
# ['a', 'b', 'c', 'd', 'eee', 'fb', 'gs']
##################################################################################
# 10. Reverse: Listeyi sondan başa doğru yani ters yazar.
# Örnek : donanim listesini ters bir şekilde yazdırınız.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
donanim.reverse()
print(donanim)
# Ekran Çıktısı: [‘sabit disk’, ‘bellek’, ‘işlemci’, ‘klavye’, ‘yazıcı’]
##################################################################################
# 11. Copy: Listeyi yeni bir liste olarak kopyalar.
# Örnek : donanim listesini yeni_donanim listesine kopyalayarak ekrana yazdırınız.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
yeni_donanim=donanim.copy()
print(yeni_donanim)
# Ekran Çıktısı: [‘yazıcı’, ‘klavye’, ‘işlemci’, ‘bellek’, ‘sabit disk’]
##################################################################################
# 12. Del: indeksi verilen elemanı siler. Pop fonksiyonuna benzer bir fonksiyon olmasına 
# rağmen kullanımı farklıdır.
# Örnek : indeksi 2 olan elemanı silerek listeyi ekrana yazdırınız.
donanim=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
del donanim[2]
print(donanim)
# Ekran Çıktısı: [‘yazıcı’, ‘klavye’, ‘bellek’, ‘sabit disk’]

# Örnek: aralık silmek
harfler = ['a', 'b','c', 'd','e','f','g']
del harfler[1:4] # 1,2 ve 3. indisi siler
print (harfler)
 # Sonuc ['a', 'e', 'f', 'g']

# listeyi tamamen silmek
 harfler = ['a', 'b','c', 'd','e','f','g']
 del harfler
 print (harfler)

 