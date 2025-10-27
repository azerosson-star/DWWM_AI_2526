def facto(nb):
    f=1
    for i in range(1,nb+1):
        f  *= i
    return f
   
nbPartant=int(input("entrer le nombres de cheveaux partant :"))
nbJoue=int(input("entrer le nombres de cheveaux joué    :"))



print(f"dans l'ordre {facto(nbPartant)/facto(nbPartant-nbJoue)}")
print(f"dans le désordre {facto(nbPartant)/(facto(nbJoue)*facto(nbPartant-nbJoue))}")