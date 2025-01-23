import pygame

class Button:
    def __init__(self, pos, w, h, bg, icon, id):
        self.image = pygame.Surface((w, h))
        self.bg = pygame.transform.scale(bg, (w, h))
        self.icon = pygame.transform.scale(icon, (w, h))
        self.image.blit(self.bg, (0, 0))
        self.image.blit(self.icon, (2, 2))
        self.rect = self.image.get_rect(center = pos)
        self.id = id
        self.last_click = pygame.time.get_ticks()

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_just_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0] and self.timeout():
            return True
        return False

        return False

    def timeout(self):
        now = pygame.time.get_ticks()
        if now - self.last_click >= 200:
            self.last_click = now
            return True
        return False

