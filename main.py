import sys
import pygame
from asteroidfield import *
from constants import *
from player import Player
def main():
	print("Starting Asteroids!")
	pygame.init()

	print("Screen width: 1280")
	print("Screen height: 720")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(640, 360)
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids,updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	shots = pygame.sprite.Group()

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        		     return
		new_shot = player.update(dt)
		if new_shot:
			shots.add(new_shot)
		for shot in shots:
			shot.update(dt)
		screen.fill((0,0,0))
		updatable.update(dt)
		for entity in drawable:
			entity.draw(screen)
		for asteroid in asteroids:
    			if player.check_collision(asteroid):
                                print("Game over!")
                                sys.exit()
		for shot in shots:
			shot.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		for asteroid in asteroids:
			for shot in shots:
				if shot.check_collision(asteroid):
					asteroid.split()
					shot.kill()

if __name__ == "__main__":
    main()
