from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

class Player(CircleShape): #Class that inherits from circleshape

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) #Draws player object in white 

    def rotate(self, dt):#Method to rotate player object
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):#Method to move player object back and forward
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt): #keybindings to call methods
        self.shoot_cooldown -= dt #Update shoot timer
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_cooldown > 0:#Only allow player to shoot every 0.3s
            return
        
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN