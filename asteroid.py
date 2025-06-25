import constants
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid = [Asteroid(self.position.x, self.position.y, new_radius),
                        Asteroid(self.position.x, self.position.y, new_radius)]

        new_asteroid[0].velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid[1].velocity = self.velocity.rotate(-random_angle) * 1.2