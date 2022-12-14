import pygame
contexte = pygame.display.set_mode((320, 280))


# Classe Snake qui définira l'objet Snake
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = [x,y]
        self.comp = 1
        self.Snake = [self.head]
        self.direction = ""

    ''' Méthode move, reçoit les paramètres x et y,
    qui seront les nouvelles coordonnées de la tête et
    insérer la nouvelle tête dans le tableau des positions '''
    def move(self, x, y):
        self.head = [x,y]
        self.Snake.append([x,y])

    ''' Méthode gandir, augmente la longueur de la
    serpent '''
    def grandir(self):
        self.comp += 1

    ''' Méthode show, dessine chaque morceau de serpent '''
    def show(self):
        for XY in self.Snake:
            pygame.draw.rect(contexte, (0,0,0), [XY[0], XY[1], 10, 10])

    ''' Méthode piste, supprime la queue lorsque le
    la queue du tableau est supérieure à la longueur du
    serpent '''
    def piste(self):
        if len(self.Snake) > self.comp:
                del self.Snake[0]

    ''' Méthode est morte, vérifiez si Snake a mangé
    lui-même, si oui renvoie vrai, cas
    sinon, renvoie faux '''
    def mort(self):
        if any(Bloco == self.head for Bloco in self.Snake[:-1]):
            return True
        return False

    ''' Méthode réinitialise, réinitialise toutes les valeurs
    de Snake pour les valeurs initiales, au cas où
    après avoir perdu les joueurs veulent continuer'''
    def réinitialise(self,x , y):
        self.x = x
        self.y = y
        self.head = [x,y]
        self.comp = 1
        self.Snake = [self.head]