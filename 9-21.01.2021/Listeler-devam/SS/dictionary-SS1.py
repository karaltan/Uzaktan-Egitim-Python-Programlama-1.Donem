sozluk = {'Bilim insani':'Aziz Sancar', 'Sair':'Mehmet Akif Ersoy', 'Astronom':'Ali Kuscu' }


meslekler=sozluk.copy()#a) sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız.
print(meslekler)

print(sozluk) #b) sozluk isimli sözlüğün değerlerini ekrana yazdırınız.


sozluk.clear() #c) sozluk isimli sözlüğü içi boş bir sözlük hâline getiriniz.
print(sozluk)

sozluk = {'Bilim insani':'Aziz Sancar', 'Sair':'Mehmet Akif Ersoy', 'Astronom':'Ali Kuscu' }
sozluk['Matematikci']='Cahit Arf' #ç) sozluk isimli sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz.
print(sozluk)

print('sozluk' in 'sanatci') #d) sozluk isimli sözlüğün içinde sanatçı anahtarının olup olmadığını sorgulayınız.

sozluk['Bilim insani']='Canan Dagdeviren' #e) sozluk isimli sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olarak değiştiriniz.
print(sozluk)

print(sozluk['Sair']) #f) sozluk isimli sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırınız.