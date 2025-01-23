from egg import Egg
from kid_pet import KidPet
import pygame

class Game:
    def __init__(self):
        pygame.init()
        SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.pet = pygame.sprite.Group()
        self.pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        Egg((self.all_sprites, self.pet), self.pos, self.screen)
        self.pet_stage = 0
        self.pet_died = False

    def draw(self):
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)
        self.pet.sprites()[0].draw_ui()

        pygame.display.update()

    def run(self):
        while self.running:

            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update(dt)
            self.draw()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()



