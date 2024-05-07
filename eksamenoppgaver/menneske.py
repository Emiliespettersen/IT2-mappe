from spillobjekt import Spillobjekt

class Menneske(Spillobjekt):
    def __init__(self) -> None:
        super().__init__("green")
        self.fart_x: int = 0
        self.fart_y: int = 0
        self.poeng: int = 0
        self.baerer_sau: bool = False #hva er bool?
        self.plassering (75, 300)


    def beveg (self, dx: int, dy: int):
        if self.baerer_sau:
            self.flytt(self.fart_x * 0.8, self.fart_y)
        else:
            self.flytt(self.fart_x, self.fart_y)

    