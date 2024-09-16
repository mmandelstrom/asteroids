import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
from fragments import Fragment


def main():
    pygame.init()
    pygame.font.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

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

    my_font = pygame.font.SysFont('freesansbold.ttf', 30)
    
    







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
                print(f"Game over! Your score was {score}")
                exit()
           
            

            for shot in shots:
                if asteroid.collision(shot):
                    if asteroid.__class__ == Fragment:
                        return
                    asteroid.split(fragments_group)
                    shot.kill()
                    score += 1
                                      

        score_text_surface = my_font.render(f'Score: {score}', False, (255, 255, 255))
        life_text_surface = my_font.render(f'Lives: {life}', False, (255, 255, 255))
        screen.blit(score_text_surface, (1180,10))
        screen.blit(life_text_surface, (1180,30))

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()