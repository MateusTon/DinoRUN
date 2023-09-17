import pygame as pg
import random as rd
from player import Player
from asteroids import Asteroids
from background import Background

class Game:
    def __init__(self):
        # Iniciando o Background
        bg = Background()
        self.bg_group = pg.sprite.GroupSingle()
        self.bg_group.add(bg)

        # Iniciando o Player
        player = Player((SCREEN_WIDTH / 2, 600))
        self.player_group = pg.sprite.GroupSingle()
        self.player_group.add(player)

        # Timer para Asteróids
        self.current_time = 0
        self.static_point = 0


        # Grupo de Sprites dos Asteróides
        self.asteroids_group = pg.sprite.Group()
        self.new_asteroids()

        
    def new_asteroids(self):
        # Iniciando varios asteróides
        for number in range(2):
            asteroid = Asteroids((rd.randrange(650), 0))
            self.asteroids_group.add(asteroid)


    def run(self):
        self.bg_group.draw(screen)

        self.player_group.update()
        self.player_group.draw(screen)

        self.current_time = pg.time.get_ticks()

        if self.current_time - self.static_point > 2000:
            self.new_asteroids()
            self.static_point = pg.time.get_ticks()

        self.asteroids_group.update()
        self.asteroids_group.draw(screen)

if __name__ == '__main__':
    pg.init()
    SCREEN_WIDTH = 650
    SCREN_HEIGHT = 700
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREN_HEIGHT))
    pg.display.set_caption('DinoRUN')
    clock = pg.time.Clock()
    running = True
    game = Game()


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((26, 225, 28))
        game.run()

        pg.display.flip()
        clock.tick(60)

    pg.quit()