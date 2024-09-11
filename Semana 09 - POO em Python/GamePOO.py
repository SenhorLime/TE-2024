from typing import List
import pygame
from pygame.locals import *

import Player
import Bola


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.__running = True

        self.__lastTime = 0
        self.__objectsOut = 0
        self.__clock = pygame.time.Clock()
        self.__currentTime = pygame.time.get_ticks()

        self.__screen = pygame.display.set_mode([800, 600])

        self.__dropImg = pygame.image.load("assets\\droplet.png").convert_alpha()
        self.__bucketImg = pygame.image.load("assets\\bucket.png").convert_alpha()
        self.__fundoImg = pygame.image.load("assets\\fundo.png").convert_alpha()

        self.__musicaFundo = pygame.mixer.music.load("assets\\rain.ogg")
        self.__barulhoColisao = pygame.mixer.Sound("assets\\drop.ogg")

        self.__font = pygame.font.SysFont("assets\\x-files.ttf", 32)

        self.__bolas = []
        self.__player = Player.Player(self.__bucketImg)

    def createObject(self, x=0, y=0):
        bola1 = Bola.Bola(self.__dropImg, self.__screen.get_width(), x, y)
        self.__bolas.append(bola1)
        self.__lastTime = pygame.time.get_ticks()

    def run(self):
        pygame.display.set_caption("Rain Game")
        pygame.display.set_icon(self.__dropImg)

        pygame.mixer.music.play(-1)
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.createObject(event.pos[0], event.pos[1])

            for bola in self.__bolas:
                bola.update()

                if bola.getRect().y > self.__screen.get_height():
                    self.__bolas.remove(bola)
                elif not bola.isLive:
                    self.__bolas.remove(bola)
                    self.__objectsOut += 1

            self.__player.update(pygame.key)

            text = self.__font.render(str(self.__objectsOut), True, (0, 0, 255))

            self.__currentTime = pygame.time.get_ticks()
            if (self.__currentTime - self.__lastTime) > 1000:
                self.createObject()

            self.__screen.blit(self.__fundoImg, (0, 0))

            for bola in self.__bolas:
                bola.draw(self.__screen)

                if bola.getRect().colliderect(self.__player.getRect()):
                    bola.isLive = False
                    self.__barulhoColisao.play()

            self.__player.draw(self.__screen)

            self.__screen.blit(text, (740, 20))
            self.__screen.blit(
                self.__font.render(str(self.__currentTime), True, (0, 0, 255)),
                (700, 40),
            )
            self.__screen.blit(
                self.__font.render(str(self.__lastTime), True, (0, 0, 255)), (700, 60)
            )
            self.__screen.blit(
                self.__font.render(
                    str(self.__currentTime - self.__lastTime), True, (0, 0, 255)
                ),
                (700, 80),
            )

            pygame.display.flip()
            self.__clock.tick(60)

        pygame.quit()


game = Game()
game.run()
