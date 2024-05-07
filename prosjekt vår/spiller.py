from figur import Figur
import pygame

class Spiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/spiller.png", vindu_bredde / 2, vindu_høyde)

        #setter spilleren i startposisjonen
        self.ramme.bottom = vindu_høyde
        self.cooldown = 20
        self.liv = 3
        self.aks = 0.7
        self.fart_y = 0
        self.penger = 0

    
    def flytt(self, dx:int):
        self.ramme.x += 3 * dx

    def står(self, blokker):
        for blokk in blokker:
            if pygame.rect.Rect(self.ramme.centerx - 10, self.ramme.bottom - 10, 20, 10).colliderect(blokk.ramme) and self.fart_y > -1:
                self.ramme.bottom = blokk.ramme.top + 5
                self.fart_y = 0
                return True
        if self.ramme.bottom >= 595 and self.fart_y > -1:
            self.ramme.bottom = 600
            self.fart_y = 0
            return True
        return False
    
    def hopp(self, blokker):
        if self.står(blokker):
            self.fart_y = -10

    def oppdater(self, blokker):
        self.ramme.centery += self.fart_y
        if self.ramme.bottom > 600:
            self.ramme.bottom = 600
        if self.står(blokker) == False:
            self.fart_y += self.aks
        if self.cooldown > 0:
            self.cooldown -= 1
