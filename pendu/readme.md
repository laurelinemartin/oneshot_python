# Résumé :

Programmer le jeu du pendu : retrouver les lettres cachées pour découvrir un mot en un nombre limité de tentatives.

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Python ou au choix

# Fonctionnalités :

- Choisir un mot au hasard dans une liste de mots ;
- Afficher ce mot sous forme cachée ;
- Demander à l’utilisateur de proposer une lettre ;
- Vérifier si la lettre donnée par l’utilisateur est dans le mot ;
- Afficher le mot avec les lettres cachées et découvertes.

# Notions abordées :

## Programmation

- Conditions et boucles ;
- Définition et appels de fonctions ;
- Manipulation de l’aléatoire ;
- Utiliser plusieurs fichiers pour organiser son codes et stocker des données simples.

## Autres :

- Utilisation du terminal

# Déroulement :

1. Créer un premier fichier nommé `dictionnaire.py` ;
2. Créer une variable `mots` . Cette variable est une liste contenant les mots que le programme pourra faire devenir à l’utilisateur.
`mots = [”chat”,
         # ...
         “mangouste”]`
*Cette variable peut contenir autant de mots que vous le souhaitez, il faut que tous les mots soient entre guillemets et que tous les mots, sauf le dernier, soient suivis d’une virgule.*
3. Créer un nouveau fichier `pendu.py` et y importer les bibliothèques `random`, `string` et depuis la bibliothèque `dictionnaire` (sans le `.py`) que nous venons de créer, importer `mots` ;
4. Créer une fonction `recupererMot()` qui
    1. Tire aléatoirement un mot parmi la liste avec `random.choice(mots)` ;
    2. Met ce mot en majuscule avec la fonction `.upper()` ;
    3. Retourne le mot sélectionné.
5. Créer une fonction `recupererLettres(mot)` qui :
    1. Récupère l’ensemble des lettres dans mots avec la fonction `set(mot)` ;
    2. Retourne cet ensemble.
6. Créer une fonction `demanderLettre()` qui : 
    1. Demande à l’utilisateur d’entrer une lettre dans le terminal ;
    2. Met le retour de l’utilisateur en majuscule ;
    3. Retourne la lettre obtenue.
7. Créer une fonction `initialiserMotCache(mot)` qui :
    1. Créer une chaîne de caractères de `"_"` de la longueur du `mot` passé en argument ;
    2. Retourner cette chaîne.
8. Créer une fonction `pendu` qui :
    1. Initialise une variable `vies` au nombre maximales de tentatives infructueuses possibles ;
    2. Initialise une variable `motAlea` avec un mot tiré aléatoirement et passé en majuscule. *Utiliser l’une des fonctions que nous venons de créer* ;
    3. Initialise une variable `lettresDuMot` avec l’ensemble des lettres contenus dans le mot. *Utiliser l’une des fonctions que nous venons de créer* ;
    4. Initialiser une variable `motCache` avec des `"_"` de la taille du mot à trouver. *Utiliser l’une des fonctions que nous venons de créer ;*
    5. Créer une boucle qui tourne tant que le nombre de `vie` est supérieur à 0 et qu’il reste des lettres dans la variable `lettreDuMot` . Dans cette boucle :
        1. Afficher  `motCache`. Pour un meilleur rendu, utiliser `print(" ".join(motCache)+" ")` ;
        2. Demander à l’utilisateur de proposer une lettre et stocker sa réponse dans une variable. *Utiliser l’une des fonctions que nous venons de créer ;*
        3. Si la lettre donnée par l’utilisateur est dans l’ensemble de lettre du mot `lettreDuMot`, alors :
            1. Pour chaque index, allant de 0 à la longueur du `mot` -1 :
                1. Si la valeur du mot à l’index courant correspond à la lettre proposée par l’utilisateur, alors remplacer la valeur de `motCache` à l’index courant par la lettre proposée :
                `if mot[i] == u:
                	u_mot[i] = u`
                    1. Si la lettre proposée par l’utilisateur est contenue dans `lettresDuMot`, alors la retirer.
        4. Si la lettre n’est pas contenue dans la variable `lettresDuMot`, alors le nombre de vie décroît de 1.
    6. Une fois sorti de la boucle, afficher le mot.
9. Appeler la fonction `pendu()`.

# Améliorations :

- Créer plusieurs variables dans le dictionnaires. Ces variables peuvent correspondre à différents niveaux de difficultés, à différents thèmes… ;
- Afficher le nombre de tentatives à chaque fin de partie ;
- Afficher les lettres déjà testées par l’utilisateur à chaque tour ;
- Proposer à l’utilisateur de rejouer ;
- Proposer à l’utilisateur d’ajouter des mots au dictionnaires ;
- Afficher le dessin du pendu qui se forme à chaque essai manqué.

# Ressources :

- Vidéo YouTube en anglais, détaillant le programme : https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s

---
