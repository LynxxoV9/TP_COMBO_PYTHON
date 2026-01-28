""" Fonctions et modalité """

#Fonction pour calculer la moyenne
def calcul_moyenne(liste_notes):
    note_cumul = 0
    for j in range(len(liste_notes)):
        note_cumul += liste_notes[j] 
    
    return round( note_cumul/len(liste_notes) ,2)


#Fonction pour mentionner une moyenne
def mention(moyenne):
    match moyenne:
        case moyenne if moyenne > 0 and moyenne  < 10:
            return "Ajourné"
        case moyenne if moyenne >= 10 and moyenne < 14:
            return "Passable"
        case moyenne if moyenne >=14 and moyenne < 16:
            return "BIEN"
        case moyenne if moyenne >=16 and moyenne <= 20:
            return "Très Bien"
        case _:
            return "XXX Moyenne insensée XXX"


# Test des fonctions avec plsieurs notes
print("\n \n \t \t==========[ Simplifyed MOY_CHECKER ]==========")

all_note_size = int(input("\n\n\nCombien de notes voulez-vous procédez?\n/>"))

all_note = []
for i in range(all_note_size):
    note = float(input(f"\n\n\nEntrez la note [{i+1}]:\n/>"))
    all_note.append(note)


print(f"\n \nLa moyenne est [{calcul_moyenne(all_note)}] sur 20 avec une mention '{mention(calcul_moyenne(all_note))}' ")

print ("\n \n \n ==========[ FIN DU PROGRAMME ]==========")

