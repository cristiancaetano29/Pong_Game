import pygame as pg

import ball
import paredesLaterais

pg.init()

largura, altura = 700, 500

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Pong Game")

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
larguraParede, alturaParede = 20, 100
BOLARADIUS = 10

"""
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
"""


def draw(win, paredes, ball):
    win.fill(BLACK)

    for parede in paredes:
        parede.draw(win)

    for i in range(altura//10):
        pg.draw.rect(win, WHITE, (largura//2 - 5, i*10, 10, 10))

    ball.draw(win)
    pg.display.update()


def movimentacao_Das_Paredes(keys, parede_esquerda, parede_direita):
    if keys[pg.K_UP] and parede_esquerda.y > 0:
        parede_esquerda.mover(True)
    if keys[pg.K_DOWN] and parede_esquerda.y < altura - alturaParede:
        parede_esquerda.mover(False)
    if keys[pg.K_w] and parede_direita.y > 0:
        parede_direita.mover(True)
    if keys[pg.K_s] and parede_direita.y < altura - alturaParede:
        parede_direita.mover(False)


def main():
    rodando = True
    clock = pg.time.Clock()
    parede_esquerda = paredesLaterais.ParedeLaterais(
        10, altura//2 - alturaParede//2, larguraParede, alturaParede)
    parede_direita = paredesLaterais.ParedeLaterais(
        largura - 10 - larguraParede, altura//2 - alturaParede//2, larguraParede, alturaParede)

    bola = ball.Ball(largura//2, altura//2, BOLARADIUS)

    while rodando:
        clock.tick(FPS)
        draw(tela, [parede_esquerda, parede_direita], bola)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

        keys = pg.key.get_pressed()
        movimentacao_Das_Paredes(keys, parede_direita, parede_esquerda)
        bola.mover()

    pg.quit()


if __name__ == "__main__":
    main()
