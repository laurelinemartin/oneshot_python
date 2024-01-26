# Résumé :

Le chiffrement de César est une méthode ancienne pour cacher des messages. Il s’agit d’un algorithme de chiffrement à décalage. C’est-à-dire que pour chiffrer un message, l’alphabet **chiffré** va être décalé par rapport à l’alphabet **clair**. Le nombre de lettre de décalage est appelé la **clé**. Pour le chiffrement de César la clé est de 3. Ainsi, A → D, B → E, C → F, D → G, …, X → A, Y → B, Z → B.

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Au choix.

# Fonctionnalités :

- Entrée : Une chaîne de caractères donnée par un utilisateur correspondant à un message clair ;
- Entrée : Un chiffre pour le décalage donné par l’utilisateur ;
- Calculer le message chiffré correspondant en respectant les minuscules, les majuscules et en ne chiffrant pas les autres caractères (commes les espaces, les points, etc.) ;
- Sortie : Une chaîne de caractère correspondant à un message chiffré.

# Notions abordées dans cette activité :

## Programmation :

- Utiliser des fonctions pour structurer son code
- Utiliser le modulo (reste d’une division euclidienne)

# Déroulement du programme :

1. Avant de commencer le programme de chiffrement / déchiffrement, nous avons besoin de connaître le code ASCII des lettres de l’alphabet (en minuscule et en majuscule). Le code ASCII attribut un nombre aux caractères. Comme nous souhaitons faire un décalage, la valeur numérique attribué à un caractère s’avère très utile. Cette valeur ne commence pas à 0 ou 1. Nous avons donc besoin de connaître les bornes numériques pour notre alphabet.
    1. Exemple en Python : `print("A = {0}".format(ord(”A”))) ;`
    Exemple en C : `printf("A : %d", 'A');`.
2. Stocker les valeurs du code ASCII de `A`, `Z`, `a` et `z` dans des variables ;
3. Créer les fonctions pour le chiffrement :
    1. Créer une fonction `chiffrer` qui prend en entrée une chaîne de caractère `clair` et un entier `cle` et en sortie une chaîne de caractère ;
    2. Créer une fonction `chiffrerUneLettre` qui prend en entrée un caractère `lettre` et un entier `cle` et en sortie un caractère
    3. Créer une fonction `retourDebutAlphabet` qui prend en entrée un caractère `lettre` et un entier `cle` et en sortie un caractère
4. Implémenter la fonction `chiffrerUneLettre` :
    1. Ajouter à la valeur numérique de `lettre` le décalage `cle ;`
    2. Utiliser une condtion pour vérifier que la valeur de `lettre` avec le décalage est dans l’alphabet ;
        1. Si ce n’est pas le cas, appeler la fonction `retournerDebutAlphabet` ;
    3. Renvoyer le caractère obtenu.
5. Implémenter la fonction `retourDebutAlphabet` :
    
    Dans le cas où ajouter la `clé` à la valeur numérique de `lettre` dépasserait la fin de l’alphabet, il faut revenir au début de l’alphabet. Par exemple : y + 3 → b.
    
    1. Utiliser des conditions pour savoir si la `lettre` est une minuscule ou une majuscule ;
    2. Si la lettre est une minuscule : 
        1. Ajouter la `cle` à la `lettre`;
        2. Pour revenir au début de l’alphabet, on utilise le reste de la division euclidienne (l’opération se note `%`) auquel on ajoute la valeur numérique de  `a`. Ce qui donne `(lettre % asciiz) + asciia-1)` .
    3. Si la lettre est une majuscule :
        1. Ajouter la `cle` à la `lettre`;
        2. Pour revenir au début de l’alphabet, on utilise le reste de la division euclidienne (l’opération se note `%`) auquel on ajoute la valeur numérique de  `a`. Ce qui donne `(lettre % asciiZ) + asciiA-1)` .
    4. Retourner le caractère obtenu.
6. Implémenter la fonction `chiffrer` :
    1. Utiliser une boucle pour lire chaque caractère de la chaîne `clair` ;
    2. Utiliser des conditions pour savoir si le caractère courant est une lettre minuscule, majuscule ou autre chose :
        1. S’il s’agit d’une lettre : appeler la fonction `chiffrerUneLettre` et ajouter le résultat à une chaîne de caractère
        2. S’il s’agit d’un autre caractère : ajouter le caractère à une chaîne de caractère
    3. Passer au tour de boucle suivant
    4. Hors de la boucle, retourner la chaîne de caractère chiffrée.
7. Dans la partie principale du code (`main`) :
    1. Demander à l’utilisateur d’entrer une phrase à chiffrer ;
    2. Demander à l’utilisateur d’entrer le décalage ;
    3. Appeler la fonction `chiffrer` ;
    4. Afficher le résultat dans le Terminal.

# Améliorations :

- Ecrire le code pour le déchiffrement.
- Permettre à l’utilisateur de choisir le mode “chiffrer” ou “déchiffrer” ;
- Lire et écrire dans un fichier .txt.

# Ressources :

Alphabet chiffré selon une clé de chiffrement de 3 :

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c6e4935-e714-4705-94a1-243e85d364ad/Untitled.png)

Le film **“*The Imitation Game”* 

Le chiffrement de César : https://www.futura-sciences.com/sciences/questions-reponses/mathematiques-quest-ce-chiffrement-cesar-8032/

Les chiffrements par substituion : https://fr.wikipedia.org/wiki/Chiffrement_par_substitution

---
