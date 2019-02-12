import pygame
import math

class Spaceship:
	def __init__(self, screen):
		self.size = 30

		self.image = pygame.image.load("assets/spaceship.png")

		self.x = screen.get_width() / 2 - self.size / 2
		self.y = screen.get_height() / 2 - self.size / 2
		self.dx = 0
		self.dy = 0
		self.ddx = 0
		self.ddy = 0

		self.maxDx = 3
		self.maxDy = 3

		self.angle = 0

		self.turningRight = False
		self.turningLeft = False

		self.screen = screen

		self.acceleratingForwards = False
		self.acceleratingBackwards = False

	def render(self, screen):
		screen.blit(pygame.transform.rotozoom(self.image, self.angle, self.size / 512), (self.x, self.y))

	def update(self):
		self.x += self.dx
		self.y += self.dy

		self.dx += self.ddx
		self.dy += self.ddy

		if self.dx > self.maxDx: 
			self.dx = self.maxDx
		elif self.dx < -self.maxDx:
			self.dx = -self.maxDx

		if self.dy > self.maxDy:
			self.dy = self.maxDy
		elif self.dy < -self.maxDy:
			self.dy = -self.maxDy

		if self.x + self.size < 0: self.x = self.screen.get_width()
		if self.x > self.screen.get_width(): self.x = 0

		if self.y + self.size < 0: self.y = self.screen.get_height()
		if self.y > self.screen.get_height(): self.y = 0

		if self.turningRight:
			self.angle -= 5

		if self.turningLeft:
			self.angle += 5

		if self.acceleratingForwards:
			#self.ddx -= 0.1 * math.sin(math.radians(self.angle))
			#self.ddy -= 0.1 * math.cos(math.radians(self.angle))
			self.dx -= math.sin(math.radians(self.angle))
			self.dy -= math.cos(math.radians(self.angle))
		elif self.acceleratingBackwards:
			#self.ddx += 0.1 * math.sin(math.radians(self.angle))
			#self.ddy += 0.1 * math.cos(math.radians(self.angle))
			self.dx -= math.sin(math.radians(self.angle))
			self.dy -= math.cos(math.radians(self.angle))
		else:
			#self.ddx = 0
			#self.ddy = 0
			self.dx = 0
			self.dy = 0

	def turnRight(self):
		self.turningRight = True

	def turnLeft(self):
		self.turningLeft = True

	def stopTurning(self):
		self.turningRight = False
		self.turningLeft = False

	def accelerateForwards(self):
		self.acceleratingForwards = True

	def accelerateBackwards(self):
		self.acceleratingBackwards = True

	def stopAccelerating(self):
		self.acceleratingForwards = False
		self.acceleratingBackwards = False
