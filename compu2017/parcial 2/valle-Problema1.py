import math as m

x0 = float(input("Ingrese el valor x0 en [0,1.2]: "))

eps = 10e-8
M = 100
#intervalo = [0, 1.2]
a = 0
b = 1.2
n = int(input("Ingrese el numero de interaciones deseadas: "))

def f(x):
  return (1/(2*x))+ m.cos(x)-1

def F(x):
  return (1/2)+ x*m.cos(x) 

print ()
print ("Nota: El programa cortara si la diferencia de aproximacion es mas chica que Epsilon" )
print ("Nota 2: El programa cortara si las iteraciones superan el numero 100")
print ()
print ("iteracion    Aprox. Xn      error")
print ("--------------------------------------")

for i in range (1,n+1):
  if i == 1:
   x1 = F(x0)
   xn = 1.2
  else:
    xn = x1
    x1 = F(x1)

  if abs(xn-x1)> eps:
    if i == 1:
     print ("%1.f        %3.10f     %1.f" % (i, F(x1), 1))

    else:
      print ("%1.f        %3.10f    %2.13f" % (i, F(x1), (xn-x1)))

  else:
    break 
    
