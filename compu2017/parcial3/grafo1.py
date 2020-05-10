import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,8,10)
v = 3/2*x
u = 2/5*x


plt.plot(x,v,"g",label = "Vector $(2,3)$")
plt.plot(x,u,"k",label= "Vector $(5,2)$")
plt.plot(0,0,"r.",label = "A")

i = -10
for i in range(30): 
   plt.plot(2,i,"y.")
   i += 1

plt.plot(2,3,"r.")


plt.legend(["Vector $(2,3)$","Vector $(5,2)$"], loc = 2)

plt.xlabel("eje x")
plt.ylabel("eje y")
plt.savefig("graf1.pdf")
plt.show()
