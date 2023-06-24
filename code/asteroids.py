import pygame as pg
import random as rd

class Asteroids(pg.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pg.image.load('../graphics/asteroids/asteroid1.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		#self.create_new_asteroids()

		self.speed = 3

	'''
	def create_new_asteroids(self):
		asteroid2 = Asteroids((50, 0))
		self.asteroid_group = pg.sprite.Group()
		self.asteroid_group.add(asteroid)
	'''

	def update(self):
		self.rect.y += self.speed
