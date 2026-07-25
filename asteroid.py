import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, color= "white", center= self.position, radius= self.radius, width= LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(angle * -1)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one = Asteroid(self.position.x, self.position.y, child_radius)
        child_two = Asteroid(self.position.x, self.position.y, child_radius)
        child_one.velocity = vector_1 * 1.2
        child_two.velocity = vector_2 * 1.2
