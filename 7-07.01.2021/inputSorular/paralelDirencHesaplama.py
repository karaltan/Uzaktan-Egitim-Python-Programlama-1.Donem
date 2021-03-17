""" biri 10ohm diğeri 20ohm değerinde 2 adet paralel bağlı direnç vardır.
devreye 40volt veriliyor. Akımı (amper) hesaplayınız """

r1=10
r2=20
v=40

rt=(r1*r2)/(r1+r2)
print("devrenin toplam değeri=",rt)

amper=v/(rt) #6.0

print("devrenin akımı=",amper)
