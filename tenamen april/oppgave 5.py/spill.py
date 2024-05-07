
import pygame
import random

# Initialiserer pygame
pygame.init()

# Definerer skjermstørrelsen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Definerer farger
GRONN = (0, 200, 0)
SVART = (0, 0, 0)
ROD = (200, 0, 0)
HVIT = (255, 255, 255)

# Definerer spiller- og ballvariabler
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 100
PLAYER_SPEED = 5
BALL_WIDTH, BALL_HEIGHT = 15, 15
HINDRING_WIDTH, HINDRING_HEIGHT = 60, 60
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Definerer spillervariabler
player1_score = 0
player2_score = 0

# Lager spillere, ball og hindringer
player1 = pygame.Rect(50, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_WIDTH//2, HEIGHT//2 - BALL_HEIGHT//2, BALL_WIDTH, BALL_HEIGHT)
hindring_1 = pygame.Rect(WIDTH//2 , HEIGHT//3 ,HINDRING_WIDTH, HINDRING_HEIGHT)
hindring_2 = pygame.Rect(WIDTH//2 , HEIGHT//5 ,HINDRING_WIDTH, HINDRING_HEIGHT)
hindring_3 = pygame.Rect(WIDTH//2 , HEIGHT//2 ,HINDRING_WIDTH, HINDRING_HEIGHT)



#  pygame.Rect(WIDTH//2 - HINDRING_WIDTH//2, HEIGHT//2 - HINDRING_HEIGHT//2,HINDRING_WIDTH, HINDRING_HEIGHT)

# Funksjon for å tegne objekter
def draw_objects():
    WIN.fill(SVART)
    pygame.draw.rect(WIN, GRONN, player1)
    pygame.draw.rect(WIN, GRONN, player2)
    pygame.draw.ellipse(WIN, GRONN, ball)
    pygame.draw.rect(WIN, ROD, hindring_1)
    pygame.draw.rect(WIN, ROD, hindring_2)
    pygame.draw.rect(WIN, ROD, hindring_3)


    # Tegner poengene på skjermen
    font = pygame.font.Font(None, 20)
    player1_text = font.render("Første spiller sine poeng: " + str(player1_score), True, HVIT)
    player2_text = font.render("Andre spiller sine poeng: " + str(player2_score), True, HVIT)
    WIN.blit(player1_text, (10, 10))
    WIN.blit(player2_text, (WIDTH - player2_text.get_width() - 10, 10))

# Funksjon for å oppdatere ballens posisjon
def move_ball():
    global BALL_SPEED_X, BALL_SPEED_Y, player1_score, player2_score

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Sjekker kollisjon med vegger
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Sjekker kollisjon med spillere
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED_X *= -1
    
    if ball.colliderect(hindring_1) or ball.colliderect(hindring_2) or ball.colliderect(hindring_2):
       BALL_SPEED_X *= -1

    # Sjekker om ballen gikk ut av skjermen
    if ball.left <= 0:
        player2_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        player1_score += 1
        reset_ball()

# Funksjon for å restarte ballens posisjon
def reset_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (WIDTH//2, HEIGHT//2)
    BALL_SPEED_X *= random.choice((1, -1))
    BALL_SPEED_Y *= random.choice((1, -1))

# Funksjon for å oppdatere spillernes posisjon
def move_players(keys_pressed):
    if keys_pressed[pygame.K_w] and player1.top > 0:
        player1.y -= PLAYER_SPEED
    if keys_pressed[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PLAYER_SPEED
    if keys_pressed[pygame.K_UP] and player2.top > 0:
        player2.y -= PLAYER_SPEED
    if keys_pressed[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PLAYER_SPEED

# Hovedspill-løkke
def main():
    global player1_score, player2_score

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        # Håndterer events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Beveger spillere
        keys_pressed = pygame.key.get_pressed()
        move_players(keys_pressed)

        # Beveger ballen
        move_ball()

        # Tegner objekter
        draw_objects()

        # Oppdaterer skjermen
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



"""
For å oppnå krav 3 så ville jeg:

1. When ball collide med spiller_ 1 eller spiller_2, så add ny ball.
2. For å få samme posisjon bruker jeg bare samme som jeg har brukt for den første ballen
3. 
4. Ball <= 5 for å få det til å være mindre enn 5 baller
5. When poeng + 1 , så skal ballen forsvinne.
6. when ballen treffer høyre eller venstre side av 
skjermen så adder vi er ny ball.

"""