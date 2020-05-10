archivo = open("algo.txt","r")#abre un archivo con permisos de lectura

lista = archivo.readlines()#convierte el archivo en una lista leyendo linea por linea

cadena = archivo.read()#a todo el archivo lo mete en un solo string
lista2=cadena.split()#crea una lista de cadenas

##############################################

np.array([a,b],[c,d])#crea un arreglo en forma de matriz

shape(3,4)#crea una matriz 3x4
reshape(4,3)#formatea en una matriz 4x3

np.zeros(numero)#crea un arreglo de esos numeros

A = np.linspace(1,30,30).reshape(5,6)
b= A.transpose()#da la matriz transpuesta

np.dot(A,b)#multiplica pero da el tamaño de A

np.conjugate(A)# da el conjugado

#############################################

x1= np.array([a,b],[c,d])
x2= np.matrix(x1)#lo convierte en formato de matriz, esta funcion si hace producto matricial

np.eye(5)#matriz identidad de 5x5

np.linalg.det(x2)#da el determinante

x = np.linalg.solve(A,b)#resuelve A.x=B

B = np.linalg.inv(B)#calcula la inversa de la matriz

F = 10*np.random(10,10)#genera una matriz 10x10 con numeros aleatorios

l,p = np.linalg.eig(A)#calcula los autovalores y autovectores

l#=autovalores
p#= autovectores

#######################################################

np.set_printoptions(suppress = true)# supreme valores chicos

np.set_printoptions(precision = 2)#imprime con una precision = 2


