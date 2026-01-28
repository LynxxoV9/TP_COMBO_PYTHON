""" LISTES, TUPLES, DICTIONNAIRES """

#Définition de la liste d'étudiants

print("\n \n \n ==================== | Enrergistrez les étudiants | ====================")

nbr_etudiant = int (input ("Combien d'étudiants voulez-vous enregistrer ?\n/>"))

liste_etudiant = {}
info=[]
for i in range(nbr_etudiant):
    nom = input (f"\nNom de l'etudiant [{i+1}]:\n/>")
    age = int(input (f"\nL'âge de l'étudiant [{i+1}]:\n/>"))
    moyenne = float(input (f"\nLa moyenne de l'étudiant [{i+1}]:\n/>"))
    info.append(nom)
    info.append(age)
    info.append(moyenne)
    liste_etudiant[f'info_étudiant{i+1}'] = info

    #####test
    print (liste_etudiant)
    info =[]

#afficher les étudiants admis (genre ayant obtenu une moyenne supérieures ou égales à 10
for i in range(nbr_etudiant):
    moyenne_valid = liste_etudiant.get(f'info_étudiant{i+1}')[2] >= 10
    if moyenne_valid:
        print ("\n=================================================================================")
        print (f"\t \tL'étudiant {liste_etudiant.get(f'info_étudiant{i+1}')[0]} est Admis !")
        print ("=================================================================================")


#Moyenne générale
mg_sum = 0
for i in range(nbr_etudiant):
    mg_sum += liste_etudiant.get(f'info_étudiant{i+1}')[2]

moyenne_generale = round(mg_sum/nbr_etudiant , 2)
print (f"\n\n \t >>>>>>>>>>>>>>>>>>>>> | La moyenne générale de l'effectif est {moyenne_generale} ! | <<<<<<<<<<<<<<<<<<<<<<<")


print ("\n \n \n ==========[ FIN DU PROGRAMME ]==========")
