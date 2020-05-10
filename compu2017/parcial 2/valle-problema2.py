P = partidas.split()

def abiertas(partidas):
    F = partidas.split()
    t = 0
    lis= []

    while len(F) >= 1: 
      for i in range(4):
        lis.append(F[i])
      if lis[0] == "e4" and lis[1]== "e5":
        t += 1
      for j in range(4):
        del(lis[0])
        del(F[0])
    return t

def semi_abiertas(partidas):
    F = partidas.split()
    t = 0
    lis= []

    while len(F) >= 1: 
      for i in range(4):
        lis.append(F[i])
      if lis[0] == "e4" and lis[1]!= "e5":
        t += 1
      for j in range(4):
        del(lis[0])
        del(F[0])
    return t

def cerradas(partidas):
    F = partidas.split()
    t = 0
    lis= []

    while len(F) >= 1: 
      for i in range(4):
        lis.append(F[i])
      if lis[0] == "d4" and lis[1]== "d5":
        t += 1
      for j in range(4):
        del(lis[0])
        del(F[0])
    return t

def ruy_lopez(partidas):
    F = partidas.split()
    t = 0
    lis= []

    while len(F) >= 1: 
      for i in range(4):
        lis.append(F[i])
      if lis[0] == "e4" and lis[1]== "e5" and lis[2]== "Nf3" and lis[3] == "Nc6":
        t += 1
      for j in range(4):
        del(lis[0])
        del(F[0])
    return t

r = abiertas(partidas)
s = semi_abiertas(partidas)
t = cerradas(partidas)
u = ruy_lopez(partidas)
z = len(P) 


print ("Tipos de apertura     Cantidad           Porcentaje")
print ("_______________________________________________________")
print ("Abiertas                %1.f                %1.5f         " % (r,(r/z)))
print ("Semi-abiertas           %1.f                %1.5f         " % (s,(s/z)))
print ("Cerradas                %1.f                %1.5f         " % (t,(t/z)))
print ("Ruy-Lopez               %1.f                %1.5f         " % (u,(u/r)))






