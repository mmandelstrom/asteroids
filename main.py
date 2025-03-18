# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #Static values for screen size/asteroids size and speed
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)#Add all future player objects to updatable/drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y)#Create player object
    asteroidfield = AsteroidField() #Create asteroidfield object
    dt = 0#Initialize dt variable

    while True:#Endless gameloop
        for event in pygame.event.get():#Create button to close window
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:#Collision check, if player object collides with asteroid exit game
            if obj.collision_check(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen) #Draw player each iteration

        pygame.display.flip()#Refresh screen, should be called last in loop

        dt = clock.tick(60) / 1000 #Pauses game for 1/60th of a second, sets dt to amount of time since it was last called in milliseconds
        

if __name__ == "__main__":
    main()