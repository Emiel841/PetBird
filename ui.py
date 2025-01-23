from bar import Bar
from button import Button
import pygame

class UI:
    def __init__(self, max_xp, max_food, screen):
        self.xp_bar = Bar(20, 10, 200, 20, 100, 0, "green", "black")
        self.food_bar = Bar(20, 40, 300, 30, 100, 100, "brown", "black")
        bg = pygame.image.load("Assets/Ui/Button/holder.png").convert_alpha()
        food = pygame.image.load("Assets/Ui/Button/food.png").convert_alpha()
        sponge = pygame.image.load("Assets/Ui/Button/sponge.png").convert_alpha()
        pills = pygame.image.load("Assets/Ui/Button/pills.png")
        self.feed_button = Button((400, 560), 60, 60, bg, food, "feed")
        self.wash_button = Button((500, 560), 60, 60, bg, sponge, "wash")
        self.cure_button = Button((800, 560), 60, 60, bg, pills, "cure")
        self.buttons = [self.feed_button, self.wash_button, self.cure_button]
        self.screen = screen
        #self.cure_button = Button

    def get_button(self):
        for button in self.buttons:
            if button.clicked():
                return button.id

    def bars(self, xp, maxp, food):
        self.xp_bar.update_value(xp, maxp)
        self.food_bar.update_value(food, 100)

    def draw(self):
        self.screen.blit(self.feed_button.image, self.feed_button.rect)
        self.screen.blit(self.wash_button.image, self.wash_button.rect)
        self.screen.blit(self.cure_button.image, self.cure_button.rect)
        self.food_bar.draw(self.screen)
        self.xp_bar.draw(self.screen)