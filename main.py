import pygame, sys, character, random, functions
from pygame.locals import *

pygame.init()
pygame.mixer.init()


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


mapa = pygame.image.load('map.bmp')

"""
def health_regen():
    screen.fill(black)
    if player.health < 0:
        player.health = 0
    if player.health > 100:
        player.health = 100
    if player.health != 100:
        player.health += 0.1
    else:
        pass

def mana_regen():
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

tick = 0
k = 0
m = 0
alive = True


while m == 0:
    loop('start.wav')
    while k == 0:
        start_menu = pygame.image.load('start.png').convert()
        screen.blit(start_menu, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_ESCAPE:
                sys.exit()
            else:
                k = 1
                pygame.mixer.music.fadeout(2000)

    while alive == True:
        tick += 1
        if player.health < 0:
            alive = False
        screen.fill(black)
        clock.tick(40)
        health_regen()
        mana_regen()
        font = pygame.font.SysFont("monospace",30)
        hp = font.render("Health: " + str(int(round(player.health, 0))), 1, red)
        mp = font.render("Mana: " + str(int(round(player.mana, 0))), 1, blue)
        rn = font.render("Round: " + str(int(round(round_number, 0))), 1, white)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            up = event.type == KEYUP
            if event.key == K_UP:
                if player.xc < 0:
                    player.xc = 0
                elif player.yc < 0:
                    player.yc = 0
                elif player.xc > resx:
                    player.xc = resx
                elif player.yc > resy:
                    player.yc = resy
                else:
                    player.yc -= down * 5
            elif event.key == K_DOWN:
                if player.xc < 0:
                    player.xc = 0
                elif player.yc < 0:
                    player.yc = 0
                elif player.xc > resx:
                    player.xc = resx
                elif player.yc > resy-20:
                    player.yc = resy-20
                else:
                    player.yc += down * 5
            elif event.key == K_RIGHT:
                if player.xc < 0:
                    player.xc = 0
                elif player.yc < 0:
                    player.yc = 0
                elif player.xc > resx-20:
                    player.xc = resx-20
                elif player.yc > resy:
                    player.yc = resy
                else:
                    if player.rightflag == True:
                        player.xc += down * 5
                        leftflag = False
                    else:
                        player.character = pygame.transform.flip(player.character, True, False)
                        rightflag = True
                        leftflag = False
                        player.xc += down * 5
            elif event.key == K_LEFT:
                if player.xc < 0:
                    player.xc = 0
                elif player.yc < 0:
                    player.yc = 0
                elif player.xc > resx:
                    player.xc = resx
                elif player.yc > resy:
                    player.yc = resy
                else:
                    if player.leftflag == True:
                        player.xc -= down * 5
                        rightflag = False
                    else:
                        player.character = pygame.transform.flip(player.character, True, False)
                        player.rightflag = False
                        player.leftflag = True
                        player.xc -= down * 5
            if event.key == K_a:
                if down == True and downflag == False:
                    player.basic_attack()
                    player.detect(enemies)
                    downflag = True
                elif up == True:
                    player.funcreset()
                    downflag = False
            elif event.key == K_s:
                if down == True and downflag == False:
                    if player.mana > 25:
                        player.mana -= 25
                        player.special_attack()
                        play('special.wav')
                        player.special_detect(enemies)
                        downflag = True
                elif up == True:
                    player.funcreset()
                    downflag = False
            elif event.key == K_ESCAPE:
                sys.exit()
        for enemy in enemies:
            if tick > 10:
                if abs(enemy.xc-player.xc) < 5 and abs(enemy.yc-player.yc) < 5:
                    enemy.basic_attack()
                    print(enemy)
                    if hasattr(enemy,'houndflag'):
                        play('hound.wav')
                        player.health -= 25
                        enemy.funcreset()
                        tick = 0
                    if hasattr(enemy,'zombflag'):
                        play('zombie.wav')
                        player.health -= 10
                        enemy.funcreset()
                        tick = 0
        for enemy in enemies:
            speed = random.randrange(0,4)
            if enemy.xc < player.xc:
                if enemy.rightflag == True:
                    enemy.xc += speed
                    enemy.leftflag = False
                else:
                    enemy.character = pygame.transform.flip(enemy.character, True, False)
                    enemy.rightflag = True
                    enemy.leftflag = False
                    enemy.xc += speed
            if enemy.xc > player.xc:
                if enemy.leftflag == True:
                    enemy.xc -= speed
                    enemy.rightflag = False
                else:
                    enemy.character = pygame.transform.flip(enemy.character, True, False)
                    enemy.rightflag = False
                    enemy.leftflag = True
                    enemy.xc -= speed
            if enemy.yc < player.yc:
                enemy.yc += speed
            if enemy.yc > player.yc:
                enemy.yc -= speed

        for enemy in enemies:
            if enemy.health <= 0:
                enemies.remove(enemy)
                enemy = None
        if len(enemies) != 0:
            round_flag = True
        if len(enemies) == 0 and round_flag == True:
            round_number += 1
            round_flag = False
            if round_number % 5 == 0:
                for num in range(0,round_number):
                    rx = random.randrange(0, resx - 20)
                    ry = random.randrange(0, resy - 20)
                    enemies.append(character.Hound(screen, rx, ry))
            else:
                for num in range(0, 2 * round_number):
                    rx = random.randrange(0, resx-20)
                    ry = random.randrange(0, resy-20)
                    enemies.append(character.Zombie(screen, rx, ry))


        screen.blit(mapa, (0,0))
        screen.blit(hp, (20,15))
        screen.blit(mp, (20,45))
        screen.blit(rn, (20,75))
        for char in enemies:
            screen.blit(char.character, (char.xc,char.yc,))
        screen.blit(player.character, (player.xc,player.yc))
        pygame.display.flip()

    death_menu = pygame.image.load('death.png').convert()
    font2 = pygame.font.SysFont("monospace", 15)
    rcount = font2.render("You died. You survived: " + str(int(round(round_number, 0))) + " rounds", 1, red)
    cont = font2.render("Press C to continue, or any other key to quit", 1, red)
    screen.blit(death_menu, (0,0))
    screen.blit(rcount, (100,250))
    screen.blit(cont, (65, 265))
    pygame.display.flip()

    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        down = event.type == KEYDOWN
        if event.key == K_c:
            alive = True
            round_number = 0
            enemies = []
            player.health = 100
            player.mana = 50
        elif event.key == K_ESCAPE:
            sys.exit()
        else:
            m = 1"""

functions.startloop(screen)
functions.gameloop(screen, resx, resy, player, clock, enemies, alive, mapa, m)