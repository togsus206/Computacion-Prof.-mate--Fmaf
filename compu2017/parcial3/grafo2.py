import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,7,10)
v = 1/4*x
w = 6*x


plt.plot(x,v,"g",label = "Vector $(4,1)$")
plt.plot(x,w,"b",label= "Vector $(1,6)$")

i = 20
for i in range(10):
     plt.plot(1,i,"y.",)
     i -= 1
plt.plot(1,6,"r.")

plt.plot(0,0,"r.",label = "A")

plt.legend(["Vector $(4,1)$","Vector $(1,6)$"], loc = 2)

plt.xlabel("eje x")
plt.ylabel("eje y")
plt.savefig("graf2.pdf")
plt.show()
