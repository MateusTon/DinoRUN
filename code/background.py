import pygame as pg

class Background(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load('../graphics/background.png').convert_alpha()
		self.rect = self.image.get_rect()
