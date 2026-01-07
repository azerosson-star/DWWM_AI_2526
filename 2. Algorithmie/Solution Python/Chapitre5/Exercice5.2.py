nb=0

while nb<10 or nb>20:
    try:
        nb=int(input("entrer un nombre entre 10 et 20 :"))
    except ValueError:
        print("il faut que ce soit un nombre")
    else : 
        if nb>20:
            print("plus petit !")
        elif nb<10:
            print("plus grand!")