import pygame
from params import *
from player import *
from img_utils import *

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spritesheet = Spritesheet("C:\\Programming\\Programming\\Game\\img\\p1_spritesheet.png")

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #update
            self.all_sprites.update()
            #draw/render
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)

            #FLIP
            pygame.display.flip()

if __name__ == "__main__":
    G = Game()
    G.new()
