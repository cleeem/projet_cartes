from Carte import *
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

class Joueur:
    def __init__(self, nom : str , nb_cartes : int):
        self._nom = nom
        self._nb_cartes = nb_cartes
        self._mainJoueur = []

    #seteur et geteur
    def set_main(self, main : list):
        self._mainJoueur = main
        
    def get_nom(self):
        return self._nom
        
    def get_nb_cartes(self):
        return self._nb_cartes
        
    #renvoi une Carte
    def jouer_carte(self) -> Carte:
        if self._mainJoueur != []:
            self._nb_cartes -= 1
            return self._mainJoueur.pop()
        return None

        
    def inserer_main(self, main : list):
        self._nb_cartes += len(main)
        self._mainJoueur = main + self._mainJoueur

    def __str__(self) -> str:
        res = f"{self._nom} à la main : \n{self._mainJoueur}"
        return res