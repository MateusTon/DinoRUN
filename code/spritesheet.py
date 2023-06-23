import pygame as pg

class SpriteSheet(pg.sprite.Sprite):
	def __init__(self, image):
		self.sheet = image


	def get_images(self, frame, sheet, width, height, scale, color):
		image = pg.Surface((width, height)).convert_alpha()	# Cria uma Surface em branco 
		image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, width, height))# Cola o sprite que quero nessa Surface
		image = pg.transform.scale(self.image, (width * scale, height * scale))# Aumenta a scala da imagem
		image.set_colorkey(color) # Retira todos os pixels pretos em volta do sprite

		return image