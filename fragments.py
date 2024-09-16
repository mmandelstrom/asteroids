import pygame
import random
from circleshape import CircleShape
from constants import *


class Fragment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.lifespan = 500
        self.spawn_time = pygame.time.get_ticks()
        self.start_pos = pygame.Vector2(self.position.x, self.position.y)
        self.end_pos = pygame.Vector2(self.position.x + 2, self.position.y + 2)
    


    def draw(self, screen):
        pygame.draw.line(screen, "white", self.start_pos, self.end_pos)

    def update(self, dt):
        self.position += self.velocity * dt
        self.start_pos = self.position
        self.end_pos = self.position + pygame.Vector2(1, 1)

        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.lifespan:
            self.kill()

    def explode(self, fragments_group):
            angle = 0
            for i in range(8):
                fragment = Fragment(self.position.x, self.position.y)
                angle += 45
                fragment.velocity = pygame.Vector2(1, 0).rotate(angle) * 50
                fragment.add(fragments_group)
            

    def collision(self, obj):
        pass