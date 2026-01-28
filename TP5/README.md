# TP5 – Lecture et écriture de fichiers

Ce travail pratique est consacré à la manipulation des fichiers en Python.  
Il met en œuvre la lecture et l’écriture de données dans des fichiers texte à travers un cas réel de sauvegarde et d’exploitation de notes scolaires.

Le programme permet d’enregistrer des données, de les relire, de les traiter et de produire un résultat exploitable.

## Objectifs du TP

Ce TP vise à :
- Comprendre la notion de fichiers en programmation
- Manipuler des fichiers texte en lecture et en écriture
- Sauvegarder des données de manière persistante
- Exploiter les données stockées dans un fichier
- Produire un résultat à partir de données enregistrées

## Fonctionnalités du programme

Le programme permet de :
- Saisir un nombre variable de notes
- Enregistrer les notes dans un fichier texte
- Lire les notes depuis le fichier
- Calculer la moyenne des notes
- Enregistrer le résultat dans un second fichier

## Fichiers utilisés

Le programme manipule deux fichiers :
- `notes.txt` : contient la liste des notes saisies
- `resultat.txt` : contient la moyenne calculée

## Concepts Python utilisés

Notions mises en pratique :
- Fonction `open()`
- Modes de fichiers : lecture (`r`) et écriture (`w`)
- Instruction `with`
- Lecture ligne par ligne
- Conversion de types (str → float)
- Calculs numériques
- Écriture dans un fichier

## Exécution du programme

Depuis le dossier TP5 :
python tp5.py

Le programme s’exécute en mode interactif et génère automatiquement les fichiers nécessaires.
Intérêt pédagogique

Ce TP montre comment :

    assurer la persistance des données

    séparer la saisie, le traitement et la sauvegarde

    écrire des programmes capables de gérer des données externes

La manipulation des fichiers est une compétence essentielle pour le développement d’applications réelles.
