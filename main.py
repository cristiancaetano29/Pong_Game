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
FONTE_PLACAR = pg.font.SysFont("comicsans", 50)


def draw(win, paredes, ball, placar_esquerda, placar_direita):
    win.fill(BLACK)

    placar_esquerda = FONTE_PLACAR.render(str(placar_esquerda), 1, WHITE)
    placar_direita = FONTE_PLACAR.render(str(placar_direita), 1, WHITE)
    win.blit(placar_esquerda, (largura//2 - 100, 10))
    win.blit(placar_direita, (largura//2 + 100, 10))

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


def colisaoParedes(parede_esquerda, parede_direita, bola):
    if bola.y + bola.radius >= altura:
        bola.velocidadeY *= -1
    elif bola.y - bola.radius <= 0:
        bola.velocidadeY *= -1

    if bola.velocidadeX < 0:
        if bola.y >= parede_esquerda.y and bola.y <= parede_esquerda.y + parede_esquerda.altura:
            if bola.x - bola.radius <= parede_esquerda.x + parede_esquerda.largura:
                bola.velocidadeX *= -1

                meio_y = parede_esquerda.y + parede_esquerda.altura / 2
                diferenca_y = meio_y - bola.y
                redutor = (parede_esquerda.altura / 2) / bola.VelocidadeMaxima
                velocidade_Y = diferenca_y / redutor
                bola.velocidadeY = -1 * velocidade_Y

    else:
        if bola.y >= parede_direita.y and bola.y <= parede_direita.y + parede_direita.altura:
            if bola.x + bola.radius >= parede_direita.x:
                bola.velocidadeX *= -1

                meio_y = parede_direita.y + parede_direita.altura / 2
                diferenca_y = meio_y - bola.y
                redutor = (parede_direita.altura / 2) / bola.VelocidadeMaxima
                velocidade_Y = diferenca_y / redutor
                bola.velocidadeY = -1 * velocidade_Y


def main():
    rodando = True
    clock = pg.time.Clock()
    parede_esquerda = paredesLaterais.ParedeLaterais(
        10, altura//2 - alturaParede//2, larguraParede, alturaParede)
    parede_direita = paredesLaterais.ParedeLaterais(
        largura - 10 - larguraParede, altura//2 - alturaParede//2, larguraParede, alturaParede)
    placar_esquerda = 0
    placar_direita = 0

    bola = ball.Ball(largura//2, altura//2, BOLARADIUS)

    while rodando:
        clock.tick(FPS)
        draw(tela, [parede_esquerda, parede_direita], bola, placar_esquerda, placar_direita)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

        keys = pg.key.get_pressed()
        movimentacao_Das_Paredes(keys, parede_direita, parede_esquerda)
        bola.mover()
        colisaoParedes(parede_esquerda, parede_direita, bola)

        if bola.x - bola.radius <= 0:
            placar_direita += 1
            bola = ball.Ball(largura//2, altura//2, BOLARADIUS)
        elif bola.x + bola.radius >= largura:
            placar_esquerda += 1
            bola = ball.Ball(largura//2, altura//2, BOLARADIUS)
        print(placar_esquerda, placar_direita)

    pg.quit()


if __name__ == "__main__":
    main()
