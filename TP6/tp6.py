""" Sécurisation d'une Application utilisée par des non-informaticiens"""

print ("\n\n\t\t================Hi ! Une division basique cette fois-ci================")

#Début de la division avec le catch de l'erreur 

while True:
    try:
        num = float(input("\n Entrez le numérateur:\n]>"))
        deno = float(input("\n Entrez le dénominateur:\]>")) #Normalement le dénominateur 0 génère une ZeroDivisionError:
        produit =round( num/deno , 2 )
        print ("\n\n",produit)
        break

    except ZeroDivisionError:
        print ("\n\nXXXXX( -Le dénominateur ne peut pas être zéro !- )XXXXX")
