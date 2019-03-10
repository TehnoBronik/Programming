import pygame,sys
import time
import random
pygame.init()
RED = [225, 0, 0]
GREEN = [0, 255, 0]
SCREEN_COLOR = [0, 0, 0]
G = 1


class  Rings():
    def __init__ (self, screen,  color, centr, r, t):
        self.screen = screen
        self.color = color
        self.centr = centr
        self.r = r
        self.t = t
        self.mass = 100
        self.vel_x = random.randint(-3, 3)
        self.vel_y = random.randint(-3, 3)
        self.stop = False

    def update(self):
        if self.stop: return
        if self.centr[1] + self.vel_y > 480 - self.r:
            print(self.vel_y)
            if 0 < self.vel_y < 4:
                    self.vel = 0
                    self.stop = True
            self.vel_y = - self.vel_y * 0.8
            self.centr[1] = 480 - self.r
            self.centr[0] += round(self.vel_x)
        else:
            self.centr[0] += round(self.vel_x)
            self.centr[1] += round(self.vel_y)
            self.vel_y += G

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.centr, self.r, self.t)

    def change_color(self):
        self.color[0] = (self.color[0] + 10) % 255
        self.color[1] = (self.color[1] + 12) % 255
        self.color[2] = (self.color[2] + 14) % 255


screen = pygame.display.set_mode([640,480])
screen.fill(SCREEN_COLOR)
ring1 = Rings(screen, GREEN, (200, 200), 80, 6)
rings = []
for i in range(10):
    rings.append(Rings(screen, [100, i*10, i*10], [100, 30+30*i], 30, 6))
for ring in rings:
    ring.draw()
ring2 = Rings(screen, [150, i*5, i*5], [200, 30+20*i], 30, 6)
rings1 = [Rings(screen, GREEN, [300, 200], 80, 6) for i in range(10)]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(SCREEN_COLOR)
    ring2.change_color()
    ring2.update()
    #ring2.draw()
    '''for ring in rings:
        ring.update()
        ring.change_color()
        ring.draw()'''
    for ring in rings1:
        ring.update()
        ring.update1()
        ring.change_color()
        ring.draw()
    time.sleep(0.1)
    pygame.display.flip()
