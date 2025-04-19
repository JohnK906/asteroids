from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call the parent constructor
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        Asteroid.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2

        return asteroid1, asteroid2
