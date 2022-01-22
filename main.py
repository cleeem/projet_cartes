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

#affichage en console
#b = Bataille("j1","j2",32)
#b.jouer()


#affichage avec pygame
c=Bataille("Kura le noir","Bonsoir",32)
j1,j2 = c.get_joueur()
c.start()

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
        texte = f"Joueur 1 : {nb_carte_1} cartes || Joueur 2  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))


        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 350))
        screen.blit(image_2, (1080 - (100 + 71), 350))

        if self.carte1.get_valeur() > self.carte2.get_valeur():
            texte = f"Le joueur {j1.get_nom()} a gagné le tour"
            aff = self.font.render(texte, True, "black")
            screen.blit(aff, (200, 500))

        else:
            texte = f"Le joueur {j2.get_nom()} a gagné le tour"
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
        texte = f"Joueur 1 : {nb_carte_1} cartes || Joueur 2  : {nb_carte_2} cartes"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (100, 100))

        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 350))
        screen.blit(image_2, (1080 - (100 + 71), 350))

        arriere = pygame.image.load("images_cartes/arriere.jpg")
        screen.blit(arriere, (100, 320))
        screen.blit(arriere, (1080 - (100 + 71), 320))

        texte = f"BATAILLE"
        aff = self.font.render(texte, True, "black")
        screen.blit(aff, (375, 320))

        pygame.display.flip()
        time.sleep(0)

        self.carte1 = j1.jouer_carte()
        self.carte2 = j2.jouer_carte()
        url_1 = get_url(self.carte1)
        url_2 = get_url(self.carte2)
        image_1 = pygame.image.load(url_1)
        image_2 = pygame.image.load(url_2)
        screen.blit(image_1, (100, 320))
        screen.blit(image_2, (1080 - (100 + 71), 320))

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


        texte = f"Le joueur {j1.get_nom()} a gagné la partie"
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

        texte = f"Le joueur {j2.get_nom()} a gagné la partie"
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
            while self.carte1 == self.carte2 and (j1.get_nb_cartes()>=2 and j2.get_nb_cartes()>=2) :
                table.append(j1.jouer_carte())
                table.append(j2.jouer_carte())

                table.append(self.carte1)
                table.append(self.carte2)

                self.bataille()

                time.sleep(0)


            if self.carte1.get_valeur() > self.carte2.get_valeur():
                j1.inserer_main(table)

            else:
                j2.inserer_main(table)

        else :
            if j1.get_nb_cartes() > j2.get_nb_cartes():  # celui qui possède le plus de carte gagne
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
            self.display()
            self.clock.tick(60)
            self.nb_tours += 1
            time.sleep(0.1)

pygame.init()
screen = pygame.display.set_mode((1080,720))
font = pygame.font.SysFont("monospace",30)
game = Game(screen,font)
game.run()

pygame.quit()



