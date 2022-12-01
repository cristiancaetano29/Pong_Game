import pygame as pg

WHITE = (255, 255, 255)


class ParedeLaterais:
    COR = WHITE
    VELOCIDADE = 5

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def draw(self, win):
        pg.draw.rect(win, self.COR, (self.x, self.y,
                     self.largura, self.altura))

    def mover(self, up=True):
        if up:
            self.y -= self.VELOCIDADE
        else:
            self.y += self.VELOCIDADE
