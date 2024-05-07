import pygame


class Spillobjekt:
    def __init__(self, farge: str) -> None:
        self.surface = pygame.Surface((50 , 50)) #lager et pygame Surface som er 50px bredt og 50 px hoyt
        self.rect = self.surface.get_rect() # lager en rect som ligger rundt surface-en
        self.surface.fill(farge)


    def plassering (self, x:int, y:int):
        self.rect.center = (x,y)


    def flytt (self, dx: int, dy: int):
        self.rect.move_ip (dx, dy) #flytter recten, bruk move_ip (move in place) istedet for move


    def tegn(self, surface: pygame.Surface):
        #tegner spillbrettes surface i posisjonen til spillerbretters rect på vindu
        surface.blit(self.surface, self.rect)
        