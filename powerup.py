import pygame
import random
from circleshape import CircleShape
from constants import *
from fragments import Fragment


class Powerup(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt


    def collision(self, obj):
        return self.position.distance_to(obj.position) <= self.radius + obj.radius