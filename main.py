import pygame
from random import randrange
from snake import Snake
from texte import Texte
from pomme import Pomme

# Utilisation d'un bloc d'essais et d'erreurs pour vérifier si pygame a démarré correctement
try:
    pygame.init()
    print("Le module pygame a été initialisé avec succès")
except:
    print("Le module pygame n'a pas été initialisé avec succès")

# Varibales tailles, couleurs et controle
largeur = 320
hauteur = 280
taille = 10
tableau = 40
blanc = (255,255,255)
noir = (0,0,0)
rouge = (255,0,0)
orange = (255,69,0)
vue = pygame.time.Clock()
contexte = pygame.display.set_mode((largeur,hauteur))
pygame.display.set_caption("Snake Game")

# Classe Game qui définira l'objet Game
class Game:
    def __init__(self):
        self.play = True
        self.perdre = False
        self.pos_x=randrange(0,largeur-taille,10)
        self.pos_y=randrange(0,hauteur-taille-tableau,10)
        self.vitesse_x=0
        self.vitesse_y=0
        self.point = 0
        self.Snake = Snake(self.pos_x, self.pos_y)
        self.Pomme = Pomme()

    # Méthode de démarrage du jeu
    def start(self):
        while self.play:

            # Vérifiez si le joueur n'a pas encore perdu le jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.Snake.direction != "droit":
                        self.Snake.direction = "gauche"
                    if event.key == pygame.K_RIGHT and self.Snake.direction != "gauche":
                        self.Snake.direction = "droit"
                    if event.key == pygame.K_UP and self.Snake.direction != "bas":
                        self.Snake.direction = "haut"
                    if event.key == pygame.K_DOWN and self.Snake.direction != "haut":
                        self.Snake.direction = "bas"
                    if event.key == pygame.K_SPACE:
                        self.Snake.grandir()

            if self.play:
                contexte.fill(blanc)
                # Vérifie la direction de Snake
                if self.Snake.direction == "haut":
                    self.pos_y -= taille
                elif self.Snake.direction == "bas":
                    self.pos_y += taille
                elif self.Snake.direction == "gauche":
                    self.pos_x -= taille
                elif self.Snake.direction == "droit":
                    self.pos_x += taille
                else:
                    pass
                # Vérifie si Snake a mangé la pomme
                if self.pos_x == self.Pomme.x and self.pos_y == self.Pomme.y:
                    self.Pomme.repositionnement()
                    self.Snake.grandir()
                    self.point += 1

                if self.pos_x + taille > largeur:
                    self.play = False
                    self.perdre = True
                    self.perdu()
                if self.pos_x < 0:
                    self.play = False
                    self.perdre = True
                    self.perdu()
                if self.pos_y + taille > hauteur:
                    self.play = False
                    self.perdre = True
                    self.perdu()
                if self.pos_y < 0:
                    self.play = False
                    self.perdre = True
                    self.perdu()

                self.Snake.move(self.pos_x, self.pos_y)
                # Efface la piste laissée par des blocs supplémentaires
                self.Snake.piste()
                # Vérifie si Snake est mort
                if self.Snake.mort():
                    self.play = False
                    self.perdre = True
                    self.perdu()
                # Dessine Snake et la Pomme sur l'écran 
                self.Snake.show()
                self.Pomme.show()
                # Dessine le tableau et le texte contenant le score actuel
                pygame.draw.rect(contexte, noir, [0, hauteur-tableau, largeur, tableau])
                texteTableau = Texte("Score : "+str(self.point), blanc, 25)
                texteTableau.show(10, hauteur-30)
                # Met à jour tout l'écran avec tous éléments précédemment dessinés 
                pygame.display.update()
                # Définit les fps du jeu 
                vue.tick(15)
        return 0

    # Méthode perdu,le joueur peut retourner jouer ou quitter le jeu
    def perdu(self):
        while self.perdre:
            # Efface l'écran à chaque nouveau début de boucle ou recommencer le jeu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                    self.perdre = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.play = True
                        self.perdre = False
                        self.pos_x=randrange(0,largeur-taille,10)
                        self.pos_y=randrange(0,hauteur-taille-tableau,10)
                        self.Snake.direction = ""
                        self.Pomme.repositionnement()
                        self.Snake.réinitialise(self.pos_x, self.pos_y)
                        self.vitesse_x=0
                        self.vitesse_y=0
                        self.point = 0
                    if event.key == pygame.K_s:
                        self.play = False
                        self.perdre = False
            
            contexte.fill(blanc)
            # Affiche l'écran de fin de jeu 
            textePerdu = Texte("Fin du Jeu", orange, 50)
            textePerdu.show(75, 30)
            texteScore = Texte("Votre Score Final : "+str(self.point), noir, 30)
            texteScore.show(65, 80)
            texteContinuer = Texte("Recommencer ? (C)", noir, 30)
            texteContinuer.show(70, 140)
            texteSortir = Texte("Partir ? (S)", noir, 30)
            texteSortir.show(115, hauteur-30)
            # Met à jour l'écran avec tous les éléments 
            pygame.display.update()
        return 0

# Commence de jeu 
game = Game()
game.start()
# Fermer le jeu 
pygame.quit()