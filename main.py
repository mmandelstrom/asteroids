# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #Static values for screen size/asteroids size and speed
from player import Player

clock = pygame.time.Clock()#Clock to track gametime
dt = 0 #Delta time variable

def main():
    pygame.init()#Initialize all pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#Create window 

    print("Starting Asteroids!") #Starting text
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2 #Static values to make player spawn in the middle of screen
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)#Create player object

    while True:#Endless gameloop
        for event in pygame.event.get():#Create button to close window
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen) #Draw player each iteration
        pygame.display.flip()#Refresh screen, should be called last in loop
        dt = clock.tick(60) / 1000 #Pauses game for 1/60th of a second, sets dt to amount of time since it was last called in milliseconds


if __name__ == "__main__":
    main()