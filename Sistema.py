import json
from threading import Thread
from time import sleep
import pygame
from Models.Planetas import *
from Models.Arbol import *


class Sistema():

    def __init__(self):

        self.font = pygame.font.SysFont("Roboto", 30)
        self.font_color = (255, 255, 255)
        self.font_bg = (0, 0, 0)

        # pluton
        self.pluton_img = pygame.image.load("./Resources/planeta08.png")
        self.pluton_img = pygame.transform.scale(self.pluton_img, (110, 110))
        self.pluton_rect = self.pluton_img.get_rect()
        self.pluton_rect.center = 800, 100

        # triton
        self.triton_img = pygame.image.load("./Resources/planeta01.png")
        self.triton_img = pygame.transform.scale(self.triton_img, (200, 200))
        self.triton_rect = self.triton_img.get_rect()
        self.triton_rect.center = 1100, 300

        # beltrak
        self.beltrak_img = pygame.image.load("./Resources/planeta02.png")
        self.beltrak_img = pygame.transform.scale(self.beltrak_img, (130, 130))
        self.beltrak_rect = self.beltrak_img.get_rect()
        self.beltrak_rect.center = 1100, 600

        # zork
        self.zork_img = pygame.image.load("./Resources/planeta03.png")
        self.zork_img = pygame.transform.scale(self.zork_img, (140, 140))
        self.zork_rect = self.zork_img.get_rect()
        self.zork_rect.center = 900, 420

        # yari
        self.yari_img = pygame.image.load("./Resources/planeta04.png")
        self.yari_img = pygame.transform.scale(self.yari_img, (200, 200))
        self.yari_rect = self.yari_img.get_rect()
        self.yari_rect.center = 800, 620

        # mercurio
        self.mercurio_img = pygame.image.load("./Resources/planeta06.png")
        self.mercurio_img = pygame.transform.scale(
            self.mercurio_img, (180, 130))
        self.mercurio_rect = self.mercurio_img.get_rect()
        self.mercurio_rect.center = 600, 220

        # tarca
        self.tarca_img = pygame.image.load("./Resources/planeta05.png")
        self.tarca_img = pygame.transform.scale(self.tarca_img, (190, 190))
        self.tarca_rect = self.tarca_img.get_rect()
        self.tarca_rect.center = 400, 400

        # zulman
        self.zulman_img = pygame.image.load("./Resources/planeta07.png")
        self.zulman_img = pygame.transform.scale(self.zulman_img, (195, 195))
        self.zulman_rect = self.zulman_img.get_rect()
        self.zulman_rect.center = 550, 600

        self.pluton = Planetas(100, "Pluton", "Oro", 50, self.pluton_rect)
        self.triton = Planetas(150, "Triton", "Plata", 90, self.triton_rect)
        self.beltrak = Planetas(
            200, "Beltrak", "Bronce", 100, self.beltrak_rect)
        self.zork = Planetas(120, "Zork", "Plata", 90, self.zork_rect)
        self.yari = Planetas(110, "Yari", "Oro", 110, self.yari_rect)
        self.mercurio = Planetas(
            50, "Mercurio", "Plata", 45, self.mercurio_rect)
        self.tarca = Planetas(20, "Tarca", "Bronce", 20, self.tarca_rect)
        self.zulman = Planetas(80, "Zulman", "Plata", 100, self.zulman_rect)

        self.arbol = Arbol(self.pluton)
        self.arbol.add(self.triton)
        self.arbol.add(self.beltrak)
        self.arbol.add(self.zork)
        self.arbol.add(self.yari)
        self.arbol.add(self.mercurio)
        self.arbol.add(self.tarca)
        self.arbol.add(self.zulman)

    def mostrar(self, screen):

        screen.blit(self.pluton_img, self.pluton_rect)
        screen.blit(self.triton_img, self.triton_rect)
        screen.blit(self.beltrak_img, self.beltrak_rect)
        screen.blit(self.zork_img, self.zork_rect)
        screen.blit(self.yari_img, self.yari_rect)
        screen.blit(self.mercurio_img, self.mercurio_rect)
        screen.blit(self.tarca_img, self.tarca_rect)
        screen.blit(self.zulman_img, self.zulman_rect)

    def contadores(self, screen):
        self.texto_planeta(screen, self.pluton, self.pluton_rect)
        self.texto_planeta(screen, self.triton, self.triton_rect)
        self.texto_planeta(screen, self.beltrak, self.beltrak_rect)
        self.texto_planeta(screen, self.zork, self.zork_rect)
        self.texto_planeta(screen, self.yari, self.yari_rect)
        self.texto_planeta(screen, self.mercurio, self.mercurio_rect)
        self.texto_planeta(screen, self.tarca, self.tarca_rect)
        self.texto_planeta(screen, self.zulman, self.zulman_rect)

    def texto_planeta(self, screen, planeta, rect):

        text1 = self.font.render(
            f"{planeta.nombre.upper()}", 1, self.font_color, self.font_bg)
        text2 = self.font.render(
            f"ID: {planeta.codigo}", 1, self.font_color, self.font_bg)
        text3 = self.font.render(
            f"{planeta.recurso}: {planeta.cantidad}", 1, self.font_color, self.font_bg)

        screen.blit(text1, (rect.x+(rect.width-text1.get_width()) /
                    2, -20+rect.y+(rect.height-text1.get_height())/2))
        screen.blit(text2, (rect.x+(rect.width-text2.get_width()) /
                    2, (rect.y+(rect.height-text2.get_height())/2)))
        screen.blit(text3, (rect.x+(rect.width-text3.get_width())/2,
                    20+(rect.y+(rect.height-text3.get_height())/2)))
