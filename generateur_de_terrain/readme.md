# Résumé :

Implémenter un programme qui permet de générer des images de texture de terrains de manière procédurale.
Utiliser pour cela, utiliser la bibliothèque PIL/Pillow qui permet de créer et de sauvegarder une image et la bibliothèque Perlin Noise qui permet de générer un pixel 

# Domaine :

![programmation.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89d0a8a9-5a49-4737-9cbd-867fc4f478a9/programmation.png)

![rgb-cmy.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b3534a5-b714-4e49-b95a-e54a90e1b362/rgb-cmy.png)

# Difficulté :

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

![etoile.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87bb1a61-62a4-41b0-9070-179ca3d67ecb/etoile.png)

# Langage de programmation :

- Python
- Les bibliothèques PIL/Pillow et Perlin Noise

# Fonctionnalités :

- Générer une image de texture de terrain.

# Ressources :

La bibliothèque Perlin Noise : https://pypi.org/project/noise/ 

La bibliothèque PIL / Pillow : https://pypi.org/project/PIL/ et https://pypi.org/project/Pillow/

# Notions abordées :

## Programmation :

- Définir et appeler des fonctions ;
- Utiliser une boucle ;
- Utiliser des bibliothèques Python.

## Autres :

- Gestion d’une image pixel par pixel
- Gestion des couleur au format R, V, B 255.

# Déroulement :

1. Importer les bibliothèques nécessaires :
    
    `from PIL import Image
    import noise` ;
    
2. Créer une variable `dimensions` contenant les dimensions en pixels de l’image à générer (plus l’image est grande, plus le programme est long)
`dimensions = (512, 512)` ;
3. Créer une variable `fichier` contenant la chaîne de caractère du nom du fichier ;
4. Définir les paramètres pour Perlin Noise :
`scale = 25
persi = 1.75
lacu = 0.16
octa = 2` ;
5. Créer une variable `image` contenant un objet Image initialisé :
`img = Image.new (mode = "RGB",size = shape)` ;
6. Définir une fonction nommée `definirCouleurPixel` prenant comme argument `x, y` (les coordonnées du pixel), `img` (l’image) et `pixel` (un nombre générer par la fonction `pnoise` expliquée à l’étape **11**) ;
7. Créer plusieurs variables contenant des tuples de couleurs :
Par exemple :
`rouge = (255, 0, 0)
 vert = (0, 255, 0)
 bleu = (0, 0, 255)
 jaune = (255, 255, 0)
 cyan = (0, 255, 255)
 magenta = (255, 0, 0)` 
*Note : Ces couleurs sont indicatives, elles ne généreront pas un joli terrain, il faut les modifier selon l’image que l’on souhaite obtenir* ;
8. Sélectionner une couleur en fonction de la valeur de `pixel`. Implémenter des conditions comparant les valeurs de `pixel` à des valeurs décimales comprises entre -1 et 1.
Par exemple :
`if pixel >= -1 and pixel < -0.45:
        img.putpixel((i,j), rouge)
 elif pixel >= -0.45 and pixel < -0.1:
        img.putpixel((i,j), vert)
 #...
else:
        img.putpixel((i,j), cyan)`
*Note : Ces conditions sont indicatives, elles ne généreront pas un joli terrain, il faut les modifier selon l’image que l’on souhaite obtenir* ;
9. Fin de la définition de la fonction.
10. Créer une double boucle parcourant chaque valeur de `dimensions[0]` et `dimensions[1]` ;
11. Utiliser la fonction `pnoise` pour générer un nombre aléatoire entre -1 et 1 proche des pixels adjacents et stocker le résultat dans la variable `pixel` :
`pixel = noise.pnoise2(i/scale,j/scale, octaves = octa , persistence = persi , lacunarity = lacu)` ;
12. Appeler la fonction `definirCouleurPixel`
13. Sortir de la boucle ;
14. Sauvegarder l’image : `img.save(NomFich).`

# Améliorations :

- Modifier les différents paramètres pour changer l’image ;
- Modifier les couleurs ;
- Afficher dans le terminal l’avancement du programme (en pourcentage ou en barre d’avancement) ;
- Essayer différents types de terrains comme une montagne, une plaine, de l’eau, un parterre de feuille mortes, un volcan…

---
