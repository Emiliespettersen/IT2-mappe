import pygame
import random
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
bakgrunnsbilde = pygame.image.load("bilder/space.jpeg") #sette bakgunnen 
bakgrunnsbilde = pygame.transform.scale(bakgrunnsbilde, (BREDDE, HOYDE)) 
hjerte = pygame.image.load("bilder/hjerte.jpeg").convert_alpha() #convert alpha betyr tar vekk det hvite i bilde.brukes vanligvis på en overflate (surface) i Pygame for å konvertere et bilde til et format som støtter gjennomsiktighet, noe som gjør det enklere å håndtere gjennomsiktige bilder i spill og andre multimedia-applikasjoner.
hjerte = pygame.transform.scale_by(hjerte, 0.1) # .scale_by minimerer hjertet

spiller = Spiller(BREDDE, HOYDE)

#legger til pengene som jeg skal samle
def legg_til_penge(penger):
    r_int = random.randint(0, len(platformer)-1) #int velger en av de platformene
    r_left = random.randint(0, platformer[r_int].ramme.width - 20) #hvor til venstre mynten ligger
    temp_rect = pygame.rect.Rect(r_left + platformer[r_int].ramme.left, platformer[r_int].ramme.top - 25, 20, 20) #tilferdig verdi for 
    penger.append(temp_rect) #append betyr legg til

fiender = [ 
    Fiende(70, 75),
    Fiende(250, 75),
    Fiende(400, 75),
    Fiende(575, 75)
]

platformer = [
    Platform (50, 290, 150),
    Platform (150, 350, 150),
    Platform (200, 440, 150),
    Platform (500, 440, 150),
    Platform (450, 510, 150),
    Platform (70, 520, 150),
    Platform (300, 550, 150)

]

skuddene = []
penger = []

#poengsum
poengsum_font = pygame.font.SysFont("Arial", 32)
poeng = 0

for i in range(5):
    legg_til_penge(penger)

cooldown = 0

while True:
    print(len(penger))
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
        spiller.hopp(platformer)
    if taster[pygame.K_SPACE]:
        if spiller.cooldown == 0:
            skuddene.append(Skudd(spiller.ramme.centerx, spiller.ramme.centery)) # legger til i tom liste. Henter fra klassen Skudd
            spiller.cooldown = 20
        
    # 3. Oppdater spill
    spiller.oppdater(platformer)

    for fiende in fiender:
        fiende.update()
        if fiende.cooldown == 0:
            skuddene.append(Skudd(fiende.ramme.centerx, fiende.ramme.bottom, True)) #gor verdier på når den skal starte
            fiende.cooldown = 200

    for i in range (len(fiender)-1, -1, -1): #indexen til fiende. går gjennom listen baklengs
        fiender[i].flytt(BREDDE) # flyy funksjonen
        for skudd in skuddene:
            if skudd.ramme.colliderect(fiender[i].ramme) and skudd.fiende == False: #hvis den ikke kolliderer så..
                fiender.pop(i) # fjerner den
                poeng += 1 # plusser på poeng når jeg dreper de andre
                break
            if skudd.ramme.colliderect(spiller.ramme) and skudd.fiende == True: #hvis den kolliderer så:
                skuddene.remove(skudd) #fjerner skuddene
                # HER MÅ DU MISTE LIV
                spiller.liv -= 1 
                if spiller.liv <= 0: # 
                    print("dø.")
                    pygame.quit()
                    raise SystemExit
    
    # SJEKKER OM DU TREFFER EN PENGE
    for penge in penger: 
        if spiller.ramme.colliderect(penge):
            spiller.penger += 1 #hvis den kolliderer så kommer det en ny
            penger.remove(penge)
            cooldown = 60
    
    for skudd in skuddene:
        skudd.flytt()

    if cooldown <= 0 and len(penger) < 5:
        legg_til_penge(penger)
        cooldown = 60
    cooldown -= 1


    #4. tegn
    vindu.blit(bakgrunnsbilde, (0, 0))

    for fiende in fiender:
        fiende.tegn(vindu)
    
    for platform in platformer:
        platform.draw(vindu)

    for skudd in skuddene:
        skudd.tegn(vindu)

    for penge in penger:
        pygame.draw.rect(vindu, (0,0,0), (penge.left-2, penge.top-2, penge.width + 4, penge.width + 4), border_radius=100)
        pygame.draw.rect(vindu, (255,255,0), penge, border_radius = 100)
    
    spiller.tegn(vindu)
    vindu.blit(poengsum_font.render(f"Poeng{poeng}", True, "white"), (0,0))
    for i in range(spiller.liv):
        vindu.blit(hjerte, ((i) * 50, 30)) #tegne


    pygame.display.flip()
    klokke.tick(FPS)


