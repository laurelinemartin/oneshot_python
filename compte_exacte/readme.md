# Résumé :

Réaliser un programme simple dont le but est de faire deviner à l’utilisateur un chiffre ou un nombre tiré au hasard par l’ordinateur avec pour seules indications “c’est supérieur” et “c’est inférieur”.

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Au choix

# Fonctionnalités :

- Tirer un chiffre aléatoirement ;
- Demander à l’utilisateur de deviner le chiffre auquel “pense” l’ordinateur ;
- Si :
    - L’utilisateur donne un chiffre trop grand, l’ordinateur lui indique que le chiffre à deviner est plus petit ;
    - L’utilisateur donne un chiffre trop petit, l’ordinateur lui indique que le chiffre à deviner est plus grand ;
    - L’utilisateur donne un chiffre exact, l’ordinateur lui indique qu’il a gagné.

# Notions abordées :

## Programmation :

- Conditions ;
- Manipulation de l’aléatoire.

## Autres :

- Utilisation d’un terminal.

# Déroulement :

1. Générer un chiffre aléatoire entre 1 et 10 et le stocker dans une variable nommée `ordinateur` ;
2. Afficher à l’écran (sur le Terminal) le message “`Devine le chiffre auquel je pens` ” ;
3. Récupérer le chiffre tapé par l’utilisateur (sur le Terminal) et stocker cette valeur dans une variable nommée `joueur` (attention ! cette valeur doit être un nombre entier, pas une chaîne de caractère !) ;
4. Si l’utilisateur a répondu un chiffre trop grand :
    
    Alors, afficher le message “`Le chiffre auquel je pense est plus …`" .
    
5. Si l’utilisateur a répondu un chiffre trop petit :
    
    Alors, afficher le message “`Le chiffre auquel je pense est plus ...`”.
    
6. Si l’utilisateur a répondu le chiffre exact :
    
    Alors, afficher le message “`Vous avez trouvé !`".
    

# Améliorations :

- Permettre à l’utilisateur de retenter sa chance jusqu’à ce qu’il tombe juste ;
- Permettre à l’utilisateur de retenter sa chance un nombre défini de fois (nombre de tentatives limité) ;
- Proposer à l’utilisateur de rejouer;
- Avoir un système de score.
- Gérer le cas où l’utilisateur répond autre chose qu’un chiffre ;
- Gérer le cas où l’utilisateur répond un chiffre en dehors de l’intervalle du chiffre tiré aléatoirement ;
- Proposer à l’utilisateur de choisir la valeur minimal et maximal du chiffre aléatoire tirée par l’ordinateur.
