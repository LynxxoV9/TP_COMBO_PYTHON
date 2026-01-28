# TP2 – Fonctions et modularité 💪

Ce travail pratique introduit la notion de fonctions en Python et met l’accent sur la modularité du code.  
Il simule un système simple de calcul de moyenne et d’attribution de mentions académiques.

Le programme demande à l’utilisateur le nombre de notes à saisir, puis affiche automatiquement la moyenne et la mention correspondante.

L’objectif est d’apprendre à structurer un programme en blocs réutilisables et logiques.

## Objectifs du TP

Ce TP vise à :
- Définir et utiliser des fonctions
- Manipuler des listes de données numériques
- Retourner des valeurs depuis une fonction
- Tester un programme avec différentes entrées utilisateur

## Fonctionnalités implémentées

Le programme permet de :
- Saisir un nombre variable de notes
- Calculer la moyenne des notes saisies
- Attribuer une mention en fonction de la moyenne obtenue
- Afficher un résultat clair et synthétique

## Fonctions définies

Fonctions principales :
- calcul_moyenne(liste_notes)  
  Calcule la moyenne d’une liste de notes et retourne une valeur arrondie à deux décimales.

- mention(moyenne)  
  Retourne une mention académique selon l’intervalle de la moyenne :
  Ajourné, Passable, Bien ou Très Bien.

## Concepts Python utilisés

Notions abordées :
- Définition de fonctions avec def
- Paramètres et valeurs de retour
- Listes
- Boucles for
- Structure match / case
- Interaction utilisateur

## Exécution du programme

Depuis le dossier TP2 :
```bash
python tp2.py
