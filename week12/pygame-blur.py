import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300,250,50,60)

running = True
while running:
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()