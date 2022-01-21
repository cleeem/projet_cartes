couleurs =["CARREAU","COEUR","TREFLE","PIQUE"]
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

class Carte :
    def __init__(self,nom : str ,couleur : str) : #initialisation des différents attributs
        self._nom = nom
        self._couleur = couleur
        self._valeur = valeurs[nom]
    
    #méthodes geteur
    def get_nom(self) -> str :
        return self._nom
    
    def get_couleur(self) -> str :
        return self._couleur
    
    def get_valeur(self) -> int :
        return int(self._valeur)
    
    #méthodes "internes" à la classe
    def __eq__(self,carte) -> bool:
        
        if self.get_valeur() == carte.get_valeur() :
            return True
        else :
            return False
        
    def __lt__(self,carte) -> bool:
        if self._valeur < carte.get_valeur() :
            return True
        else :
            return False

    def __gt__(self,carte) -> bool:
        if self._valeur > carte.get_valeur() :
            return True
        else :
            return False

    def __str__(self) -> str:
        if self.get_couleur() == "CARREAU" :
            return f"|{self.get_nom()[0]}|♦"

        elif self.get_couleur() == "COEUR" :
            return f"|{self.get_nom()[0]}|♥"
        
        elif self.get_couleur() == "TREFLE" :
            return f"|{self.get_nom()[0]}|♣"
        
        elif self.get_couleur() == "PIQUE" :
            return f"|{self.get_nom()[0]}|♠"

    def __repr__(self) -> str:
        return f"{self._nom} de {self._couleur}"