import pygame
#1. oppsett
pygame.init()
BREDDE = 500
HOYDE = 500
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

while True:
    #2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    #3. Oppdater soill
    #4. tegn

    pygame.display.flip()
    klokke.tick(FPS)


    def kalkuler(tall):
        tall = tall + 1
        return tall * 2
    
    print(kalkuler(2)+kalkuler(4))
    