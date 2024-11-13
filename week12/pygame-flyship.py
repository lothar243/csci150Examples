import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ship_position = {"x_pos": 100.0, "y_pos": 100.0, "x_velocity": 0.0, "y_velocity": 0.0, "direction": 0}
clock = pygame.time.Clock()

def moveShip(ship_position):
    # move the ship based on its current speed, also keep the ship x between 0 and 800, the ship y between 0 and 600
    ship_position["x_pos"] = (ship_position["x_pos"] + ship_position["x_velocity"]) % 800
    ship_position["y_pos"] = (ship_position["y_pos"] + ship_position["y_velocity"]) % 600
    # apply some drag to slow the ship down over time
    ship_position["x_velocity"] = ship_position["x_velocity"] * .99
    ship_position["y_velocity"] = ship_position["y_velocity"] * .99

def drawShip(screen, ship_position):
    pygame.draw.arc(
        screen, color=(100, 100, 100), 
        rect=(ship_position["x_pos"] + 3, ship_position["y_pos"] - 10, 50, 50), 
        start_angle=-.4+3.14 + ship_position["direction"], 
        stop_angle=.4+3.14 + ship_position["direction"], 
        width=50
    )

running = True
while running:
    screen.fill((255,255,255))    # fill the screen with white
    moveShip(ship_position)
    drawShip(screen, ship_position)

    #handle key press events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()
    if(keys_pressed[pygame.K_UP]):
        ship_position["x_velocity"] += .1 * math.cos(ship_position["direction"])
        ship_position["y_velocity"] += .1 * math.sin(-ship_position["direction"])
    if(keys_pressed[pygame.K_DOWN]):
        ship_position["x_velocity"] -= .05 * math.cos(ship_position["direction"])
        ship_position["y_velocity"] -= .05 * math.sin(-ship_position["direction"])
    if(keys_pressed[pygame.K_LEFT]):
        ship_position["direction"] += .05
    if(keys_pressed[pygame.K_RIGHT]):
        ship_position["direction"] -= .05
                
    clock.tick(60)
    pygame.display.flip()

pygame.quit()