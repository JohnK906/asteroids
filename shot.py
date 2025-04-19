import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Call the parent constructor


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
