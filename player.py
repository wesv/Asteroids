from circleshape import CircleShape
from shot import Shot
import constants
import pygame

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x,y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
            pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer <= 0:
                self.shoot()
                self.cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN



    def rotate(self, dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2((0,1)).rotate(self.rotation)
        shot.velocity *= constants.PLAYER_SHOOT_SPEED
