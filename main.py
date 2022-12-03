import pygame as pg
from pygame.locals import (
    K_ESCAPE,
    K_F2,
    K_SPACE

)

import ball
import paredesLaterais

pg.init()

largura, altura = 900, 500

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Pong Game")

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)

larguraParede, alturaParede = 20, 100
BOLARADIUS = 15
FONTE_PLACAR = pg.font.SysFont("comicsans", 50)
FONTE_MENU = pg.font.SysFont("comicsans", 30)
FONTE_GANHADOR = pg.font.SysFont("comicsans", 40)
PLACAR_VENCEDOR = 3


def draw(win, paredes, ball, placar_esquerda, placar_direita):
    win.fill(BLACK)

    placar_esquerda = FONTE_PLACAR.render(str(placar_esquerda), 1, WHITE)
    placar_direita = FONTE_PLACAR.render(str(placar_direita), 1, WHITE)
    win.blit(placar_esquerda, (largura//2 - 100, 10))
    win.blit(placar_direita, (largura//2 + 100, 10))

    for parede in paredes:
        parede.draw(win)

    for i in range(altura//10):
        pg.draw.rect(win, YELLOW, (largura//2 - 5, i*10, 10, 10))

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
    parede_esquerda = paredesLaterais.ParedeLaterais(10, altura//2 - alturaParede//2, larguraParede, alturaParede)
    parede_direita = paredesLaterais.ParedeLaterais(largura - 10 - larguraParede, altura//2 - alturaParede//2, larguraParede, alturaParede)
    placar_esquerda = 0
    placar_direita = 0

    bola = ball.Ball(largura//2, altura//2, BOLARADIUS)

    while rodando:
        clock.tick(FPS)
        draw(tela, [parede_esquerda, parede_direita],bola, placar_esquerda, placar_direita)

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

        if placar_esquerda >= PLACAR_VENCEDOR:
            TEXTO_VENCEDOR = FONTE_GANHADOR.render("Jogador da esquerda ganhou", 1, WHITE)
            tela.blit(TEXTO_VENCEDOR, (largura//2 - TEXTO_VENCEDOR.get_width() //2, altura//2 - TEXTO_VENCEDOR.get_height()//2))
            pg.display.update()
            pg.time.delay(2000)
            menuFinal(tela)
        elif placar_direita >= PLACAR_VENCEDOR:
            TEXTO_VENCEDOR = FONTE_GANHADOR.render("Jogador da direita ganhou", 1, WHITE)
            tela.blit(TEXTO_VENCEDOR, (largura//2 - TEXTO_VENCEDOR.get_width() //2, altura//2 - TEXTO_VENCEDOR.get_height()//2))
            pg.display.update()
            pg.time.delay(2000)
            menuFinal(tela)
    pg.quit()


def menuInicial(win):
    run = True
    while run:
        win.fill(BLACK)
        titulo = FONTE_MENU.render("Pressione qualquer tecla para jogar", 1, WHITE)
        win.blit(titulo, (largura//2 - titulo.get_width() //2, altura//2 - titulo.get_height()//2))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                main()
    pg.quit()


def menuFinal(win):
    run = True
    while run:
        win.fill(BLACK)
        tituloFinal = FONTE_MENU.render("Pressione espaco para jogar novamente ou esc para sair", 1, WHITE)
        win.blit(tituloFinal, (largura//2 - tituloFinal.get_width() //2, altura//2 - tituloFinal.get_height()//2))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()

            if event.key == K_SPACE:
                main()

            if event.key == K_ESCAPE:
                run = False
                pg.quit()

    pg.quit()



if __name__ == "__main__":
    menuInicial(tela)