import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
import sys

from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")    
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
