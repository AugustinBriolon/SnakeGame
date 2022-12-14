import pygame
contexte = pygame.display.set_mode((320,280))

# Classe Texte définira les éléments de l'objet
class Texte:
    def __init__(self, msg, cor, tam):
        self.font = pygame.font.SysFont(None, tam)
        self.Texte = self.font.render(msg, True, cor)
        
    def show(self, x, y):
        contexte.blit(self.Texte, [x, y])