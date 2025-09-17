import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        velocity_one = self.velocity.rotate(random_angle)
        velocity_two = self.velocity.rotate(-random_angle)

        new_raduis = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_raduis)
        new_asteroid.velocity = velocity_one * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_raduis)
        new_asteroid.velocity = velocity_two * 1.2
