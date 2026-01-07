nb=int(input("entrer un nombre : "))

somme =0
aff = ""
for i in range(1,nb+1):
    somme  += i
    aff += "+"+ str(i)
print(f"{aff[1:]} = {somme}")