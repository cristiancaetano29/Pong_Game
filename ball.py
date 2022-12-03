import pygame as pg

import paredesLaterais

WHITE = (255, 255, 255)
BLUE = (0,0,255)

class Ball:
    VelocidadeMaxima = 5
    COR = BLUE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocidadeX = self.VelocidadeMaxima
        self.velocidadeY = 0

    def draw(self, win):
        pg.draw.circle(win, self.COR, (self.x, self.y), self.radius)

    def mover(self):
        self.x += self.velocidadeX
        self.y += self.velocidadeY
