from Carte import *
from random import random,randint,shuffle
couleurs =["CARREAU","COEUR","TREFLE","PIQUE"]
noms = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
valeurs = {
    "2" : 2 ,
    "3" : 3 ,
    "4" : 4 ,
    "5" : 5 ,
    "6" : 6 ,
    "7" : 7 ,
    "8" : 8 ,
    "9" : 9 ,
    "10" : 10 ,
    "Valet" : 11 ,
    "Dame" : 12 ,
    "Roi" : 13 ,
    "As" : 14 ,
}


class JeuCarte :
    def __init__(self,nb_cartes : int = 52) : #initialisation des différents attributs
        assert nb_cartes == 52 or nb_cartes == 32 , "le jeu doit comporter soit 32 soit 52 cartes" #vérification du nombre de carte
        self._jeu = []
        self._taille = nb_cartes

    def get_taille(self) -> int: #revoi le nombre de cartes dans le paquet
        return int(self._taille)
    
    def creer_jeu(self) -> None:
        #si le jeu contient 52 cartes
        if self._taille == 52 :
            for color in couleurs :
                for nom in noms :
                    self._jeu.append(Carte(nom,color))
        else :
        #si le jeu contient 32 cartes on commence à partir du 7
            for color in couleurs :
                for nom in noms[5:] : 
                    self._jeu.append(Carte(nom,color))

    def melanger(self) -> None:
        shuffle(self._jeu)
    
    def distribuer(self) -> Carte:
        assert len(self._jeu)>0 ,"veuillez créer le jeu avec creer_jeu()"
        carte = self._jeu.pop(-1) #carte sur le haut du paquet
        return carte

    def distribuer_jeu(self,nbcarte : int ,nbjoueurs : int) -> list:
        nb_distributions = int(nbcarte/nbjoueurs) #pour que tous les joueurs aient le même nombre de cartes
        liste_retour = []
        for i in range(nbjoueurs) :
            liste_retour.append([])
            for j in range(nb_distributions) :
                liste_retour[i].append(self.distribuer())
        return liste_retour

    def __str__(self) -> str:
        res = ""
        for elt in self._jeu :
            res = res + str(elt) +", "
        return res