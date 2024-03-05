import pygame

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



while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    if taster [pygame.K_RIGHT]:
        print ("pil høyre")
        dino_x += 1
    if taster [pygame.K_LEFT]:
        print ("pil venstre")
        dino_x -= 1
    if taster [pygame.K_UP]:
        print("pil opp")
        dino_y -= 1
    if taster [pygame.K_DOWN]:
        print ("pil ned")
        dino_y += 1

    if taster [pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit
    
   
    


    # 3. Oppdater spill
    # 4. Tegn (print)
    vindu.fill ("gray")
    pygame.draw.rect(vindu, "black", (200 , 100, 50 , 100))


    #oppgave: bruk juksearket og lag det danske flagget

    
    vindu.fill ((200, 100, 50))
    pygame.draw.rect(vindu, "red", (200, 250, 70, 90))
    pygame.draw.rect(vindu, "red", (300, 250, 70, 90))
    pygame.draw.rect(vindu, "red", (300, 370, 70, 90))
    pygame.draw.rect(vindu, "red", (200, 370, 70, 90))
    pygame.draw.rect(vindu, "white", (270, 250, 30, 210))
    pygame.draw.rect(vindu, "white", (200, 340, 170, 30))

    tekst_lykke_til = stor_font.render ("Lykketil!", True, "black")
    vindu.blit(tekst_lykke_til, (400, 20))

    vindu.blit(dino_bilde1, (dino_x, dino_y))


    print("En rudne i gameloop")
    pygame.display.flip()
    klokke.tick(FPS)
   