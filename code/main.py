import pygame as pg
import random as rd
from player import Player
from asteroids import Asteroids

class Game:
    def __init__(self):
        # Iniciando o Player
        player = Player((SCREEN_WIDTH / 2, 600))
        self.player_group = pg.sprite.GroupSingle()
        self.player_group.add(player)

        # Inciando primeiro esteróide
        asteroid = Asteroids((SCREEN_WIDTH / 2, 0))
        self.asteroids_group = pg.sprite.Group()
        self.asteroids_group.add(asteroid)

    def run(self):
        self.player_group.update()
        self.player_group.draw(screen)

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