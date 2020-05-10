import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,201)
y = 1/(1+x**2)
plt.title("Curva Lorentziana")
plt.xlabel("x")
plt.axis([-4,4,0,1.1])
plt.plot(x,y, 'r-')
plt.legend(['1/(1+x^2)'], loc=1)
plt.savefig("lorentziana.pdf")
plt.show()


