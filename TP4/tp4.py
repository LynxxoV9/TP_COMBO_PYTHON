import time
""" Manipulation de chaînes de caractères """

print("\n\n==================== | Quelques opérations sur les phrases | ====================\n")

#La phrase de l'utilisateur
some_words = input("Entrer une phrase :\n)> ").strip()
while some_words == "":
    some_words = input("Entrez une phrase qui n'est pas vide:\n/> ").strip()


#Compter le nombre de mots
words = some_words.split()
counter = len(words)

print(f"\nLe nombre de mots dans la phrase : {counter}")



#Trouver le mot le plus long
m_long = words[0]
for mot in words:
    if len(mot) > len(m_long):
        m_long = mot

print(f"\n\t\t | Le mot le plus long est [{m_long}] avec {len(m_long)} caractères |")




#Check si la phrase est un palindrome( peu importe le sens se lit de la mm manière sans considérer les espaces)

print ("\n \n ================[ Vérifions voir si vous avez entré un palindrôme ou pas ? ]================")

time.sleep(1)
print ("1")
time.sleep(1)
print ("2")
time.sleep(1)
print ("3")
time.sleep(1)
espace_closed = some_words.lower().replace(" ", "")

if espace_closed == espace_closed[::-1]:
    print("\nLa phrase est un palindrome")
else:
    print("\nLa phrase n'est pas un palindrome")


print("\n\n==================== | Fin du programme | ====================")

