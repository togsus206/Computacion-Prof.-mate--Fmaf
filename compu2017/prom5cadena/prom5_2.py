archivo = open("nombres.dat","r")
l = archivo.readlines()

cadena = []

for i in l:
    cadena.append(i.split("\t"))

  
notas = {}

  
for j in cadena:
       j[1]= int(j[1])
       j[2] = int(j[2])
       j[3] = int(j[3])
    
for t in cadena:
    notas[t[0]]=[t[1],t[2],t[3]]


for j in notas:
   i= notas[j]
   if (i[0]< 4 and i[1]<4) or (i[1]< 4 and i[2]<4) or (i[0]<4 and i[2]<4):
       notas[j] = "Libre"

   if ((i[0]>=4 and i[1]>=4) or (i[1]>=4 and i[2]>=4) or (i[0]>=4 and i[2]>=4)) and (i[0]<6 or i[1]<6 or i[2]<6) :
       notas[j] = "Regular"

   if (i[0]>= 6 and i[1]>=6 and i[2]>=6) and (i[0]+i[1]+i[2] >= 21):
       notas[j]= "Promocion"

for i in notas:
    print ("El alumno %s se encuentra en estado %s" %(i,notas[i]))
