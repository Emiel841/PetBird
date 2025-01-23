import pygame
from kid_pet import KidPet
from os.path import join

class Egg(pygame.sprite.Sprite):
    def __init__(self, groups, pos, screen):
        super().__init__(groups)
        self.frames = [pygame.transform.scale(pygame.image.load(join("Assets", "Pet", "Egg", str(i) + ".png")).convert_alpha(), (256, 256)) for i in range(4)]
        self.image = self.frames[0]
        self.rect = self.image.get_frect(center=pos)
        self.times_clicked = 0
        self.groups = groups
        self.screen = screen
        self.last_click = pygame.time.get_ticks()

    def update(self, dt):
        if self.clicked():
            self.times_clicked += 1
            if self.times_clicked == 30:
                self.image = self.frames[1]
            if self.times_clicked == 60:
                self.image = self.frames[2]
            if self.times_clicked == 90:
                self.image = self.frames[3]
            if self.times_clicked == 110:
                self.kill()
                KidPet(self.groups, self.rect.center, self.screen)

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_just_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0] and self.timeout():
            return True
        return False

        return False

    def timeout(self):
        now = pygame.time.get_ticks()
        if now-self.last_click >= 200:
            self.last_click = now
            return True
        return False

    def draw_ui(self):
        pass