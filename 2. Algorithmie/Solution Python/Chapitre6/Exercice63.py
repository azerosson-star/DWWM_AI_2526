# # Déclaration du tableau de notes
# notes = [0] * 9

# # Boucle pour lire les notes
# for i in range(9):
#     notes[i] = int(input(f"Entrez la note numéro {i + 1} :"))

# Affichage des notes
# print("Les notes saisies sont :", notes)


print(f"Les notes saisies sont :{[int(input(f"Entrer une note {i+1} : ")) for i in range(9)]}")
