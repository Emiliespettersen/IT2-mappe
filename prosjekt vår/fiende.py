from figur import Figur
import random

fiender_lis = []

class Fiende (Figur):
    def __init__(self, x, y) -> None:
        super().__init__("bilder/fiende-hvit.png", x, y)
        a = random.randint(1,2) #mellom 1 og 2
        if a == 1:
            self.fart_x = 1 #hvor fort de går fram og tilbake
        else:
            self.fart_x = -1 # hvor fort de går fram og tilbake
        self.cooldown = 200

    def flytt(self, bredde): 
        if self.ramme.left <= 0 or self.ramme.right >= bredde: #skjekker om noe av fienden er utenfor vinduet (bredden)
            self.fart_x = self.fart_x * -1 #endrer fartretningen
        self.ramme.centerx += self.fart_x #flytter
    
    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 0.5 #hvor fort skuddene kommer