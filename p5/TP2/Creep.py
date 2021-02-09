import random

import pygame
from pygame.math import Vector3, Vector2

pass

class Creep:
    def __init__(self):
        self.taille=2
        self.forme= 2
        self.couleur = Vector3 (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        self.position= Vector2 (random.randint(0,400),random.randint(0,400))
        self.direction= Vector2 ()
        pass

    def afficher (self,core):
        pygame.draw.circle(core.screen, (self.couleur.x, self.couleur.y, self.couleur.z),
                           (self.position.x, self.position.y), self.taille)


    def manger(self):
        pass


    def mourir(self):
        pass


    def deplacer(self):
        pass