import numpy as np
import matplotlib.pyplot as plt

a = float(input("Ingresa el valor del centro de desrrollo en [-2,8]: "))

def f(x):
  return x+np.e**(x/4)*np.cos(x)

def f1(x):
 return 1+(((np.e**(x/4))*np.cos(x))/4)-((np.e**(x/4))*np.sin(x))

def f2(x):
  return ((np.e**(x/4))*(1/16)*np.cos(x))-((np.e**(x/4))*(1/2)*np.sin(x))-((np.e**(x/4))*np.cos(x))

def f3(x):
  return ((np.e**(x/4))*(1/64)*np.cos(x))-((np.e**(x/4))*(1/16)*np.sin(x))-((np.e**(x/4))*(1/8)*np.sin(x))-((np.e**(x/4))*(1/2)*np.cos(x))-((np.e**(x/4))*(1/4)*np.cos(x))+((np.e**(x/4))*np.sin(x))


x = np.linspace(-2,8,51)
y =f(x)
polinomio2 = f(a)+f1(a)*(x-a)
polinomio3 = f(a)+(f2(a)*((x-a)**2))/2
polinomio4 = f(a)+(f3(a)*((x-a)**3))/6

plt.plot(x,y,"k",label="funcion")
plt.plot(x,polinomio2,"y",label = "Polinomio 1")
plt.plot(x,polinomio3, "b",label = "Polinomio 2")
plt.plot(x,polinomio4, "g",label = "Polinomio 3")
plt.plot(a,f(a), "r.")

plt.legend(["funcion","Polinomio 1","Polinomio 2","Polinomio 3"], loc = 2)

plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("Grafico de una funcion con sus tres primeros polinomios de Taylor")
plt.axis([-2,8,-3,10])
plt.show()
