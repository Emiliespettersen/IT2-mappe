import pygame
from figur import Figur

class Skudd(Figur):
    def __init__(self, x, y, fiende=False) -> None:
        super().__init__("bilder/skudd.png", x, y)
        if fiende == False:
            self.bilde = pygame.transform.scale_by(self.bilde, 0.3)
        else:
            self.bilde = pygame.transform.scale_by(self.bilde, 0.2)
            self.bilde = pygame.transform.rotate(self.bilde, 180)
        self.fiende = fiende
        self.ramme = self.bilde.get_rect()
        self.ramme.bottom = y
        self.ramme.centerx = x
    
    def skyt(self, x, y):
        self.ramme.bottom = y
        self.ramme.centerx = x    

    def flytt(self):
        if self.fiende == False:
            self.ramme.y -= 5
        else:
            self.ramme.y += 3
        

