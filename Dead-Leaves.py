from pygame import *
from random import *

init()

screen_width = 600
screen_height = 600

screen = display.set_mode((screen_height, screen_width))
display.set_caption("Dead Leaves")

leaf1 = image.load('sprites/leaf1.png')
leaf2 = image.load('sprites/leaf2.png')

class DeadLeaves(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = choice([leaf1, leaf2])

        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen_width)
        self.rect.y = randint(-20, screen_height)

    def update(self):
        self.rect.y += 1
        self.rect.x += randint(-10, 10)
        if self.rect.y > screen_height:
            self.rect.y = randint(-20,-1)
            self.rect.x = randint(0, screen_width)
        
leaves = sprite.Group()

for i in range (100):
    leaf = DeadLeaves()
    leaves.add(leaf)

running = True
while running:
    screen.fill((0, 0, 0))

    for e in event.get():
        if e.type == QUIT:
            running = False

    leaves.update()

    leaves.draw(screen)

    display.flip()

    time.Clock().tick(60)

quit()