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
        """
        On vérifie le nombre de cartes saisies en entrée
        :param nb_cartes: nombre de cartes que le joueur entre
        """
        assert nb_cartes == 52 or nb_cartes == 32 , "le jeu doit comporter soit 32 soit 52 cartes" #vérification du nombre de carte
        self._jeu = []
        self._taille = nb_cartes

    def get_taille(self) -> int:
        """
        revoi le nombre de cartes dans le paquet
        :return: int
        """
        return int(self._taille)
    
    def creer_jeu(self) -> None:
        """
        deux cas distincts :
            -jeu de 52 cartes :
                on ajoute toutes les cartes d'un jeu normal (sauf les Jokers)
            -jeu de 32 cartes :
                on ajoute toutes les cartes en partant de 7 (vers l'as)
        """
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
        """
        on mélange le jeu à l'aide la commande shuffle
        """
        shuffle(self._jeu)
        
    
    def distribuer(self) -> Carte:
        """
        On vérifie tout d'abbord que le jeu n'est pas vide
        On renvoi ensuite la carte située sur le haut du paquet
        :return: Une Carte
        """
        assert len(self._jeu)>0 ,"veuillez créer le jeu avec creer_jeu()"
        carte = self._jeu.pop(-1) #carte sur le haut du paquet
        return carte

    def distribuer_jeu(self,nbcarte : int ,nbjoueurs : int) -> list:
        """
        On distribue le nombre de cartes souhaitées aux nombre de joueurs (on vérifie que c'est possible)
        :param nbcarte: Nombre qu'on souhaite distribuer aux joueurs
        :param nbjoueurs: Nombre de joueurs
        :return: Une liste de listes
        """
        assert nbcarte*nbjoueurs<= self.get_taille(),"le nombre de cartes souhaitées est trop grand"
        liste_retour = []
        for i in range(nbjoueurs) :
            liste_retour.append([])
            for j in range(nbcarte) :
                liste_retour[i].append(self.distribuer())
        return liste_retour

    def __str__(self) -> str:
        """
        méthode d'afichage
        :return: str
        """
        res = ""
        for elt in self._jeu :
            res = res + str(elt) +", "
        return res


def test_jeu() :
    jeu = JeuCarte(32)
    jeu.creer_jeu()
    print(jeu.get_taille())
    print(jeu)
    jeu.melanger()
    print(jeu)
    print(jeu.distribuer())
    print(jeu.distribuer_jeu(10,2))
    print(jeu.get_taille())
    
#test_jeu()