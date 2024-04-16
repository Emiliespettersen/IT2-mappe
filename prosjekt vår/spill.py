import pygame
from spiller import Spiller
from fiende import Fiende
from skudd import Skudd
from plattform import Platform

#1. oppsett
pygame.init()
BREDDE = 700
HOYDE = 600
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

bakgrunnsbilde = pygame.image.load("bilder/space.jpeg") 
bakgrunnsbilde = pygame.transform.scale(bakgrunnsbilde, (BREDDE, HOYDE))
hjerte = pygame.image.load("bilder/hjerte.jpeg").convert_alpha()
hjerte = pygame.transform.scale_by(hjerte, 0.1)

spiller = Spiller(BREDDE, HOYDE)

fiender = [ 
    Fiende(70, 75),
    Fiende(250, 75),
    Fiende(400, 75),
    Fiende(575, 75)
]

platformer = [
    Platform (50, 200, 150),
    Platform (150, 300, 150),
    Platform (300, 550, 150),
    Platform (400, 550, 150),
    Platform (400, 470, 150),
    Platform (450, 510, 150),
    Platform (500, 610, 150)

]

skuddene = []

#poengsum
poengsum_font = pygame.font.SysFont("Arial", 32)
poeng = 0

while True:
    poeng_surface = poengsum_font.render(f"poengsum:{poeng}", True, "white")
    #2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    #Dette er for de forskjellige tastene
    taster = pygame.key.get_pressed()
    if taster [pygame.K_LEFT]:
        spiller.flytt(-1)
    if taster[pygame.K_RIGHT]:
        spiller.flytt(1)
    if taster[pygame.K_UP]:
        spiller.hopp()
    if taster[pygame.K_SPACE]:
        if spiller.cooldown == 0:
            skuddene.append(Skudd(spiller.ramme.centerx, spiller.ramme.centery))
            spiller.cooldown = 20
        
    # 3. Oppdater spill
    spiller.oppdater()

    for fiende in fiender:
        fiende.update()
        if fiende.cooldown == 0:
            skuddene.append(Skudd(fiende.ramme.centerx, fiende.ramme.bottom, True))
            fiende.cooldown = 200

    for i in range (len(fiender)-1, -1, -1):
        fiender[i].flytt(BREDDE)
        for skudd in skuddene:
            if skudd.ramme.colliderect(fiender[i].ramme) and skudd.fiende == False:
                fiender.pop(i)
                poeng += 1
                break
            if skudd.ramme.colliderect(spiller.ramme) and skudd.fiende == True:
                skuddene.remove(skudd)
                # HER MÅ DU MISTE LIV
                spiller.liv -= 1
                if spiller.liv <= 0:
                    print("dø.")
                    pygame.quit()
                    raise SystemExit
    
    for skudd in skuddene:
        skudd.flytt()

    for platform in platformer:
        if spiller.ramme.colliderect(platform.rect) and platform.rect[1] + 5 > spiller.ramme.bottom:
            print("Standing")
            spiller.ramme.bottom = platform.ramme.top + 3

 
    #4. tegn
    vindu.blit(bakgrunnsbilde, (0, 0))

    for fiende in fiender:
        fiende.tegn(vindu)
    
    for platform in platformer:
        platform.draw(vindu)

    for skudd in skuddene:
        skudd.tegn(vindu)

    
    
    spiller.tegn(vindu)
    vindu.blit(poengsum_font.render(f"Poeng{poeng}", True, "white"), (0,0))
    for i in range(spiller.liv):
        vindu.blit(hjerte, ((i) * 50, 30))


    pygame.display.flip()
    klokke.tick(FPS)