prixArticle=0
total=0
montantPayer=0

while prixArticle!=0:
    total=total+prixArticle
    prixArticle=int(input("entrer le prix de l'article : "))

while montantPayer <total:
    montantPayer=int(input("entrer le montant payer : "))
    
monnaie=montantPayer-total

if monnaie==0:
    print("pas de monnaie à rendre")
else:
    while monnaie>10:
        print("Billet de 10")
        monnaie-=10
    while monnaie>5:
        print("Billet de 5")
        monnaie-=5
    while monnaie>0:
        print("Pièce de 1")
        monnaie-=1