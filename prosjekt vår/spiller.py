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

    def står(self, blokker): # Funksjon for å sjekke om spiller står på blokkene (plattformene)
        # Sender med listen til plattformene som blokker
        for blokk in blokker:
            """
                Lager en ny Rect som kun er en liten del av hele bildet,
                dette er ford man kun vil stå dersom bunnen treffer plattformene
                Sjekker deretter om denne rammen treffer rammen til blokken
                Sjekker også om spiller beveger seg nedover.
            """
            if pygame.rect.Rect(self.ramme.centerx - 10, self.ramme.bottom - 10, 20, 10).colliderect(blokk.ramme) and self.fart_y > -1:
                # Hvis alt stemmer, så:
                self.ramme.bottom = blokk.ramme.top + 5  # Setter bunnen til spilleren 5px under toppen av plattformen
                self.fart_y = 0 # Setter farten til spilleren lik 0
                return True # Returnerer True, som gjør at det står om spiller står eller ikke
        if self.ramme.bottom >= 595 and self.fart_y > -1: # Sjekker om spiller er på bunnen av skjermen
            # GJØR SAMME SOM if SETNNGEN OVER, BARE PÅ BAKKEN
            self.ramme.bottom = 600
            self.fart_y = 0
            return True
        # Returnerer False dersom spiller ikke står
        return False
    
    def hopp(self, blokker): # Sender inn blokker for å kjøre står funksjonen
        if self.står(blokker): # Dersom spiller(self) står 
            self.fart_y = -10 # Farten til et hopp 

    def oppdater(self, blokker):
        self.ramme.centery += self.fart_y # Endrer posisjonen til spilleren med farten
        if self.står(blokker) == False: # Endrer farten nedover dersom spilleren ikke står på blokkene
            self.fart_y += self.aks
        if self.cooldown > 0: # Endrer cooldownen nedover dersom cooldownen er over 0
            self.cooldown -= 1
