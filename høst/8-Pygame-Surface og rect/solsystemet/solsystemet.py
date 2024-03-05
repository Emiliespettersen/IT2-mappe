import pygame
from planet import Planet

#1. oppsett
pygame.init()
BREDDE = 1000
HOYDE = 400 
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

planeter = [
    Planet (-200, 0, 200, "bilder/sun.png"),
    Planet (200, 200, 50, "bilder/mercury.png"),
    Planet(300, 200, 50, "bilder/venus.png"),
    Planet(400, 200, 50, "bilder/earth.png"),
    Planet (500, 200, 50, "bilder/mars.png"),
    Planet(600, 200, 50, "bilder/jupiter.png"),
    Planet(700, 200, 50, "bilder/saturn.png"),
    Planet(800, 200, 50, "bilder/uranus.png"),
    Planet (900, 200, 50, "bilder/neptune.png")
]




while True:
    #2. håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    #3. oppdater spill
    #. Tegn
    for p in planeter:
        p.tegn(vindu)



    pygame. display.flip()
    klokke.tick(FPS)

