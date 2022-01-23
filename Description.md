# projet_cartes
Projet de NSI 

Pour lancer le jeu, utiliser le fichier main.py.
Ce projet dispose d'un affichage avec pygame et si le programme ne marche pas, utiliser REPLIT pour l'affichage
(cependant l'affichage console marche partout)

REGLES DU JEU :

    -soit 52 soit 32 cartes

    -chaque joueur commence la partie avec la moitié des cartes

    -le joueur qui n'a plus de cartes perd

    -en cas de bataille (2 cartes de même valeur) les joueurs posent une carte face cachée puis une face visible


UTILITE DES FICHIERS :

  -Carte -> sert à créer l'objet Carte avec lequel les joueurs jouent

  commandes :
  
    -get_nom : pour avoir le chiffre/figure de la carte 
  
    -get_couleur : pour avoir son symbole
  
    -get_valeur : renvoi la "puissance" de la carte
  
  
-JeuCarte -> sert à créer un jeu composé de Carte de taille saisie par l'utilisateur

  commandes :
  
    -get_taille : renvoi le nombre de cartes (soit 52 soit 32)
  
    -melanger : mélange le paquet
  
    -distribuer_jeu : distribue un même nombre de carte à tous les joueurs
  
-Joueur -> sert à implémenter les différentes actions que les joueurs peuvent utiliser

  commandes :
  
    -set_main : initialise la main du joueur
  
    -get_nom : renvoi le nom du joueur
  
    -get_nb_cartes : renvoi le nombre de cartes présentes dans la main du joueur
  
    -jouer_carte : renvoi la carte en haut de la main du joueur
  
    -inserer_main : ajoute un certain nombre de cartes (contenues dans une liste) dans le bas de la main du joueur
  
  
-Bataille -> contient la fonction pour jouer une partie

  commandes :
  
    -joueur : lance la partie
  
 
