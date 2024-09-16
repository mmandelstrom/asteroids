import pygame
import random
from circleshape import CircleShape
from constants import *
from fragments import Fragment


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, fragments_group):
        self.kill()
        


        if self.radius <= ASTEROID_MIN_RADIUS:
            Fragment.explode(self, fragments_group)
        
        angle = random.uniform(20, 50)
        first_split = pygame.math.Vector2.rotate(self.velocity, angle)
        second_split = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_split * 1.2
        second_asteroid.velocity = second_split * 1.2
        