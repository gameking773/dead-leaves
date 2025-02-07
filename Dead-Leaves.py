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
        self.taille = randint(5, 8)
        self.image = choice([leaf1, leaf2])

        self.image = transform.scale(self.image, (self.taille * 10, self.taille * 10))

        self.rect = self.image.get_rect()
        self.rect.x = randint(0, screen_width)
        self.rect.y = randint(-20, screen_height)
        self.vitesse = uniform(0.5, 2.0) 
        self.direction = choice([-2, 2]) 


    def update(self):
        self.rect.y += self.vitesse
        self.rect.x += self.direction*0.5
        if self.rect.x <= 0 or self.rect.x >= screen_width:
            self.direction *= -1
        if self.rect.y >= screen_height:
            self.rect.y = randint(-20,-1)
            self.rect.x = randint(0, screen_width)

    def touchedby(self, curseur_x, curseur_y):
        return (self.rect.x <= curseur_x <= self.rect.x + self.taille * 10) and (self.rect.y <= curseur_y <= self.rect.y + self.taille*10)


leaves = sprite.Group()

def newLeaf():
    return DeadLeaves()


for i in range (50):
    leaf = DeadLeaves()
    leaves.add(leaf)

score = 0
r,v,b = 0,0,0
running = True

while running:
    r = r  % 256  

    screen.fill((r,v,b))

    suppLeaf = []

    for e in event.get():
        if e.type == QUIT:
            running = False

    curseur_x, curseur_y = mouse.get_pos()

    for leaf in leaves:
        if leaf.update():
            score += 1
   
        
        if leaf.touchedby(curseur_x, curseur_y):
                score += 1
                leaf.y = randint(-100, -10)
                suppLeaf.append(leaf)
                leaves.add(newLeaf())  
                r+=1

    # Supprimer les feuilles touchées
    for feuille in suppLeaf:
        leaves.remove(feuille)


    leaves.draw(screen)

    scoretxt = police.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(scoretxt, (screen_width - scoretxt.get_width() - 20, 20))

    display.flip()

    time.Clock().tick(60)

quit()