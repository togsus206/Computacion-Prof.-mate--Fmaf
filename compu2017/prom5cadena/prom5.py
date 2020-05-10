archivo = open("nombres.dat","r")
l = archivo.readlines()

lista =[]
for i in l:
  c = i.split()
  lista.append(c)
  
for j in lista:
       j[2]= int(j[2])
       j[3] = int(j[3])
       j[4] = int(j[4])


promocion = []
regular =[]
libre = []

for i in lista:
  if (i[2]< 4 and i[3]<4) or (i[2]< 4 and i[4]<4) or (i[3]<4 and i[4]<4):
      libre.append(i[0])
      libre.append(i[1])
     
  if ((i[2]>=4 and i[3]>=4) or (i[2]>=4 and i[4]>=4) or (i[3]>=4 and i[4]>=4)) and (i[2]<6 or i[3]<6 or i[4]<6) :
      regular.append(i[0])
      regular.append(i[1])
   
  if (i[2]>= 6 and i[3]>=6 and i[4]>=6) and (i[2]+i[3]+i[4] >= 21):
      promocion.append(i[0])
      promocion.append(i[1])


while len(promocion) > 1:
  print ("%s %s esta promocionado" % (promocion[0],promocion[1]))
  del promocion[0]
  del promocion[0]
  print()
 
while len(regular)>1:
  print ("%s %s esta regular" % (regular[0],regular[1]))
  del regular[0]
  del regular[0]
  print()

while len(libre) > 1:
  print ("%s %s esta libre" % (libre[0],libre[1]))
  del libre[0]
  del libre[0]
  print()

