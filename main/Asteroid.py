import pygame
import random

class Asteroid:
	def __init__(self, screen):
		self.asteroids = []
		self.asteroids.append(pygame.image.load("assets/asteroid_1.png"))
		self.asteroids.append(pygame.image.load("assets/asteroid_2.png"))
		self.asteroids.append(pygame.image.load("assets/asteroid_3.png"))

		self.screen = screen

		self.id = random.randint(0, len(self.asteroids) - 1)
		self.angle = random.randint(0, 360)

		self.size = random.randint(40, 80)

		self.minDx = 1
		self.maxDx = 3
		self.minDy = 2
		self.maxDy = 4

		self.x, self.y = self.getXY()
		self.dx, self.dy = self.getDxDy()

	def render(self, screen):
		screen.blit(pygame.transform.rotozoom(self.asteroids[self.id], self.angle, self.size / 512), (self.x, self.y))

	def update(self):
		self.x += self.dx
		self.y += self.dy

	def getXY(self):
		number = random.randint(0, 3)
		x = 0
		y = 0
		if number == 0:
			x = -self.size
			y = random.randint(0, self.screen.get_height())
		elif number == 1:
			x = self.screen.get_width()
			y = random.randint(0, self.screen.get_height())
		elif number == 2:
			x = random.randint(0, self.screen.get_width())
			y = -self.size
		else:
			x = random.randint(0, self.screen.get_width())
			y = self.screen.get_height()
		return x, y

	def getDxDy(self):
		dx = 0
		dy = 0
		if self.x < self.screen.get_width() / 2:
			dx = random.randint(self.minDx, self.maxDx)
		else:
			dx = -random.randint(self.minDx, self.maxDx)

		if self.y < self.screen.get_height() / 2:
			dy = random.randint(self.minDy, self.maxDy)
		else:
			dy = -random.randint(self.minDy, self.maxDy)

		return dx, dy

	def isOffScreen(self):
		if self.x + self.size < 0:
			return True
		elif self.x > self.screen.get_width():
			return True
		elif self.y + self.size < 0:
			return True
		elif self.y > self.screen.get_height():
			return True

		return False
