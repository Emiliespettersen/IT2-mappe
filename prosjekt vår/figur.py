import pygame

class Figur ():
    def __init__(self, bildesti: str, x, y) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale_by(self.bilde, 0.2)
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
    
    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)