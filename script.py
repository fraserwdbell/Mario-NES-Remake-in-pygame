import pygame
import random
import sys
pygame.init()

def load_image(name):
    image = pygame.image.load(name)
    return image

displayWidth = 650
displayHeight = 240
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Mario Test Game BETA 1.0")
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

x = 0
y = 0

all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Usually, I add a single image, but I have a folder called walk, containing all sprites to animate.
        self.rect = self.image.get_rect()
        self.rect.centerx = displayWidth / 2
        self.rect.bottom = displayHeight - 32
        self.speedx = 3
        self.rect.x = 0
    def update(self):
        self.image = self.images[self.index]
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speedx = 2
        if keystate[pygame.K_LEFT]:
            self.speedx = -2
        self.rect.x += self.speedx
        
player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gameDisplay.fill(white)
    gameDisplay.blit(map1, (0,0))
    clock.tick(60)
    all_sprites.draw(gameDisplay)
    all_sprites.update()
    pygame.display.flip()


pygame.quit()
