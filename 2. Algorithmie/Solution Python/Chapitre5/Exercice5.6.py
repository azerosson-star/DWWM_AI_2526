nb=int(input("entrer un nombre : "))

facto =1
aff = ""
for i in range(1,nb+1):
    facto  *= i
    aff += "*"+ str(i)
print(f"{aff[1:]} = {facto}")