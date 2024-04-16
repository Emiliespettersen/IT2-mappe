from figur import Figur

class Spiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/spiller.png", vindu_bredde / 2, vindu_høyde)

        #setter spilleren i startposisjonen
        self.ramme.bottom = vindu_høyde
        self.cooldown = 20
        self.liv = 3
        self.aks = 0.7
        self.fart_y = 0

    
    def flytt(self, dx:int):
        self.ramme.x += 3 * dx
    
    def hopp(self):
        if self.ramme.bottom > 595:
            self.fart_y = -10

    def oppdater(self):
        self.ramme.centery += self.fart_y
        if self.ramme.bottom > 600:
            self.ramme.bottom = 600
        self.fart_y += self.aks
        if self.cooldown > 0:
            self.cooldown -= 1
