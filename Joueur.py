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
        """
        :param nom: Le nom du joueur
        :param nb_cartes: Le nombre de cartes qu'il possède
        """
        self._nom = nom
        self._nb_cartes = nb_cartes
        self._mainJoueur = []

    #seteur et geteur
    def set_main(self, main : list) -> None:
        """
        Ajoute des cartes dans la main du joueur
        :param main: Une liste de Carte
        """
        self._mainJoueur = main
        
    def get_nom(self) -> str:
        """
        renvoie le nom du joueur
        :return: str
        """
        return self._nom
        
    def get_nb_cartes(self) -> int:
        """
        renvoie le nombre de carte que le joueur possède dans sa main
        :return: int
        """
        return self._nb_cartes

    def jouer_carte(self) -> Carte:
        """
        renvoie la carte qui se situe en haut de la main du joueur
        :return: objet de la classe Carte (ou None en cas d'erreur)
        """
        if self._mainJoueur != []:
            self._nb_cartes -= 1
            return self._mainJoueur.pop()
        return None

    def inserer_main(self, main : list):
        """
        ajout main dans la main du joueur et incrémentation du nombre de cartes du joueur
        :param main: Une liste de carte
        """
        self._nb_cartes += len(main)
        self._mainJoueur = main + self._mainJoueur

    def __str__(self) -> str:
        """
        méthode d'affichage du joueur avec son nom et sa main
        :return: str
        """
        res = f"{self._nom} à la main : \n{self._mainJoueur}"
        return res