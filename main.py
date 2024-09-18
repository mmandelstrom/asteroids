import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
from fragments import Fragment
from textoutput import scoreboard, end_screen


def main():
    pygame.init()
    pygame.font.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    my_font = pygame.font.SysFont('Arial', 30)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    life = 5

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    text = pygame.sprite.Group()
    fragments_group = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    Fragment.containers = (asteroids, updatable, drawable)

   
    


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        
            
        for obj in updatable:
            obj.update(dt)

        fragments_group.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player) and life > 0:
                life -= 1
                player.reset_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                

            elif asteroid.collision(player) and life <= 0:
                pass

            

            for shot in shots:
                if asteroid.collision(shot):
                 
                    asteroid.split(fragments_group)
                    shot.kill()
                    score += 1


        if life < 1:
            end_screen(screen, score, my_font)
                                      

        scoreboard(screen, score, my_font, life)


        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()