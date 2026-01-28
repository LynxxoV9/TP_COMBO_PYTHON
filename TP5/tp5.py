"""  Lecture et écriture de fichiers """

print("\n==================== | Gestion des notes | ====================\n")

#Enregistrement des notes dans un fichier
notes_file = "notes.txt"

nbr_notes = int(input("Combien de notes voulez-vous enregistrer ?\n/> "))

with open(notes_file, "w") as f:
    for i in range(nbr_notes):
        note = float(input(f"Entrez la note [{i+1}] :\n/> "))
        f.write(str(note) + "\n")


#La lecture du fichier et calcul de la moyenne
somme = 0
compteur = 0

with open(notes_file, "r") as f:
    for ligne in f:
        note = float(ligne.strip())
        somme += note
        compteur += 1

moyenne = round(somme / compteur, 2)

#Écriture du résultat dans un autre fichier
resultat_file = "resultat.txt"

with open(resultat_file, "w") as f:
    f.write(f"La moyenne des notes : {moyenne}\n")

print("\nLa moyenne a été calculée avec succès")
print(f"Moyenne = {moyenne}")


print("\n==================== | Fin du programme | ====================")
