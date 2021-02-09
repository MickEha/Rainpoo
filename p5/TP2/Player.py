import pygame
from pygame.math import Vector3, Vector2

pass

class Player:
    def __init__(self):
        self.taille=100
        self.couleur = Vector3(255,0,0)
        self.position= Vector2 ()
        self.direction= Vector2()
        self.forme ='rond'

    def afficher (self,core):
        if self.forme == 'rond':
            pygame.draw.circle(core.screen,(self.couleur.x,self.couleur.y,self.couleur.z),(self.position.x,self.position.y),self.taille)


    def manger(self):
        pass


    def mourir(self):
        pass


    def deplacer(self,position):
        self.position.x = position[0]
        self.position.y = position[1]