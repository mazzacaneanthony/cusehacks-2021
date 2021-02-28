"""
This program will be a 2D Shooter where the player's goal is to Mask as many people
as possible
"""
import pygame as pg
import random
from time import sleep
from sys import exit

# Initialization
pg.init()
screenWidth = 960
screenHeight = 640
screen = pg.display.set_mode((screenWidth, screenHeight))
clock = pg.time.Clock()
gameStatus = True

# Sets the window name and icon
pg.display.set_caption("2D Mask Shooter")
name = pg.image.load('Game Sprites/player.png').convert()
pg.display.set_icon(name)

# NPC Class

# Projectile Class
mask = pg.image.load('Game Sprites/maskBullet2.png')
class projectile(object):
    def __init__ (self, x, y, spdx, spdy):
        self.x = x
        self.y = y
        self.spdx = spdx
        self.spdy = spdy
        self.hitbox = (self.x, self.y, 15, 15)
    def draw(self, screen):
        screen.blit(mask, (self.x, self.y))
        pg.draw.rect(screen, (0, 255, 0), self.hitbox, 2)

#Background
bgSurface = pg.image.load('Game Sprites/Background.png').convert()

#Player object
playerSurf = pg.image.load('Game Sprites/player.png').convert_alpha()
playerSurf = pg.transform.scale2x(playerSurf)
playerRect = playerSurf.get_rect()


class char(object):
    def __init__ (self, x, y, width, height, spd):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spd = spd
        self.hitbox = (self.x + 20, self.y - 25, 28, 60)
    def draw(self, screen):
        screen.blit(playerSurf, (self.x, self.y))

        self.hitbox = (self.x, self.y, 40, 35)
        pg.draw.rect(screen, (255, 0, 255), self.hitbox, 2)

