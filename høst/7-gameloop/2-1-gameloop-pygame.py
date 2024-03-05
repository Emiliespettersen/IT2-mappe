import pygame
import random

# Gamelook-mønsteret

# 1. oppsett
pygame.init()

BREDDE = 1000
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode ((BREDDE, HOYDE))
klokke = pygame.time.Clock ()
stor_font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)

dino_x = 300
dino_y = 300
dino_bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha()

sirkel1_x = 400
sirkel1_y = 300
sirkel1_farge = "green"

sirkel2_x = 500
sirkel2_y = 400
sirkel2_farge = "green"



while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster [pygame.K_RIGHT]:
        print ("pil høyre")
        dino_x += 5
    if taster [pygame.K_LEFT]:
        print ("pil venstre")
        dino_x -= 5
    if taster [pygame.K_UP]:
        print("pil opp")
        dino_y -= 5
    if taster [pygame.K_DOWN]:
        print ("pil ned")
        dino_y += 5

    if taster [pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit
    
   
    


    # 3. Oppdater spill
    dino_rektangel = pygame.Rect (dino_x , dino_y, 100, 100)
    sirkel1_rektangel = pygame.Rect(sirkel1_x, sirkel1_y, 80, 80)
    sirkel2_rektangel = pygame.Rect(sirkel2_x, sirkel2_y, 80, 80)

    if dino_rektangel.colliderect(sirkel1_rektangel):
        print("over sikel 1")
        sirkel1_farge = "red"
        sirkel1_x = random.randint (0, BREDDE)
        sirkel1_y = random.randint (0, HOYDE)
    
    if dino_rektangel.colliderect(sirkel2_rektangel):
        print("over sikel 2")
        sirkel2_farge = "red"
        sirkel2_x = random.randint (0, BREDDE)
        sirkel2_y = random.randint (0, HOYDE)

    # 4. Tegn (print)
    vindu.fill ("gray")


    pygame.draw.circle (vindu, sirkel1_farge, (sirkel1_x, sirkel1_y), 40)
    pygame.draw.circle (vindu, sirkel2_farge, (sirkel2_x, sirkel2_y), 40)


    tekst_dino = stor_font.render ("DINO", True, "black")
    vindu.blit(tekst_dino, (400, 20))
    vindu.blit(dino_bilde1, (dino_x, dino_y))


    print("En rudne i gameloop")
    pygame.display.flip()
    klokke.tick(FPS)
   