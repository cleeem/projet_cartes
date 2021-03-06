from Carte import *
from JeuCarte import *
from Joueur import *
from Bataille import *
import time
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

def get_url(carte : Carte) :
    couleur = carte.get_couleur().lower()
    nom = carte.get_nom().lower()
    if len(nom)>1 :
        url = f"images_cartes/{nom}_{couleur}.png"
        return url
    else :
        url = f"images_cartes/{nom}_{couleur}.png"
        return url

class Game:
    def __init__(self, screen,font):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.area = pygame.Rect(0,0,0,0)
        self.area_color = "black"
        self.font = font
        self.nb_tours = 0

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def display(self):
        self.screen.fill((0,120,0))
        pygame.draw.rect(self.screen, self.area_color, self.area)

        texte = f"{j1.get_nom()} VS {j2.get_nom()}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (300, 600))

        largeur = 71
        hauteur = 97
        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere,(100,150))
        screen.blit(arriere,(1080-(100+71),150))

        texte = f"Nombre de tours : {self.nb_tours}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (0, 0))

        nb_carte_1 = j1.get_nb_cartes()
        nb_carte_2 = j2.get_nb_cartes()
        texte = f"{j1.get_nom()} : {nb_carte_1} cartes || {j2.get_nom()}  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))

        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 350))
        screen.blit(image_2, (1080 - (100 + 71), 350))

        if self.carte1.get_valeur() > self.carte2.get_valeur():
            texte = f"Le joueur {j1.get_nom()} a gagn?? le tour"
            aff = self.font.render(texte, True, "black")
            screen.blit(aff, (200, 500))

        else:
            texte = f"Le joueur {j2.get_nom()} a gagn?? le tour"
            aff = self.font.render(texte, True, "black")
            screen.blit(aff, (200, 500))

        pygame.display.flip()

    def bataille(self):
        self.screen.fill((0, 120, 0))
        pygame.draw.rect(self.screen, self.area_color, self.area)

        texte = f"{j1.get_nom()} VS {j2.get_nom()}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (300, 600))

        largeur = 71
        hauteur = 97
        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere, (100, 150))
        screen.blit(arriere, (1080 - (100 + 71), 150))

        texte = f"Nombre de tours : {self.nb_tours}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (0, 0))

        nb_carte_1 = j1.get_nb_cartes()
        nb_carte_2 = j2.get_nb_cartes()
        texte = f"{j1.get_nom()}: {nb_carte_1} cartes || {j2.get_nom()}  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))

        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 350))
        screen.blit(image_2, (1080 - (100 + 71), 350))

        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere, (100, 350+self.pixel_bataille))
        screen.blit(arriere, (1080 - (100 + 71), 350+self.pixel_bataille))

        texte = f"BATAILLE"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (375, 320))

        pygame.display.flip()
        time.sleep(1)

        self.carte1 = j1.jouer_carte()
        self.carte2 = j2.jouer_carte()
        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 350+self.pixel_bataille))
        screen.blit(image_2, (1080 - (100 + 71), 350+self.pixel_bataille))

        pygame.display.flip()

    def fin_joueur_1(self):
        self.screen.fill((0, 120, 0))
        pygame.draw.rect(self.screen, self.area_color, self.area)

        texte = f"{j1.get_nom()} VS {j2.get_nom()}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (300, 600))

        largeur = 71
        hauteur = 97
        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere, (100, 150))
        screen.blit(arriere, (1080 - (100 + 71), 150))

        texte = f"Nombre de tours : {self.nb_tours}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (0, 0))

        nb_carte_1 = j1.get_nb_cartes()
        nb_carte_2 = j2.get_nb_cartes()
        texte = f"{j1.get_nom()}  : {nb_carte_1} cartes || {j2.get_nom()}  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))


        texte = f"Le joueur {j1.get_nom()} a gagn?? la partie"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (350, 500))

        pygame.display.flip()

        time.sleep(5)

    def fin_joueur_2(self):
        self.screen.fill((0, 120, 0))
        pygame.draw.rect(self.screen, self.area_color, self.area)

        texte = f"{j1.get_nom()} VS {j2.get_nom()}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (300, 600))

        largeur = 71
        hauteur = 97
        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere, (100, 150))
        screen.blit(arriere, (1080 - (100 + 71), 150))

        texte = f"Nombre de tours : {self.nb_tours}"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (0, 0))

        nb_carte_1 = j1.get_nb_cartes()
        nb_carte_2 = j2.get_nb_cartes()
        texte = f"{j1.get_nom()}  : {nb_carte_1} cartes || {j2.get_nom()}  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))

        texte = f"Le joueur {j2.get_nom()} a gagn?? la partie"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (200, 500))

        pygame.display.flip()

        time.sleep(5)


    def jouer(self):
        if j1.get_nb_cartes()>0 and j2.get_nb_cartes()>0 :
            table = []
            self.carte1 = j1.jouer_carte()
            self.carte2 = j2.jouer_carte()
            table =  [self.carte1,self.carte2]

            self.display()

            self.pixel_bataille = 0

            while self.carte1 == self.carte2 and (j1.get_nb_cartes()>=2 and j2.get_nb_cartes()>=2) :

                self.pixel_bataille += 20

                table.append(j1.jouer_carte())
                table.append(j2.jouer_carte())

                table.append(self.carte1)
                table.append(self.carte2)

                self.bataille()

            self.pixel_bataille = 0

            if self.carte1.get_valeur() > self.carte2.get_valeur():
                j1.inserer_main(table)

            else:
                j2.inserer_main(table)

        else :
            if j1.get_nb_cartes() > j2.get_nb_cartes():  # celui qui poss??de le plus de carte gagne
                self.fin_joueur_1()
                self.running = False
            else:
                self.fin_joueur_2()
                self.running = False

            pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.jouer()
            self.clock.tick(60)
            self.nb_tours += 1
            time.sleep(1)
            


nb=int(input("choississez l'affichage : \n 1 pour la console \n 2 pour pygame \n"))
j1 = str(input("entrez le nom du premier joueur "))
j2 = str(input("entrez le nom du deuxi??me joueur "))
b=int(input("Combien de cartes ? "))
if nb==1 :
#affichage en console
    if b==32:
        B = Bataille(j1,j2,32)
        B.jouer()
    elif b==52:
        B = Bataille(j1,j2,52)
        B.jouer()
    else:
        print("Le jeu de bataille se joue soit avec 32 cartes, soit avec 52. ")

elif nb==2 :
    #affichage avec pygame
    if b==32 or b==52 :
        c=Bataille(j1,j2,b)
        j1,j2 = c.get_joueur()
        c.start()
    
        pygame.init()
        screen = pygame.display.set_mode((1080,720))
        font = pygame.font.SysFont("monospace",30)
        game = Game(screen,font)
        game.run()
    
        pygame.quit()
    else:
        print("nombre de carte incorrect")
