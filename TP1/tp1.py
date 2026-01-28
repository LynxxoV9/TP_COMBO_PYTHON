print ("\n \t \t    ==========Prise en main et les structures de bases==========\n \n")


""" 1- Programme qui demande le nom et l'âge d'un utilisateur """
name = str(input("Nom:\n />"))
age = int(input("\nEntrer votre âge:\n />"))
while age <= 0:
    age = int(input("Veuillez entrer un âge valide:\n />"))

print("\n\n")
"""2- Au Togo est majeur celui qui a au moins 18 ans et au cas contraire il est mineur."""
if age >=18 :
    print(f"{name.upper()} vous avez {age} ans, vous êtes majeur.")
else:
    print(f"{name.upper()} vous avez {age} ans, vous êtes mineur.")




"""3- Afficher tous les nombre paire entre 1 et 100 """
print("\n\n\t\t========== La liste de tous les nombres paires entre 1 et 100 ==========")
for number in range(1 , 101):
    if number%2 == 0:
        print(number)
