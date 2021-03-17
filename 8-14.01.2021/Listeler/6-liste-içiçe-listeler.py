# bir listeyi yazarken başka listeyi dahil etmek
meyveler=["elma", "çilek", "armut"]
alisveris_listesi=["süt", "peynir", meyveler]
print(alisveris_listesi)
# ['süt', 'peynir', ['elma', 'çilek', 'armut']]
##################################################################
# farklı listeleri bir liste yapmak
bellekler=["RAM", "ROM"]
ekran_kartlari=["Paylaşımlı", "Paylaşımsız"]
sabit_diskler=["SSD"]
birimler=bellekler, ekran_kartlari, sabit_diskler
print(birimler)
# (['RAM', 'ROM'], ['Paylaşımlı', 'Paylaşımsız'], ['SSD'])

print(birimler[0][1]) # ROM
print(birimler[0][1], birimler[2][0]) # ROM SSD
##################################################################
# örnek: 
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller + yorumlanan_diller
print(programlama_dilleri)
##################################################################

