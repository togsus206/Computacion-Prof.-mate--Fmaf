from math import e

a = int(input("ingrese 10, 100 o 1000: "))
n = 1
c = 1
suma = 1

while (n <= a):
    c = c * n 
    s = 1 / c
    suma += s
    n += 1

print (suma)
print ( e)
