nb=0
liste=[]
while nb!=0: 
    nb=int(input(f"entrer un nombre : "))
    if nb>0:
         liste.append(nb)
print(f" le plus grand nombre est le {max(liste)} c'etait le numéro {liste.index(max(liste))}")