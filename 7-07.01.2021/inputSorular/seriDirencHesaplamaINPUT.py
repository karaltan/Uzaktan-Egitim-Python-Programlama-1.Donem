""" dışarıdan girilen 2 adet seri bağlı direnç vardır.
devreye kaç volt verildiğini sor. Akımı (amper) hesaplayınız """

r1=int(input("1.direncin değerini giriniz:"))
r2=int(input("2.direncin değerini giriniz:"))
v=int(input("volt değerini giriniz:"))

rt=r1+r2
print("devrenin toplam direnci=",rt)

amper=v/(rt)

print("devrenin akımı=",amper)
