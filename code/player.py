import pygame as pg
from suport import import_folder

class Player(pg.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.import_player_assets()
		# Player Image
		self.frame_index = 0
		self.animation_speed = 0.15
		self.image = self.animations['idle'][self.frame_index]
		self.rect = self.image.get_rect(bottomleft = pos)
		self.scale = 3.5
		
		# Player movement
		self.speed = 5
		self.is_idle = True
		self.faced_left = False


	def animate(self):
		if self.is_idle:
			status = 'idle'
		else:
			status = 'walk'
		animation = self.animations[status]

		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		new_size = self.rect.size[1] * self.scale

		if self.faced_left:
			image = pg.transform.scale(animation[int(self.frame_index)], (new_size, new_size))
			self.image = pg.transform.flip(image, True, False)
		else:
			self.image = pg.transform.scale(animation[int(self.frame_index)], (new_size, new_size))

	def import_player_assets(self):
		player_path = '../graphics/dino/'
		self.animations = {'idle':[], 'walk':[]}

		for animation in self.animations.keys():
			full_path = player_path + animation
			self.animations[animation] = import_folder(full_path)

	def get_inputs(self):
		keys = pg.key.get_pressed()
		
		if keys[pg.K_RIGHT]:
			self.rect.x += self.speed
			self.faced_left = False
			self.is_idle = False
			self.limit_players_position()

		if keys[pg.K_LEFT]:
			self.rect.x -= self.speed
			self.faced_left = True
			self.is_idle = False
			self.limit_players_position()

		if not keys[pg.K_LEFT] and not keys[pg.K_RIGHT]:
			self.is_idle = True

	def limit_players_position(self):
		if self.rect.left <= -20:
			self.rect.left = -20

		if self.rect.right >= 608:
			self.rect.right = 608

	def update(self):
			self.get_inputs()
			self.animate()
