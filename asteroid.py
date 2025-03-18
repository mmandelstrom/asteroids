from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:#smallest asteroids do not spawn additional asteroids when destroyed
            return
        else:
            angle = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(angle)
            vel_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast_1 = Asteroid(self.position[0], self.position[1], new_radius)
            ast_2 = Asteroid(self.position[0], self.position[1], new_radius)

            ast_1.velocity = vel_1 * 1.2
            ast_2.velocity = vel_2 * 1.2

            
