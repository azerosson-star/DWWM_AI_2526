
# liste=[]
# for i in range (5):
#     liste.append(int(input(f"entrer le nombre{i} : ")))


liste=[int(input(f"entrer le nombre {i}: ")) for i in range (1,6)]
print(f" le plus grand nombre est le {max(liste)} c'etait le numéro {liste.index(max(liste))+1}")