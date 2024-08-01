import pygame
import os
from scryptnetwork import Network
from Scrypt_player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.mouse.set_visible(False)


def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player2.draw(win)
    player.draw(win)
    win.blit(pygame.image.load(os.path.join("Scryption_Display", "Cursor", "normal.png")), player2.mousePos)
    win.blit(pygame.image.load(os.path.join("Scryption_Display", "Cursor", "normal.png")), player.mousePos)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()
