# TP3 – Listes, tuples et dictionnaires

Ce travail pratique met en œuvre les structures de données fondamentales en Python, notamment les listes et les dictionnaires, à travers un cas réel de gestion simplifiée des résultats académiques d’étudiants.

Le programme permet d’enregistrer plusieurs étudiants, d’analyser leurs moyennes et d’afficher des statistiques globales.

## Objectifs du TP

Ce TP vise à :
- Comprendre l’utilisation des listes et des dictionnaires
- Stocker des données structurées
- Parcourir des collections avec des boucles
- Effectuer des traitements conditionnels
- Calculer des statistiques simples sur un ensemble de données

## Fonctionnalités du programme

Le programme permet de :
- Enregistrer un nombre variable d’étudiants
- Stocker pour chaque étudiant :
  - le nom
  - l’âge
  - la moyenne
- Afficher les étudiants admis (moyenne supérieure ou égale à 10)
- Calculer et afficher la moyenne générale de la classe

## Structure des données

Les informations sont stockées dans un dictionnaire dont :
- les clés sont générées dynamiquement (`info_étudiant1`, `info_étudiant2`, etc.)
- les valeurs sont des listes contenant :
  - le nom de l’étudiant
  - son âge
  - sa moyenne

Exemple de structure :
```python
{
  "info_étudiant1": ["Olivier", 18, 17.0],
  "info_étudiant2": ["Lynx", 25, 9.0]
}

## Concepts Python utilisés

Notions mises en pratique :

    Listes

    Dictionnaires

    Boucles for

    Conditions if

    Saisie utilisateur avec input()

    Calculs numériques

    Accès aux éléments par index

## Exécution du programme

Depuis le dossier TP3 :

python tp3.py

Le programme s’exécute en mode interactif et guide l’utilisateur lors de la saisie des informations.

## Résultats affichés

À l’exécution, le programme affiche :

    la liste des étudiants admis

    la moyenne générale de l’effectif

    un message de fin indiquant la fin du traitement


