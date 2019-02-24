import pygame
import math

class Bullet:
	def __init__(self, x, y, angle, size):
		self.x = x + size / 2
		self.y = y + size / 2

		self.dx = -5 * math.sin(math.radians(angle))
		self.dy = -5 * math.cos(math.radians(angle))

	def render(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

	def update(self):
		self.x += self.dx
		self.y += self.dy

	def getX(self):
		return self.x

	def getY(self):
		return self.y