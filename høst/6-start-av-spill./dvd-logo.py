import pygame
import random

def tilfeldig_farge():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r , g , b]


#1. opsett (init)
pygame.init()                               #starter opp pygame
BREDDE = 1200
HOYDE = 600
vindu = pygame.display.set_mode ([BREDDE, HOYDE])
klokke = pygame.time.Clock() #oppretter en klokke som brukes for å begrense spillet til 60FPS

x = 20
y = 50
radius = 50
farge = tilfeldig_farge() #eks: [100 , 150 , 200]
x_fart = 1
y_fart = 1

spiller = True

while spiller: #når spiller er true

    #2. Håndter input/hendelser             #game loop
    hendelser = pygame.event.get()      #lager en liste med ale hendelsene
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            spiller = False
    if hendelser:
        print(hendelser)

    #3. oppdater spill
    x += x_fart
    y += y_fart

    if x > BREDDE or x < 0:
        #treffer vegg på høyre side eller venstre side
        x_fart = x_fart * -1
        farge = tilfeldig_farge()

    if y > HOYDE or y < 0:
        #treffer vegg på bunnen eller toppen
        y_fart = y_fart * -1
        farge = tilfeldig_farge()

    #4. Tegn (render)
    vindu.fill((20,0,255))
    pygame.draw.circle(vindu, farge, [x, y], radius) #vindu er hvor den skal tegne. første []er fargen til sirkelen. den andre er plasering. den tredje er radiusen på sirkelen
    pygame.draw.circle(vindu, [150,30,255], [200, 200], radius) #for å få flere baller
    pygame.display.update()
    klokke.tick(60) #forteller at løkken/spillet skal kjøre 60 ganger i sekundet (60 FPS)


    pass #middletidig
