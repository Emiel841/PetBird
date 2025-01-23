import pygame
import random
from ui import UI
from os.path import join

class KidPet(pygame.sprite.Sprite):
    def __init__(self, groups, pos, screen):
        super().__init__(groups)
        self.screen = screen
        frame_amount = 2
        self.baseframes = [pygame.transform.scale(pygame.image.load(join("Assets", "Pet", "Normal", str(i) + ".png")).convert_alpha(), (512, 512)) for i in range(frame_amount)]
        self.frames = self.baseframes
        self.hungry_frames = [pygame.transform.scale(pygame.image.load(join("Assets", "Pet", "Hungry", str(i) + ".png")).convert_alpha(), (512, 512)) for i in range(frame_amount)]
        self.sick_frames = [pygame.transform.scale(pygame.image.load(join("Assets", "Pet", "Thermometer", str(i) + ".png")).convert_alpha(), (512, 512)) for i in range(frame_amount)]
        self.dirty_frames = [pygame.transform.scale(pygame.image.load(join("Assets", "Pet", "Dirty", str(i) + ".png")).convert_alpha(), (512, 512)) for i in range(frame_amount)]
        self.base_image = self.frames[0]
        self.image = pygame.Surface((512, 512))
        self.image.blit(self.base_image, (0, 0))
        self.rect = self.image.get_frect(center=pos)
        self.hunger = 100
        self.dirty = 0
        self.is_sick = False
        self.prevhunger_tick = pygame.time.get_ticks()
        self.prev_dirt_tick = pygame.time.get_ticks()
        self.hunger_time = 1000
        self.dirt_time = 1000
        self.sick_time = random.randint(10000, 50000)
        self.prev_sick_tick = pygame.time.get_ticks()
        self.xp = 0
        self.max_xp = 300
        self.ui = UI(self.max_xp, self.hunger, screen)
        self.currentframe = 0

        self.is_dirty = False
        self.is_hungry = False


    def animate(self, dt):
        self.image.fill("white")

        if self.is_hungry:
            self.base_image = self.hungry_frames[int(self.currentframe)]
        else:
            self.base_image = self.frames[int(self.currentframe)]

        self.image.blit(self.base_image, (0, 0))

        if self.is_dirty:
            self.image.blit(self.dirty_frames[int(self.currentframe)])
        if self.is_sick:
            self.image.blit(self.sick_frames[int(self.currentframe)])

        self.currentframe += 1 *dt
        if self.currentframe >= len(self.frames):
            self.currentframe = 0


    def check_tasks(self):
        now = pygame.time.get_ticks()
        if now - self.prevhunger_tick >= self.hunger_time:
            self.prevhunger_tick = now
            self.hunger -= 2
            if self.is_sick:
                self.hunger -= 2
            print(self.hunger)
        if now - self.prev_dirt_tick >= self.dirt_time:
            self.prev_dirt_tick = now
            self.dirty += 1

        if not self.is_sick:
            if now - self.prev_sick_tick >= self.sick_time:
                self.sick_time = random.randint(5000, 10000)
                self.is_sick = True


        if self.dirty < 50: self.is_dirty = False
        else: self.is_dirty = True
        if self.dirty >= 100: self.die()

        if self.hunger < 50: self.is_hungry = True
        else: self.is_hungry = False
        if self.hunger <= 0: self.die()


    def die(self):
        self.kill()


    def update(self, dt):

        self.check_tasks()

        button_clicked = self.ui.get_button()
        if button_clicked == "feed":
            xp_gained = 100-self.hunger
            if xp_gained > 30: xp_gained = 30
            self.xp += xp_gained
            self.hunger += 30
            if self.hunger > 100:
                self.hunger = 100
            self.check_xp()
        if button_clicked == "wash":
            xp_gained = self.dirty
            if xp_gained > 30: xp_gained = 30
            self.xp += xp_gained
            self.dirty -= 30
            if self.dirty < 0:
                self.dirty = 0
            if self.check_xp():
                self.become_adult()

        if button_clicked == "cure" and self.is_sick:
            print("cure")
            self.is_sick = False
            self.sick_time = random.randint(10000, 50000)
            self.prev_sick_tick = pygame.time.get_ticks()


        self.animate(dt)

        self.ui.bars(self.xp, self.max_xp, self.hunger)




    def check_xp(self):
        if self.xp >= self.max_xp:
            return True

    def draw_ui(self):
        self.ui.draw()

    def become_adult(self):
        self.kill()