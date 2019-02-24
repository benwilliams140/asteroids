import pygame
import time
import sys
import random

from Spaceship import Spaceship
from Asteroid import Asteroid

class Main:
	def __init__(self):
		pygame.init()

		self.width = 800
		self.height = 800
		self.screen = pygame.display.set_mode((self.width, self.height))

		self.lives = 3
		self.gameState = "PLAYING"

		self.running = False

		self.delta = 0
		self.currentTime = 0
		self.previousTime = 0
		self.fps = 30

		self.spaceship = Spaceship(self.screen)

		self.minAsteroids = 8
		self.maxAsteroids = 10
		self.asteroids = []

		self.startTime = time.time()

	def main(self):
		self.running = True

		while(self.running):
			self.getInput()
			self.update()
			self.render()
			if self.delta > 0:
				time.sleep(self.delta)

		pygame.quit()
		sys.exit()

	def getInput(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					self.spaceship.turnLeft()
				if event.key == pygame.K_d:
					self.spaceship.turnRight()
				if event.key == pygame.K_w:
					self.spaceship.accelerateForwards()
				if event.key == pygame.K_SPACE:
					self.spaceship.createBullet()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d:
					self.spaceship.stopTurning()
				if event.key == pygame.K_w:
					self.spaceship.stopAccelerating()


		#self.spaceship.getInput()

	def render(self):
		self.screen.fill((0, 0, 0))

		if self.gameState == "MENU":
			print("menu")
		elif self.gameState == "PLAYING":
			self.spaceship.render()
			for asteroid in self.asteroids:
				asteroid.render(self.screen)

		pygame.display.update()

	def update(self):
		self.currentTime = time.time()
		self.delta = 1 / self.fps - (self.currentTime - self.previousTime)
		self.previousTime = self.currentTime

		if self.gameState == "MENU":
			print("menu")
		elif self.gameState == "PLAYING":
			self.spaceship.update()
			if (time.time() - self.startTime) > 10:
				self.startTime = time.time()
				self.maxAsteroids += 1

			if len(self.asteroids) < self.minAsteroids:
				self.asteroids.append(Asteroid(self.screen))
			elif len(self.asteroids) < self.maxAsteroids:
				if random.randint(0, 1) == 0:
					self.asteroids.append(Asteroid(self.screen))

			for asteroid in self.asteroids:
				asteroid.update()
				if asteroid.isOffScreen():
					self.asteroids.remove(asteroid)

if __name__ == "__main__":
	main = Main()
	main.main()