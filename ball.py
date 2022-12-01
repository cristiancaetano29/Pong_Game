import pygame as pg

import paredesLaterais

WHITE = (255, 255, 255)


class Ball:
    VelocidadeMaxima = 10
    COR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocidadeX = self.VelocidadeMaxima
        self.velocidadeY = 0

    def draw(self, win):
        pg.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def mover(self, paredes):
        self.x += self.velocidadeX
        self.y += self.velocidadeY

