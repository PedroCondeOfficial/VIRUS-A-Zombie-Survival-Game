import pygame, sys, character, random, time
from pygame.locals import *

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0, 0, 0)

resx = 500
resy = 500
screen = pygame.display.set_mode((resx, resy))
clock = pygame.time.Clock()
round_number = 0
pygame.key.set_repeat(10, 10)
player = character.Character(screen, 250, 250)
downflag = False
enemies = []
round_flag = True
alive = True
m = 0

def health_regen(player):
    if player.health < 0:
        player.health = 0
    if player.health > 100:
        player.health = 100
    if player.health != 100:
        player.health += 0.1
    else:
        pass
def mana_regen(player):
    if player.mana < 0:
        player.mana = 0
    if player.mana > 50:
        player.mana = 50
    if player.mana != 50:
        player.mana += 0.1
    else:
        pass

def play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
def loop(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
