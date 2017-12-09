import pygame, sys, time, random
from pygame.locals import *

black = (0,0,0)
n = 0

def play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)

class Character:
    def __init__(self, surface, x,y):
        self.health = 100
        self.mana = 50
        self.surf = surface
        self.xc = x
        self.yc = y
        self.character = pygame.image.load('character.png').convert_alpha()
        self.attack = pygame.image.load('attack.png').convert_alpha()
        self.special = pygame.image.load('special.png').convert_alpha()
        self.reset = pygame.image.load('character.png').convert_alpha()
        self.check = False
        self.rightflag = None
        self.leftflag = None

    def detect(self, enemies):
        self.enemies = enemies
        for enemy in enemies:
            xprox = abs(enemy.xc - self.xc)
            yprox = abs(enemy.yc - self.yc)
            if xprox < 50 and yprox < 50:
                enemy.health -= 15
                play('hit.wav')
            else:
                play('attack.wav')

    def special_detect(self, enemies):
        self.enemies = enemies
        for enemy in enemies:
            xprox = abs(enemy.xc - self.xc)
            yprox = abs(enemy.yc - self.yc)
            if xprox < 150 and yprox < 150:
                enemy.health -= 50

    def basic_attack(self):
        self.surf.fill(black)
        self.character = self.attack
        self.surf.blit(self.character, (self.xc,self.yc))
        pygame.display.flip()

    def special_attack(self):
        self.surf.fill(black)
        self.character = self.special
        self.surf.blit(self.character, (self.xc, self.yc))
        pygame.display.flip()

    def funcreset(self):
        self.surf.fill(black)
        self.character = self.reset
        self.surf.blit(self.character, (self.xc, self.yc))
        pygame.display.flip()

class Zombie:
    def __init__(self, surface, x, y):
        self.health = 50
        self.surf = surface
        self.xc = x
        self.yc = y
        self.character = pygame.image.load('zombie.png').convert_alpha()
        self.attack = pygame.image.load('zombieattack.png').convert_alpha()
        self.reset = pygame.image.load('zombie.png').convert_alpha()
        self.zombflag = True
        self.rightflag = None
        self.leftflag = None

    def basic_attack(self):
        self.surf.fill(black)
        self.character = self.attack
        self.surf.blit(self.character, (self.xc,self.yc))
        pygame.display.flip()

    def funcreset(self):
        self.surf.fill(black)
        self.character = self.reset
        self.surf.blit(self.character, (self.xc, self.yc))
        pygame.display.flip()

class Hound:
    def __init__(self, surface, x, y):
        self.health = 100
        self.surf = surface
        self.xc = x
        self.yc = y
        self.character = pygame.image.load('hound.png').convert_alpha()
        self.attack = pygame.image.load('houndattack.png').convert_alpha()
        self.reset = pygame.image.load('hound.png').convert_alpha()
        self.houndflag = True
        self.rightflag = None
        self.leftflag = None

    def basic_attack(self):
        self.surf.fill(black)
        self.character = self.attack
        self.surf.blit(self.character, (self.xc,self.yc))
        pygame.display.flip()

    def funcreset(self):
        self.surf.fill(black)
        self.character = self.reset
        self.surf.blit(self.character, (self.xc, self.yc))
        pygame.display.flip()













