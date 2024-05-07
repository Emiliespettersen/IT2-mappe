import pygame
from figur import Figur


class Platform (Figur):
    def __init__(self, x, y, width) -> None:
        super().__init__("bilder/fiende-hvit.png", x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = 20
        self.ramme = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def draw(self, vindu):
        pygame.draw.rect(vindu, (160, 20, 140), self.ramme, border_radius=10)
       