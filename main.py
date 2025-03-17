# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #Static values for screen size/asteroids size and speed

def main():
    pygame.init()#Initialize all pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#Create window 

    print("Starting Asteroids!") #Starting text
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:#Endless gameloop
        for event in pygame.event.get():#Create button to close window
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()#Refresh screen, should be called last in loop



if __name__ == "__main__":
    main()