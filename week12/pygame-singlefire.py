import pygame
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
target = pygame.Rect(300,250,50,60)

running = True
while running:
    pygame.draw.rect(screen, (255, 0, 0), target)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("'a' was pressed")
            elif event.key == pygame.K_ESCAPE:
                running = False
            else:
                print("Something other than 'a' was pressed, it has the value of", event.key)
        elif event.type == pygame.KEYUP:
            print("Key has been released")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if target.collidepoint(event.pos):
                print("Clicked inside target")
            else:
                print("Clicked outside target")

        elif event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button has been released")

    pygame.display.update()


pygame.quit()