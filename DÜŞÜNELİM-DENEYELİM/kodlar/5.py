t = int(input("sıcaklık giriniz: "))
if t<0:
    hal = "katı"
elif t>=0 and t<100:
    hal = "sıvı"
else:
    hal = "gaz"
print(hal)

