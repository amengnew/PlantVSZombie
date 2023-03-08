import pygame


class SeedBank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("photo/others/SeedBank.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 40, - self.rect.height
        self.position = False
        self.speed = 5

    def move(self):
        if self.rect.top < 0:
            self.rect.top += self.speed
        else:
            self.rect.top = 0
            self.position = True
