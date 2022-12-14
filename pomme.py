import pygame
from random import randrange
largeur = 320
hauteur = 280
taille = 10
tableau = 40
contexte = pygame.display.set_mode((largeur,hauteur))

# Classe Pomme qui définira l'objet Pomme
class Pomme:
    def __init__(self):
        self.x = randrange(0,largeur-taille,10)
        self.y = randrange(0,hauteur-taille-tableau,10)

    ''' Méthode show, dessine la pomme sur l'écran '''
    def show(self):
        pygame.draw.rect(contexte, (255,0,0), [self.x, self.y, taille, taille])

    ''' Méthode de repositionnement, définir de nouveaux x et y
    aléatoire pour la pomme après avoir été mangée par le Serpent '''
    def repositionnement(self):
        self.x = randrange(0,largeur-taille,10)
        self.y = randrange(0,hauteur-taille-tableau,10)