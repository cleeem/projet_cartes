import time
from JeuCarte import *
from Carte import *
from Joueur import *
import pygame

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

class Bataille :
    def __init__(self,nom1 : str ,nom2 : str, nb_cartes = 52)  :
        #création du jeu
        self.jeu = JeuCarte(nb_cartes)
        #création des joueurs
        self.j1 = Joueur(nom1,int(self.jeu.get_taille()/2))
        self.j2 = Joueur(nom2,int(self.jeu.get_taille()/2))

    def jouer(self) :
        self.jeu.creer_jeu() #ajout des cartes dans le jeu
        self.jeu.melanger() #melange des cartes

        #attribution des mains aux joueurs
        liste_distribution = self.jeu.distribuer_jeu(self.jeu.get_taille(),2)
        self.j1.set_main(liste_distribution[0])
        self.j2.set_main(liste_distribution[1])

        print(f"Début de la partie : \nLe joueur {self.j1.get_nom()} possède {self.j1.get_nb_cartes()}\nLe joueur {self.j2.get_nom()} possède {self.j2.get_nb_cartes()}")
        print("")
        while self.j1.get_nb_cartes()>0 and self.j2.get_nb_cartes() > 0 : #tant que la partie n'est pas finie
            table = [] #liste des cartes jouées

            #les joueurs retournent leurs cartes
            carte1 = self.j1.jouer_carte()
            carte2 = self.j2.jouer_carte()

            #on ajoute les cartes sur la table
            table.append(carte1)
            table.append(carte2)

            print(f"Les cartes sont : \n{self.j1.get_nom()} : {carte1}\n{self.j2.get_nom()} : {carte2}")

            while carte1.get_valeur() == carte2.get_valeur() and (self.j1.get_nb_cartes()>=2 and self.j2.get_nb_cartes()>=2): #si il y a une "bataille on continue jusqu'à obtenir 2 cartes différentes"
                print("BATAILLE")
                #ce tirage représente les cartes face cachées
                cachée_1  = self.j1.jouer_carte()
                cachée_2  = self.j2.jouer_carte()
                table.append(cachée_1)
                table.append(cachée_2)

                #tirage des 2 autres cartes mais face visible
                carte1 = self.j1.jouer_carte()
                carte2 = self.j2.jouer_carte()
                print(f"Les cartes suivantes sont : \n{self.j1.get_nom()} : {carte1} et {self.j2.get_nom()} : {carte2}")
                table.append(carte1)
                table.append(carte2)


            if carte1.get_valeur()>carte2.get_valeur() :
                self.j1.inserer_main(table)
                print(f"Le joueur {self.j1.get_nom()} récupère {len(table)} cartes, il en a : {self.j1.get_nb_cartes()}\nLe joueur {self.j2.get_nom()} en a : {int(self.j2.get_nb_cartes())}")
            else :
                self.j2.inserer_main(table)
                print(f"Le joueur {self.j2.get_nom()} récupère {len(table)} cartes, il en a : {self.j2.get_nb_cartes()}\nLe joueur {self.j1.get_nom()} en a : {int(self.j1.get_nb_cartes())}")
            print("")

            #time.sleep(0.75)

        if self.j1.get_nb_cartes()>self.j2.get_nb_cartes() : #celui qui possède le plus de carte gagne
            print(f"le joueur {self.j1.get_nom()} a gagné la partie")
        else :
            print(f"le joueur {self.j2.get_nom()} a gagné la partie")
    
