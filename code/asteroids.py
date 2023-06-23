import pygame as pg

class Asteroids(pg.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pg.image.load('../graphics/asteroids/asteroid1.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)

		self.speed = 3

	def update(self):
		self.rect.y += self.speed