class NPC(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        win.blit(npcSurf, (self.x, self.y))

    def move(self):
        if self.x > 2 and self.x < 850:
            self.x += random.choice(npcMoveLst)
        if self.x > 2:
            self.x += abs(random.choice(npcMoveLst))
        elif self.x <= 2:
            self.x = 25
        if self.x < 850:
            self.x = abs(random.choice(npcMoveLst))
        elif self.x >= 850:
            self.x = 25
        if self.y > 2 and self.y < 550:
            self.y += random.choice(npcMoveLst)
        if self.y > 2:
            self.y += abs(random.choice(npcMoveLst))
        elif self.y <= 2:
            self.y = 25
        if self.y < 550:
            self.y -= abs(random.choice(npcMoveLst))
        elif self.y >= 550:
            self.y = 25

    def hit(self):
        print('hit')

def createNPC():
    i = 0
    npcRect = npcSurf.get_rect(center=(npcx[i], npcy[i]))
    i += 1
    return npcRect


def drawNPC(lst):
    for npc in lst:
        screen.blit(npcSurf, npc)
    pg.display.update()


def moveNPC(npcs, lst):
    for npc in npcs:
        if npc.centerx > 2 and npc.centerx < 850:
            npc.centerx += random.choice(lst)
        if npc.centerx > 2:
            npc.centerx += abs(random.choice(lst))
        elif npc.centerx <= 2:
            npc.centerx = 25
        if npc.centerx < 850:
            npc.centerx = abs(random.choice(lst))
        elif npc.centerx >= 850:
            npc.centerx = 25
        if npc.centery > 2 and npc.centery < 550:
            npc.centery += random.choice(lst)
        if npc.centery > 2:
            npc.centery += abs(random.choice(lst))
        elif npc.centery <= 2:
            npc.centery = 25
        if npc.centery < 550:
            npc.centery -= abs(random.choice(lst))
        elif npc.centery >= 550:
            npc.centery = 25
    return npcs
# Redraw/update the entire canvas
def redraw(lst):
    screen.blit(bgSurface, (0, 0))
    player.draw(screen)
    drawNPC(lst)
    for bullet in bullets:
        bullet.draw(screen)
    for buil in buildingCoord:
        screen.blit(buildSurf, buil)
    gameStatusLable = mainFont.render(f"Game Status: {gameStatus}", 1, (150, 5, 150), )
    screen.blit(gameStatusLable, (10, 10))
    pg.display.update()




def resetGame(x, y, lst):
    x, y = 0, 0
    lst.clear()
    return x, y, lst


def checkHit(lstNpc):
    for bullet in bullets:
        for npc in lstNpc:# Don't forget this part of the code
            if bullet.collide(npc):
                npc = pg.image.load('Game Sprites/masked.png')
                return npc
            else:
                return npc


def checkColl(build, speed):
    for wall in build:
        if playerRect.colliderect(wall):
            return -speed

def createWallLst(horizLst, vertLst):
    for horiz in horizLst:
        wallLst.append(horiz)
    for vert in vertLst:
        wallLst.append(vert)
    return wallLst

def buildings(rectLst):
    for rect in rectLst:
        print(rect)
        x, y, w, h = rect
        rect = buildSurf.get_rect(topleft=(x, y))
        buildingRects.extend(rect)
    return buildingRects




# Player Defaults
px, py = screenWidth/2, screenHeight/2
spd = 5

# Create a player
player = char(px, py, 32, 32, spd)

# Walls
wallLst = []
vertWallSurf = pg.image.load('Game Sprites/verticalWall.png').convert_alpha()
vertwallSurf = pg.transform.scale2x(vertWallSurf)
vertRect = vertwallSurf.get_rect()

horizWallSurf = pg.image.load('Game Sprites/horizontalWall.png').convert_alpha()
horizWallSurf = pg.transform.scale2x(horizWallSurf)
horizRect = horizWallSurf.get_rect()

# Buildings
buildSurf = pg.image.load('Game Sprites/buildingTop.png').convert()
buildingCoords = [(0, 78, 177, 277), (260, 79, 441, 279), (521, 80, 698, 277), (782, 79, 958, 279), (0, 360, 180, 560), (260, 359, 441, 560), (520, 361, 700, 558), (780, 358, 956, 556)]
buildingCoord = [(0, 78), (260, 79), (521, 80), (782, 79), (0, 360), (260, 359), (520, 361), (780, 358)]
buildingRects = []

buildings(buildingCoords)
print(buildingRects)

# NPC Defaults
npcSurf = pg.image.load('Game Sprites/unmasked.png').convert_alpha()
npcSurf = pg.transform.scale2x(npcSurf)
npcRect = npcSurf.get_rect()
print(npcSurf.get_rect())
npcx = [200, 350, 500]
npcy = [200, 350, 500]
npcMoveLst = [10, 20, 30, -10, -20, -30]# These are the different distances the NPC can move
npcDelayLst = [250, 500, 750, 1000]# These are the times in between each movement(in milliseconds)
npcLst = []# This creates a list to store all NPCs in
NPCDRAW = pg.USEREVENT
SPAWNNPC = pg.USEREVENT# This creates an event type called SPAWNNPC
pg.time.set_timer(SPAWNNPC, random.choice(npcDelayLst))# This sets a timer that delays the spawning of npcs for a random amount of time
pg.time.set_timer(NPCDRAW, random.choice(npcDelayLst))


# Bullets
bullet = projectile

bullets = []
shootLoop = 0
bulletSpd = 10
# bulletRect = (bullet.x, bullet.y, bullet.width, bullet.height)


onetick = 20
delay = 1
# Main Loop

while True:
    pg.time.delay(delay)
    clock.tick(onetick)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    mainFont = pg.font.SysFont('comicsans', 50)# Creates the font variable
    for event in pg.event.get():# Checks for events
        if event.type == pg.QUIT:# If x is clicked, exit game
            pg.quit()
            exit()

        if len(npcLst) <= 2:
            if event.type == SPAWNNPC:# If the timer goes off, create an NPC
                npcLst.append(createNPC())
        if event.type == NPCDRAW:
            npcLst = moveNPC(npcLst, npcMoveLst)  # Moves all of the npcs at the same time
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            print(pos)


    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0 and bullet.y > 0 and bullet.y < screenHeight:
            bullet.x += spdx
            bullet.y += spdy
            pg.draw.rect(screen, (0, 255, 0), bullet.hitbox, 2)
        else:
            bullets.pop(bullets.index(bullet))

    # checkHit(npcLst)


    keys = pg.key.get_pressed()# If one of the arrow keys are pressed, move in that direction

    if keys[pg.K_LEFT] and gameStatus and player.x > player.spd:
        player.x -= spd
        checkColl(wallLst, spd)
        isLeft = True
        isUp = isRight = isDown = False
    if keys[pg.K_UP] and gameStatus and player.y > player.spd:
        player.y -= spd
        isUp = True
        isLeft = isRight = isDown = False
    if keys[pg.K_RIGHT] and gameStatus and player.x < screenWidth - player.width - spd:
        player.x += spd
        isRight = True
        isUp = isLeft = isDown = False
    if keys[pg.K_DOWN] and gameStatus and player.y < screenHeight - player.height - spd:
        player.y += spd
        isDown = True
        isUp = isRight = isLeft = False
    if keys[pg.K_SPACE] and gameStatus and shootLoop == 0:# if event.key == pg.K_SPACE and gameStatus:# If the space bar is pressed and the game is active, sho0t a mask
        if isDown:
            spdx = 0
            spdy = bulletSpd
        if isUp:
            spdx = 0
            spdy = -1 * bulletSpd
        if isLeft:
            spdx = -1 * bulletSpd
            spdy = 0
        if isRight:
            spdx = bulletSpd
            spdy = 0
        if len(bullets) < 100:
            bullets.append(projectile(round(player.x + player.width//2),round(player.y + player.height//2), spdx, spdy))
    if keys[pg.K_BACKSPACE] and not gameStatus:  # If the spacebar is pressed and the game isn't active, restart
        gameStatus = True
        px, py, npcLst = resetGame(px, py, npcLst)
    if keys[pg.K_BACKSPACE] and gameStatus:
        gameStatus = False
    # if pg.mouse.get_pressed():
    #     print(pg.mouse.get_pos())


    redraw(npcLst)



