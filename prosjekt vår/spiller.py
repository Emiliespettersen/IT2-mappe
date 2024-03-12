from figur import Figur

class Spiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/spiller.png", vindu_bredde / 2, vindu_høyde)

        #setter spilleren i startposisjonen
        self.ramme.bottom = vindu_høyde
        self.cooldown = 20
        self.liv = 3
    
    def flytt(self, dx:int):
        self.ramme.x += dx

    def oppdater(self):
        if self.cooldown > 0:
            self.cooldown -= 1
