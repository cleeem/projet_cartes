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
        """
        :param nom: Correspond au nom de la carte
        :param couleur: Correspond au signe de la carte
        """
        self._nom = nom
        self._couleur = couleur
        self._valeur = valeurs[nom]
    
    #méthodes geteur
    def get_nom(self) -> str :
        """
        Retourne le nom de la carte
        :return: str
        """
        return self._nom
    
    def get_couleur(self) -> str :
        """
        Retourne la couleur de la Carte
        :return: str
        """
        return self._couleur
    
    def get_valeur(self) -> int :
        """
        Retourne la valeur de la carte
        :return: int
        """
        return int(self._valeur)
    
    #méthodes "internes" à la classe
    def __eq__(self,carte) -> bool:
        """
        regarde si les valeur des cartes sont les mêmes
        :param carte: objet de la classe Carte avec laquelle on effectue la comparaison
        :return: Booléen du résultat
        """
        if self.get_valeur() == carte.get_valeur() :
            return True
        else :
            return False
        
    def __lt__(self,carte) -> bool:
        """
        regarde si la valeur de l'objet self est inférieur à la valeur de la carte en entrée
        :param carte: objet de la classe Carte avec laquelle on effectue la comparaison
        :return: Booléen du résultat
        """
        if self._valeur < carte.get_valeur() :
            return True
        else :
            return False

    def __gt__(self,carte) -> bool:
        """
        regarde si la valeur de l'objet self est supérieur à la valeur de la carte en entrée
        :param carte: objet de la classe Carte avec laquelle on effectue la comparaison
        :return: Booléen du résultat
        """
        if self._valeur > carte.get_valeur() :
            return True
        else :
            return False

    def __str__(self) -> str:
        """
        retourne un affichage "agréable" en console
        :return: str
        """
        if  self.get_nom() == "10" :
            if self.get_couleur() == "CARREAU" :
                return f"|{self.get_nom()}|♦"

            elif self.get_couleur() == "COEUR" :
                return f"|{self.get_nom()}|♥"
            
            elif self.get_couleur() == "TREFLE" :
                return f"|{self.get_nom()}|♣"
            
            elif self.get_couleur() == "PIQUE" :
                return f"|{self.get_nom()}|♠"
        else :
            if self.get_couleur() == "CARREAU" :
                return f"|{self.get_nom()[0]}|♦"

            elif self.get_couleur() == "COEUR" :
                return f"|{self.get_nom()[0]}|♥"
            
            elif self.get_couleur() == "TREFLE" :
                return f"|{self.get_nom()[0]}|♣"
            
            elif self.get_couleur() == "PIQUE" :
                return f"|{self.get_nom()[0]}|♠"

    def __repr__(self) -> str:
        """
        Donne la représentation de la carte
        :return: str
        """
        return f"{self._nom} de {self._couleur}"



def test_carte() :
    carte = Carte("As","COEUR")
    print(carte.get_nom())
    print(carte.get_couleur())
    print(carte.get_valeur())
    print(carte)

#test_carte()