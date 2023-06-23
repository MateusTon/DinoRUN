import pygame as pg

class Player(pg.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		# Dando load numa imagem para uma variavel
		self.sprite_sheet = pg.image.load('../graphics/dinospritesheet.png').convert_alpha()
		self.image = self.get_images(0, self.sprite_sheet, 24, 24, 4, (0, 0, 0))
		self.rect = self.image.get_rect(midbottom = pos)
		
		self.speed = 5

	def get_inputs(self):
		keys = pg.key.get_pressed()
		
		if keys[pg.K_RIGHT]:
			self.rect.x += self.speed
			self.is_idle = False

		if keys[pg.K_LEFT]:
			self.rect.x -= self.speed
			self.is_idle = False

	def get_images(self, frame, sheet, width, height, scale, color):
		image = pg.Surface((width, height)).convert_alpha()	# Cria uma Surface em branco 
		image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, width, height))# Cola o sprite que quero nessa Surface
		image = pg.transform.scale(image, (width * scale, height * scale))# Aumenta a scala da imagem
		image.set_colorkey(color) # Retira todos os pixels pretos em volta do sprite

		return image


	def update(self):
			self.get_inputs()
