import pygame
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300,250,50,60)
playerspeed = 3

running = True
while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player.move_ip(0, -playerspeed)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, playerspeed)
    elif key[pygame.K_LEFT]:
        player.move_ip(-playerspeed, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(playerspeed, 0)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    time.sleep(.01)

pygame.quit()