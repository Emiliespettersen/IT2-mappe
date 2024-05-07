from spillebrett import Spillobjekt
import random

class Sau (Spillobjekt):
    def __init__(self) -> None:
        super().__init__("gray")
        self.blir_loftet: bool = False

        tilfeldig_y = random.randint (50, 550) #bvariabler uten self. "glemmes" når init-metoden er ferdig
        tilfeldig_x = random.randint (450, 550) #bvariabler uten self. "glemmes" når init-metoden er ferdig
        self.plassering (tilfeldig_x, tilfeldig_y)

        
      


  