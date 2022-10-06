from random import randint
from time import sleep
from threading import Thread
import pygame
from Models.Materiales import Materiales
from Models.Nave import *
from Models.Nodriza import *


class Naves():

    def __init__(self, velocidad):

        self.velocidad = velocidad
        self.tolerancia = self.velocidad*5+1

        self.nodriza_img = pygame.image.load("./Resources/Nave Madre.png")
        self.nodriza_img = pygame.transform.scale(self.nodriza_img, (300, 100))
        self.nodriza_rect = self.nodriza_img.get_rect()
        self.nodriza_rect.centerx = 150
        self.nodriza_rect.centery = 90
        self.nodriza = Nodriza("Nodriza", self.nodriza_img, self.nodriza_rect)

        self.nave1_img = pygame.image.load("./Resources/Naves.png")
        self.nave1_img = pygame.transform.scale(self.nave1_img, (100, 50))
        self.nave1_rect = self.nave1_img.get_rect()
        self.nave1_rect.centerx = 100
        self.nave1_rect.centery = 225
        self.nave1 = Nave("Nave 1", self.nave1_img, self.nave1_rect)

        self.nave2_img = pygame.image.load("./Resources/Naves.png")
        self.nave2_img = pygame.transform.scale(self.nave2_img, (100, 50))
        self.nave2_rect = self.nave2_img.get_rect()
        self.nave2_rect.centerx = 100
        self.nave2_rect.centery = 325
        self.nave2 = Nave("Nave 2", self.nave2_img, self.nave2_rect)

        self.nave3_img = pygame.image.load("./Resources/Naves.png")
        self.nave3_img = pygame.transform.scale(self.nave3_img, (100, 50))
        self.nave3_rect = self.nave3_img.get_rect()
        self.nave3_rect.centerx = 100
        self.nave3_rect.centery = 425
        self.nave3 = Nave("Nave 3", self.nave3_img, self.nave3_rect)

    def mostrar(self, screen):
        screen.blit(self.nodriza_img, self.nodriza_rect)
        screen.blit(self.nave1_img, self.nave1_rect)
        screen.blit(self.nave2_img, self.nave2_rect)
        screen.blit(self.nave3_img, self.nave3_rect)

    def obtener_disponible(self):
        while True:
            ran = randint(1, 3)
            # print(ran)
            if self.nave1.disponible == True:
                if ran == 1:
                    return self.nave1
            if self.nave2.disponible == True:
                if ran == 2:
                    return self.nave2
            if self.nave3.disponible == True:
                if ran == 3:
                    return self.nave3
            elif self.nave1.disponible == False and self.nave2.disponible == False and self.nave3.disponible == False:
                return None

    def mover(self, nave, ubicacion):
        #print(self.velocidad)
        if (nave.rect.centerx >= ubicacion.rect.centerx-self.tolerancia and nave.rect.centerx <= ubicacion.rect.centerx+self.tolerancia 
            and nave.rect.centery >= ubicacion.rect.centery-self.tolerancia and nave.rect.centery <= ubicacion.rect.centery+self.tolerancia):
            #print("Llego a: "+ubicacion.nombre)
            return True
        if nave.rect.centerx < ubicacion.rect.centerx:
            nave.rect.centerx += self.velocidad
        if nave.rect.centerx > ubicacion.rect.centerx:
            nave.rect.centerx -= self.velocidad
        if nave.rect.centery < ubicacion.rect.centery:
            nave.rect.centery += self.velocidad
        if nave.rect.centery > ubicacion.rect.centery:
            nave.rect.centery -= self.velocidad
