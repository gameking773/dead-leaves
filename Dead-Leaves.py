from pygame import *
from random import *

init()

screen_width = 600
screen_height = 600
police = font.SysFont("Arial", 30)
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
        self.vitesse = uniform(0.5, 2.0) 
        self.direction = choice([-2, 2]) 
        self.taille = randint(2, 4)

    def update(self):
        self.rect.y += self.vitesse
        self.rect.x += self.direction*0.5
        if self.rect.x <= 0 or self.rect.x >= screen_width:
            self.direction *= -1
        if self.rect.y >= screen_height:
            self.rect.y = randint(-20,-1)
            self.rect.x = randint(0, screen_width)

leaves = sprite.Group()

for i in range (100):
    leaf = DeadLeaves()
    leaves.add(leaf)

score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for e in event.get():
        if e.type == QUIT:
            running = False

    for leaf in leaves:
        if leaf.update():
            score += 1
        

    leaves.draw(screen)

    scoretxt = police.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(scoretxt, (screen_width - scoretxt.get_width() - 20, 20))

    display.flip()

    time.Clock().tick(60)

quit()