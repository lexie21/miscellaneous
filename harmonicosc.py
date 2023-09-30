import pygame as pg
import sys

W,H = 500,500
POS = 1
t = 0.1

clock = pg.time.Clock()
FPS = 40

class Particle:
    
    def __init__(self,game,x):
        self.game = game
        self.x = x
        self.velocity = 0
    
    def movement(self):
        self.x += t*self.velocity
        acceleration = -self.x
        self.velocity += t*acceleration
    
    def draw(self):
        pg.draw.circle(self.game.screen,'blue',(W/2+self.x*100,H/2),10)

    def update(self):
        self.movement()

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([W,H])
        self.clock = pg.time.Clock()
        self.initialize()

    def initialize(self):
        self.particle = Particle(self,POS)
        # self.particle.update()

    def update(self):
        self.particle.update()
        pg.display.flip()
        clock.tick(FPS)
    
    def draw(self):
        self.screen.fill('black')
        self.particle.draw()

    def check_events(self):
         for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            print('here')

while __name__ =='__main__':
    game = Game()
    game.run()


#TODO: create a cluster of particles with different initial velocities and positions, using list comprehension
#put all constants into a setting file