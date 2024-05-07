from spillobjekt import Spillobjekt
from menneske import Menneske
from sau import Sau
import pygame

class Spillebrett:
    def __init__(self, bredde, hoyde) -> None:
        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objerkter: list[Spillobjekt] = []

        #alle "ting" i pygame må ha en surface og en rect. Rect er den som ligger rundt og surface er
        self.surface = pygame.Surface( (self.bredde, self.hoyde) )
        self.rect = self.surface.get_rect()

        #plassering på spillebrettet i (x, y)
        self.rect.topleft = (0 , 0)
        #fargen på bakgrunnen
        self.surface.fill ("white")

        # oppretter et menneske
        self.spiller1 = Menneske()

        #oppretter sauer
        # self.sau1 = Sau()
        # self.sau2 = Sau()
        # self.sau3 = Sau()

        self.sauer: list[Sau] = []
        for i in range (3):
            self.sauer.append(Sau())

    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        #legger til nytt objekt i listen self.objekter
        self.objerkter.append(nytt_objekt)

    def fjern_objekt(self, objekt: Spillobjekt):
        self.objerkter.remove(objekt) #fjerner et objekt


    def tegn (self, vindu: pygame.Surface):
        self.spiller1.tegn(self.surface)

        # self.sau1.tegn(self.surface)
        # self.sau2.tegn(self.surface)
        # self.sau3.tegn(self.surface)

        for sau in self.sauer:
            sau.tegn (self.surface)
        
        # tegner spillbrettets surface i posisjonen til spillebrettets rect på vinduet
        vindu.blit(self.surface, self.rect) 