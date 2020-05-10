n = 100
x = 1/2
suma = x
a = 1
c = 1

while (a <= n):
  c = c* (((2*n)-1)/(2*n))
  suma += c * ((x**((2*n) +1))/((2*n)+1))
  a += 1

print (6*suma)    
