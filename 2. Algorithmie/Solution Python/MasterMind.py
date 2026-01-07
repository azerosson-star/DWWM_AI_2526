import random

NB_COULEURS = 4
LONGUEUR_COMBINAISON = 4
NB_ESSAIS_MAX = 10
couleurs=[]

def generer_combinaison_secrete():
    """Génère une combinaison secrète aléatoire."""
    combinaison_secrete = []
    for _ in range(LONGUEUR_COMBINAISON):
        combinaison_secrete.append(random.choice(couleurs)) # selectionne au hasard un élément du tableau
    return combinaison_secrete

def afficher_combinaison(combinaison):  
    """Affiche une combinaison de couleurs."""
    for couleur in combinaison:
        print(couleur, end=" ")
    print()

def verifier_proposition(combinaison_secrete, proposition_joueur):
    """Vérifie la proposition du joueur et retourne le nombre de pions bien placés et mal placés."""
    nb_pions_bien_places = 0
    nb_pions_mal_places = 0
    secret = combinaison_secrete.copy()
    prop = proposition_joueur.copy()

    # Pions bien placés
    for i in range(LONGUEUR_COMBINAISON-1,-1,-1): # on parcours à partir de la fin pour ne pas modifier les positions pour le pop
        # je veux aller de 3 à 0; 3=len-1; pour traiter le 0, il faut une fin de range à -1; pas de -1 pour reculer
        if combinaison_secrete[i] == proposition_joueur[i]:
            nb_pions_bien_places += 1
            secret.pop(i) # on enleve les elements bien placés pour ne pas les recompter dans les mal placés
            prop.pop(i) # on enleve les elements bien placés pour ne pas les recompter dans les mal placés

    # Pions mal placés
    for i in range(len(prop)):
        if prop[i] in secret:
            secret.pop(secret.index(prop[i])) # équivaut à secret.remove(prop[i])
            nb_pions_mal_places += 1

    return nb_pions_bien_places, nb_pions_mal_places

def jouer_manche(combinaison_secrete):
    """Joue une manche du jeu."""
    nb_essais = 0
    affichage = []
    proposition_joueur=None
    while nb_essais < NB_ESSAIS_MAX and proposition_joueur != combinaison_secrete:
        # Proposition du joueur
        proposition_joueur = []
        for i in range(LONGUEUR_COMBINAISON):
            couleur=-1
            while  couleur <= 0 or couleur > NB_COULEURS:
                try:
                    couleur = int(input(f"Saisissez la couleur {i + 1} {couleurs} : "))
                except ValueError:
                    print("Erreur : Saisie incorrecte. Veuillez saisir un nombre entier.")
            proposition_joueur.append(couleur)

        # Évaluation de la proposition
        nb_pions_bien_places, nb_pions_mal_places = verifier_proposition(combinaison_secrete, proposition_joueur)

        # Affichage du résultat
        print(f"{nb_pions_bien_places} pion(s) bien placé(s).")
        print(f"{nb_pions_mal_places} pion(s) de la bonne couleur mais mal placé(s).")
        nb_essais += 1
        # on crée un tuple qui correspond aux données du tour
        tour =()
        tour = tour + (proposition_joueur,nb_pions_bien_places,nb_pions_mal_places)
        # on range le tuple dans l'afficheur
        affichage.append(tour)
    
        # on affiche le résumé
        print("\n\n")
        for i in range(len(affichage)):
            print(f" combinaison {affichage[i][0]} :\t {affichage[i][1]} bien placés\t {affichage[i][2]} mal placés")
        print("\n\n")

    if proposition_joueur == combinaison_secrete:
        print("Manche gagnée !")
    else:
        print("Manche perdue !")
    afficher_combinaison(combinaison_secrete)

def jouer():
    """Fonction principale du jeu."""
    initialisation()
    # Nombre de manches
    nb_manches=0
    while nb_manches<1:
        try:
            nb_manches = int(input("Combien de manches souhaitez-vous jouer ? "))
        except ValueError:  
            print("Erreur : Saisie incorrecte. Veuillez saisir un nombre entier.")

    # Boucle principale du jeu
        for manche in range(1, nb_manches + 1):
            print(f"\nManche {manche} :")
            combinaison_secrete = generer_combinaison_secrete()
            print(combinaison_secrete)
            jouer_manche(combinaison_secrete)

def initialisation():
    global NB_COULEURS, NB_ESSAIS_MAX, LONGUEUR_COMBINAISON, couleurs
    choix=0

    while choix<1 or choix>4:
        try:
            choix = int(input("Quel niveau de difficulté (1 à 4) ? "))
        except ValueError:
            print("Erreur : Saisie incorrecte. Veuillez saisir un nombre entre 1 et 4.")

    # Définition des variables
    match choix:
        case 1:
            NB_COULEURS = 4
            LONGUEUR_COMBINAISON = 4
            NB_ESSAIS_MAX = 10
        case 2:
            NB_COULEURS = 4
            LONGUEUR_COMBINAISON = 5
            NB_ESSAIS_MAX = 10
        case 3:
            NB_COULEURS = 5
            LONGUEUR_COMBINAISON = 5
            NB_ESSAIS_MAX = 10
        case 4:
            NB_COULEURS = 5
            LONGUEUR_COMBINAISON = 5
            NB_ESSAIS_MAX = 7

    # Couleurs possibles
    couleurs=[]
    for i in range(1,NB_COULEURS+1):
        couleurs.append(i)

jouer() 
