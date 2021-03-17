a = int(input("1.doğrunun uzunluğu: "))
b = int(input("2.doğrunun uzunluğu: "))
c = int(input("3.doğrunun uzunluğu: "))

if (a+b)>c and (a+c)>b and (c+b)>a:
    print("üçgen oluşturabilir")
else:
    print("üçgen oluşmaz")


