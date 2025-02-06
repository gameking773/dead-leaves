from pygame import *
from random import *

init()

screen_width = 800
screen_height = 620

screen = display.set_mode((screen_height, screen_width))
display.set_caption("Dead Leaves")

leaf1 = image.load("leaf1.png")
leaf2 = image.load("leaf2.png")

class DeadLeaves(sprite.Sprite):
    def __init__(self, screen):

        self.image = choice(leaf1, leaf2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = random.randint(-20, screen_height)

    def update(self):
        self.rect.y += 5
        self.rect.x += random.randint(-5, 5)
        if self.rect.y > screen_height:
            self.rect.y = random.randint(-20,-1)
            self.rect.x = random.randint(0, screen_width)
        
leaves = sprite.Group()

running = True

while running:
    screen.fill((0, 0, 0))

    for e in event.get():
        if e.type == QUIT:
            running = False

    leaves.update()

    leaves.draw(screen)

    display.flip()

quit()