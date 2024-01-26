# jeu de Nim

# Résumé :

Le jeu de Nim est un jeu à 2 joueurs. À tour de rôle, chaque joueur peut retirer 1, 2 ou 3 allumettes. Dans cette variante, le joueur qui retire la dernière allumette a gagné.

Le but de cette activité est de trouver et d’implémenter une stratégie gagnante au jeu de Nim. L’ordinateur doit gagner à tous les coups contre un humain.

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Au choix

# Fonctionnalités :

- L’utilisateur doit pouvoir indiquer le nombre d’allumette qu’il veut retirer (1, 2 ou 3) ;
- Le programme est le 2nd joueur.
- Le programme doit pouvoir savoir le nombre d’allumette à enlever pour gagner.

# Notions abordées :

## Programmation :

- Conditions ;
- Boucles ;
- Tableaux à une dimension (i.e. listes).

## Autres :

- Utilisation du Terminal ;
- Algorithmique.

# Déroulement :

1. Élaborer sur papier une stratégie gagnante ;
2. Créer un tableau à une dimension (i.e. une liste) de 20 cases (pour les 20 bâtonnets). Nommer ce tableau `jeu` ;
3. Initialiser ce tableau en mettant un `'|'` dans chaque case de ce tableau ;
4. Créer une variable `joueur` initialisée à 0. Cette variable stockera le nombre d’allumettes que le joueur retirera ;
5. Créer une variable `allumettes` initialisée à 20. Cette variable permet de savoir combien d’allumettes il reste ;
6. Tant que le nombre d’`allumettes` est supérieur à 0 :
    1. Afficher dans le terminal le nombre d’allumettes restantes;
    2. Demander au joueur combien d’allumette il souhaite retirer et stocker ;
    3. Retirer le nombre d’allumettes demander par le joueur à la variable `allumettes` :
        
        `allumettes = allumettes - joueur`
        
    4. Retirer le nombre d’allumettes demandé par le joueur du tableau `jeu` (par exemple, remplacer par `' '`) ;
        
        Par exemple : 
        `for(int i = allumettes; i < allumettes + joueur; i++) { 
             jeu[i] = ' ';
        }`
        
    5. Si le tableau est vide :
        
        Alors, afficher que le joueur a gagné et arrêter la boucle.
        
    6. Implémenter la stratégie gagnante pour l’ordinateur et retirer le nombre d’allumettes à la variable `allumettes` et au tableau `jeu` ;
    7. Si le tableau est vide :
        
        Alors, afficher que l’ordinateur a gagné.
        

# Améliorations :

- Si la stratégie adoptée est gagnante à coup sûr pour l’ordinateur, l’étape **e** n’est pas nécessaire.
- Gérer le cas où l’utilisateur répond autre chose que 1, 2 ou 3.
- Programmer la stratégie gagnante pour l’ordinateur de la variante où le dernier joueur à retirer une allumette perd.

# Ressources :

> Expliquons en détail la version utilisée dans l'émission de *[Fort Boyard](https://fr.wikipedia.org/wiki/Fort_Boyard_(jeu_t%C3%A9l%C3%A9vis%C3%A9))*, un tel jeu constitue le duel des *bâtonnets* contre un *maître des ténèbres* (le tas comprend 20 allumettes). Ce jeu consiste à enlever 1, 2 ou 3 bâtonnets à chaque tour. Le vainqueur est celui qui peut jouer en dernier. Voici un exemple de partie :
20 → 19 → 16 → 13 → 12 → 10 → 8 → 5 → 4 → 3 → 0
> 
> 
> [*https://fr.wikipedia.org/wiki/Jeux_de_Nim](https://fr.wikipedia.org/wiki/Jeux_de_Nim)* 
> 

Dans cet exemple, le joueur bleu gagne.
