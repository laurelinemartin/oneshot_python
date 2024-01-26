# Résumé :

Réaliser un programme simple dont le but est de deviner si la prochaine carte tirée au hasard par l’ordinateur sera supérieur ou inférieur à la première carte affichée à l’écran.

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Au choix

# Fonctionnalités :

- Afficher le chiffre d’une carte (compris entre 1 et 9) ;
- Demander à l’utilisateur si la prochaine carte sera supérieur ou inférieur à la première carte ;
- Si :
    - Le joueur a répondu juste : il a gagné
    - Le joueur a répondu faux : il a perdu
- Afficher le chiffre de la seconde carte

# Notions abordées :

## Programmation :

- Conditions
- Manipulation de l’aléatoire

## Autres :

- Utilisation d’un terminal

# Déroulement :

1. Générer deux chiffres aléatoires entre 1 et 9 et les stocker dans deux variables nommées `carte1` et `carte2` ;
2. Afficher à l’écran (sur le Terminal) la valeur de `carte1` ;
3. Afficher à l’écran le message “La prochaine carte sera-t-elle plus grande (tapez +) ou plus petite (tapez -) ?”
4. Récupérer du texte tapé par l’utilisateur (sur le Terminal) et stocker cette valeur dans une variable nommée `joueur` ;
5. Si l’utilisateur à répondu `“+”` :
    1. Si la valeur de la variable `carte2` est supérieur à la valeur de la variable `carte1` :
        
        Alors afficher le message “Vous avez ……………”
        
    2. Si la valeur de la variable `carte2` est inférieur à la valeur de la variable `carte1` :
        
        Alors afficher le message “Vous avez ……………”
        
6. Si l’utilisateur à répondu `“-”` :
    1. Si la valeur de la variable `carte2` est supérieur à la valeur de la variable `carte1` :
        
        Alors afficher le message “Vous avez ……………”
        
    2. Si la valeur de la variable `carte2` est inférieur à la valeur de la variable `carte1` :
        
        Alors afficher le message “Vous avez ……………”
        
7. Afficher la valeur de la variable `carte2`.

# Améliorations :

- Proposer à l’utilisateur de rejouer;
- Avoir un système de score.
- Gérer le cas où l’utilisateur répond autre chose que `+` ou `-`.
