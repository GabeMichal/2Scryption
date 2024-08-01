from Scrypt_card import *
from Scrypt_map import *
from Scrypt_player import *
#from Scrypt_events import *
from scryptnetwork import Network
import pygame
import os
import random
import sys

WIN = pygame.display.set_mode((480*dimension, 300*dimension))
pygame.display.set_caption("Inscryption Card Test")


pygame.font.init()
pygame.mouse.set_visible(False)
font = pygame.font.Font("Scrypt_Font.ttf", 10)

def hoverDesc(hovered):
    cardname = font.render(hovered.name, False, (0,0,0))
    namesize = cardname.get_size()
    WIN.blit(pygame.transform.scale(cardname, (namesize[0]*dimension, namesize[1]*dimension)), (337*dimension,48*dimension))
    cardtribe = font.render(hovered.tribe, False, (0,0,0))
    if hovered.tribe == "N/A":
        cardtribe = font.render("NONE", False, (0,0,0))
    tribesize = cardtribe.get_size()
    WIN.blit(pygame.transform.scale(cardtribe, (tribesize[0]*dimension, tribesize[1]*dimension)), (337*dimension,65*dimension))
    WIN.blit(pyload("Scryption_Display/InCosts/"+hovered.cost+".png"), (404*dimension,41*dimension))
    for n in range(len(hovered.sigils+hovered.sigils2)):
        if n >= len(hovered.sigils):
            thisSigil = sigilSpriteB[sigilList.index((hovered.sigils+hovered.sigils2)[n])]
        else:
            thisSigil = sigilSprite[sigilList.index((hovered.sigils+hovered.sigils2)[n])]
        if n < 5:
            ny = 82
        else:
            ny = 104
        nx = 337+22*(n%5)
        nPos = (nx*dimension, ny*dimension)
        sigilSize = thisSigil.get_size()
        WIN.blit(pygame.transform.scale(thisSigil, (sigilSize[0]*dimension, sigilSize[1]*dimension)), nPos)
    if hovered.sigilTem != 0:
        n = len(hovered.sigils+hovered.sigils2)
        if n < 5:
            ny = 82
        else:
            ny = 104
        nx = 337+22*(n%5)
        nPos = (nx*dimension, ny*dimension)
        thisSigil = sigilSpriteO[sigilList.index(hovered.sigilTem)]
        sigilSize = thisSigil.get_size()
        WIN.blit(pygame.transform.scale(thisSigil, (sigilSize[0]*dimension, sigilSize[1]*dimension)), nPos)

def menu1():
    global dimension
    global WIN
    clock = pygame.time.Clock()
    counter = 0
    clicked = False
    while True:
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Main_Menu/WeegiModLogo.png"), (0,0))
        if counter >= 40:
            counter = 0
        if hovCheck("rect", [(0,165),(480,10)], mousePos):
            counter+=1
            if counter <= 20:
                WIN.blit(pyload("Scryption_Display/Main_Menu/START_GAME.png"), (0,0))
        elif hovCheck("rect", [(0,187),(480,10)], mousePos):
            counter+=1
            if counter <= 20:
                WIN.blit(pyload("Scryption_Display/Main_Menu/OPTIONS.png"), (0,0))
        elif hovCheck("rect", [(0,209),(480,10)], mousePos):
            counter+=1
            if counter <= 20:
                WIN.blit(pyload("Scryption_Display/Main_Menu/EXIT_GAME.png"), (0,0))
        else:
            counter = 0
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    if hovCheck("rect", [(0,209),(480,10)], mousePos):
                        return 0
                    if hovCheck("rect", [(0,165),(480,10)], mousePos):
                        return 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
                elif event.key > 48 and event.key < 58:
                    dimension = event.key-48
                    WIN = pygame.display.set_mode((480*dimension, 300*dimension))
        WIN.blit(pyload("Scryption_Display/Overlay.png"), (0,0))
        pygame.display.update()

def menu2():
    global dimension
    global WIN
    clock = pygame.time.Clock()
    counter = 0
    counter2 = 0
    clicked = True
    startDeckOpts = [[create_card("Stoat"), create_card("Bullfrog"), create_card("Wolf")], [create_card("Black Goat"), create_card("Moose Buck"), create_card("Mole")],
                     [create_card("Ant Queen"), create_card("Flying Ant"), create_card("Skunk")], [create_card("Mantis God"), create_card("Ring Worm"), create_card("Ring Worm")],
                     [create_card("Kingfisher"), create_card("Kingfisher"), create_card("Great Kraken")], [create_card("Racoon"), create_card("Dire Wolf Pup"), create_card("Coyote")],
                     [create_card("Rabbit"), create_card("Tadpole"), create_card("Geck")], [create_card("Curious Egg"), create_card("Curious Egg"), create_card("Curious Egg")]]
    deckOpts2 = ["Vanilla", "Cost", "Ant", "Mantis", "Swim", "Bone", "Free", "Egg"]
    currDeck = startDeckOpts[0]
    while True:
        selecting = False
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Main_Menu/KayceeModStarter.png"), (0,0))
        counter2 += 1
        counter += 1
        if counter >= 40:
            counter = 0
        for n in range(8):
            if hovCheck("rect", [(75+((n%4)*86),82+(int(n/4)*53)),(73,48)], mousePos):
                selecting = True
                currDeck = startDeckOpts[n]
                if counter <= 20:
                    WIN.blit(pyload("Scryption_Display/Main_Menu/"+deckOpts2[n]+".png"),(0,0))
        if hovCheck("rect", [(20,25),(20,20)], mousePos):
            if counter <= 20:
                WIN.blit(pyload("Scryption_Display/Main_Menu/X.png"), (0,0))
        elif hovCheck("rect", [(440,25),(20,20)], mousePos):
            if counter <= 20:
                WIN.blit(pyload("Scryption_Display/Main_Menu/Random.png"), (0,0))
        elif selecting == False:
            counter = 0
        for n in range(3):
            cardPos = ((169+(n*50)),221)
            currDeck[n].show_image(dimension, cardPos, 0, WIN, counter2, 44, 0)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(8):
                        if hovCheck("rect", [(75+((n%4)*86),82+(int(n/4)*53)),(73,48)], mousePos):
                            currDeck.append(create_card("Rabbit Pelt"))
                            currDeck.append(create_card("Rabbit Pelt"))
                            return currDeck
                    if hovCheck("rect", [(440,25),(20,20)], mousePos):
                        currDeck = random.choice(startDeckOpts)
                        currDeck.append(create_card("Rabbit Pelt"))
                        currDeck.append(create_card("Rabbit Pelt"))
                        return currDeck
                    if hovCheck("rect", [(20,25),(20,20)], mousePos):
                        return 1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 1
        WIN.blit(pyload("Scryption_Display/Overlay.png"), (0,0))
        pygame.display.update()

def mainScreen(net):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    hovered = 0
    mousePos = pygame.mouse.get_pos()
    g = net.send((mousePos, pygame.key.get_pressed(), False))
    #print("Received:", g)
    while True:
        p = g.players[net.pNum]
        p2 = g.players[1-net.pNum]
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        keys = pygame.key.get_pressed()
        clickDown = False
        WIN.fill((0,0,0))
        # All pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    clickDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
        if g.screen == "overworld":
            for n in range(5):
                if 4-n < len(g.map[0].trans):
                    WIN.blit(pyload("Scryption_Display/InPaths/"+g.map[0].trans[4-n]+".png"), (0,60*(n-4)*dimension))
            p2.draw(WIN)
            p.draw(WIN)
            for n in range(5):
                if 4-n < len(g.map[0].trans):
                    WIN.blit(pyload("Scryption_Display/InTrees/"+g.map[0].trans[4-n]+".png"),(0,60*(n-4)*dimension))
            for n in range(5):
                if 4-n < len(g.map[0].spots):
                    spotLen = len(g.map[0].spots[4-n])
                    for m in range(spotLen):
                        if spotLen == 1:
                            mPos = (225,60*(n+1)-15)
                        elif spotLen == 2:
                            mPos = (185+80*m,60*(n+1)-15)
                        elif spotLen == 3:
                            mPos = (145+80*m,60*(n+1)-15)
                        else:
                            mPos = (105+80*m, 60*(n+1)-15)
                        if "Boss" in g.map[0].spots[4-n][m]:
                            mPos = (mPos[0]-28, mPos[1]-16)
                        mPos = (mPos[0]*dimension, mPos[1]*dimension)
                        try:
                            WIN.blit(pyload("Scryption_Display/MapIcons/"+g.map[0].spots[4-n][m]+".png"), mPos)
                        except FileNotFoundError:
                            a=0
        else:
            WIN.blit(pyload("Scryption_Display/Background.png"), (0,0))
            if g.screen in ["battle", "trial", "goob", "stones", "item", "bone", "myco"] or "Boss" in g.screen:
                WIN.blit(pyload("Scryption_Display/Events/"+g.screen+".png"), (0,0))
            elif g.screen == "battleswap":
                WIN.blit(pyload("Scryption_Display/Events/battle.png"), (0,0))
            # Display totem and items
            if 0 not in p.totem:
                WIN.blit(pyload("Scryption_Display/InTotems/"+p.totem[0]+".png"),(334*dimension,131*dimension))
                WIN.blit(pyload("Scryption_Display/InTotems/Base.png"),(334*dimension,131*dimension))
                thisSigil = sigilSpriteO[sigilList.index(p.totem[1])]
                sigilSize = thisSigil.get_size()
                sigilImage = pygame.transform.scale(thisSigil, (sigilSize[0]*dimension, sigilSize[1]*dimension))
                WIN.blit(sigilImage,(338*dimension,158*dimension))
            for n in range(3):
                if p.items[n] != 0:
                    WIN.blit(pyload("Scryption_Display/InItems/"+"_".join(p.items[n].split())+".png"), ((362+28*n)*dimension, 131*dimension))
                    if hovCheck("rect", [(360+26*n,131),(25,50)], mousePos):
                        WIN.blit(pyload("Scryption_Display/HovItems/"+"_".join(p.items[n].split())+".png"), ((362+28*n)*dimension, 131*dimension))
            # Display whatever's needed for the screen
            hovered = g.moment(net.pNum, hovered, counter, WIN)
            # Display description of card
            if hovered != 0:
                hoverDesc(hovered)
        WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), p2.mousePos)
        if p.cursorMode == "sacrifice":
            if clicked:
                WIN.blit(pyload("Scryption_Display/Cursor/sacrifice_click.png"), (mousePos[0]-5*dimension, mousePos[1]-15*dimension))
            else:
                WIN.blit(pyload("Scryption_Display/Cursor/sacrifice.png"), (mousePos[0]-5*dimension, mousePos[1]-19*dimension))
        else:
            if clicked:
                WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), (mousePos[0]+dimension, mousePos[1]+2*dimension))
            else:
                WIN.blit(pyload("Scryption_Display/Cursor/normal.png"), mousePos)
        WIN.blit(pyload("Scryption_Display/Overlay.png"), (0,0))
        pygame.display.update()
        g = net.send((mousePos, keys, clickDown))

def battleScreen(currDeck):
    net = Network()
    p = net.getP()
    p.deck = currDeck
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    p.totem = ["Canine", random.choice(sigilList)]
    p.items = random.sample(itemList,3)
    hovered = 0
    while True:
        counter += 1
        clock.tick(60)
        p2 = net.send(p)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background.png",dimension), (0,0))
        cardPos = []
        if len(p.deck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(p.deck)-1)+2
        for n in range(4):
            if p.board[n] != 0:
                nPos = (150+(n*44),137)
                if p.board[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = p.board[n]
            if p2.board[3-n] != 0:
                nPos = (150+(n*44),74)
                if p2.board[3-n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = p2.board[3-n]
        for n in range(len(p.deck)):
            if p.deck[n].tribe == p.totem[0]:
                p.deck[n].sigilTem = p.totem[1]
            n_x = 240+cardSep*(n-len(p.deck)/2)
            cardPos.append((n_x,215))
            if n == len(p.deck)-1:
                cardSep = 44
            if p.deck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = p.deck[n]
        # Display totem and items
        if len(p.totem) == 2:
            WIN.blit(pyload("Scryption_Display/InTotems/"+p.totem[0]+".png",dimension),(334*dimension,131*dimension))
            WIN.blit(pyload("Scryption_Display/InTotems/Base.png",dimension),(334*dimension,131*dimension))
            thisSigil = sigilSpriteO[sigilList.index(p.totem[1])]
            sigilSize = thisSigil.get_size()
            sigilImage = pygame.transform.scale(thisSigil, (sigilSize[0]*dimension, sigilSize[1]*dimension))
            WIN.blit(sigilImage,(338*dimension,158*dimension))
        for n in range(3):
            if p.items[n] != 0:
                WIN.blit(pyload("Scryption_Display/InItems/"+p.items[n]+".png",dimension), ((360+26*n)*dimension, 131*dimension))
        # Display description of card
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        # All other events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    # Check for clicks
                    for n in range(len(p.deck)):
                        if n >= len(p.deck):
                            break
                        if p.deck[n].selected:
                            p.deck[n].selected = False
                            for m in range(4):
                                if hovCheck("rect", [(150+m*44,137),(44,56)]):
                                    p.board[m] = p.deck[n]
                                    p.deck.pop(n)
                        else:
                            if len(p.deck) < 9 or n == len(p.deck)-1:
                                cardSep = 44
                            else:
                                cardSep = 332/(len(p.deck)-1)+2
                            n_cp = (240+cardSep*(n-len(p.deck)/2),215)
                            if hovCheck("rect",[n_cp,(cardSep,58)]):
                                p.deck[n].selected = True
                                p.deck[n].counter = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def stonesScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    selfStones = [0,0]
    hovered = 0
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background2.png",dimension), (0,0))
        cardPos = []
        # cardSep stays consistent no matter the dimensions
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = (332/(len(currDeck)-1)+2)
        for n in range(2):
            if selfStones[n] != 0:
                nPos = ((215-7*n),(59+74*n))
                if selfStones[n].show_image(dimension, nPos, n, WIN, counter, 44, 1):
                    hovered = selfStones[n]
        if selfStones[0] != 0 and selfStones[1] != 0:
            WIN.blit(pyload("Scryption_Display/Buttons/Stones.png",dimension),(0,0))
            if hovCheck("ellipse", [(240,245),(64,24)]):
                WIN.blit(pyload("Scryption_Display/Buttons/StonePress.png",dimension),(0,0))
        else:
            for n in range(len(currDeck)):
                n_x = (240+cardSep*(n-len(currDeck)/2))
                cardPos.append((n_x,215))
                if n == len(currDeck)-1:
                    cardSep = 44
                if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                    hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for m in range(2):
                        if hovCheck("rect", [(215-7*m,59+74*m),(44+14*m,58-14*m)]):
                            if selfStones[m] != 0:
                                currDeck.append(selfStones[m])
                                selfStones[m] = 0
                            else:
                                for n in range(len(currDeck)):
                                    if n >= len(currDeck):
                                        break
                                    if currDeck[n].selected == True:
                                        currDeck[n].selected = False
                                        selfStones[m] = currDeck[n]
                                        currDeck.pop(n)
                    if selfStones[0] == 0 or selfStones[1] == 0:
                        for n in range(len(currDeck)):
                            if n >= len(currDeck):
                                break
                            if len(currDeck) < 9 or n == len(currDeck)-1:
                                cardSep = 44
                            else:
                                cardSep = 332/(len(currDeck)-1)+2
                            n_cp = (240+cardSep*(n-len(currDeck)/2),215)
                            if currDeck[n].selected == True:
                                currDeck[n].selected = False
                            elif hovCheck("rect", [n_cp, (cardSep, 58)]):
                                currDeck[n].selected = True
                                currDeck[n].counter = 0
                    else:
                        if hovCheck("ellipse", [(240,245),(64,24)]):
                            selfStones[0].sigils2 = selfStones[1].sigils
                            selfStones[1] = 0
                            currDeck.append(selfStones[0])
                            selfStones[0] = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def fireScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    firing = 0
    hovered = 0
    survivors = get_cardlist("deathcards", 5)
    for n in range(5):
        survivors[n].cost = "0N"
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background3.png",dimension), (0,0))
        cardPos = []
        # cardSep stays consistent no matter the dimensions
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = (332/(len(currDeck)-1)+2)
        if firing != 0:
            firPos = (216,112)
            if firing.show_image(dimension, firPos, 0, WIN, counter, 44, 1):
                hovered = firing
        for n in range(5):
            nPos = (int(68*math.sin(0.29*n*math.pi-math.pi*0.58)+216),int(-68*math.cos(0.29*n*math.pi-math.pi*0.58)+110))
            survivors[n].show_image(dimension, nPos, 0, WIN, counter, 44, 0)
        if firing != 0:
            WIN.blit(pyload("Scryption_Display/Buttons/Fire.png",dimension),(0,0))
            if hovCheck("ellipse", [(240,245),(64,24)]):
                WIN.blit(pyload("Scryption_Display/Buttons/FirePress.png",dimension),(0,0))
        else:
            for n in range(len(currDeck)):
                n_x = (240+cardSep*(n-len(currDeck)/2))
                cardPos.append((n_x,215))
                if n == len(currDeck)-1:
                    cardSep = 44
                if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                    hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    if hovCheck("rect", [(216,111),(44,58)]):
                        if firing != 0:
                            currDeck.append(firing)
                            firing = 0
                        else:
                            for n in range(len(currDeck)):
                                if n >= len(currDeck):
                                    break
                                if currDeck[n].selected == True:
                                    currDeck[n].selected = False
                                    firing = currDeck[n]
                                    currDeck.pop(n)
                    if firing == 0:
                        for n in range(len(currDeck)):
                            if n >= len(currDeck):
                                break
                            if len(currDeck) < 9 or n == len(currDeck)-1:
                                cardSep = 44
                            else:
                                cardSep = 332/(len(currDeck)-1)+2
                            n_cp = (240+cardSep*(n-len(currDeck)/2),215)
                            if currDeck[n].selected == True:
                                currDeck[n].selected = False
                            elif hovCheck("rect", [n_cp, (cardSep,58)]):
                                currDeck[n].selected = True
                                currDeck[n].counter = 0
                    elif hovCheck("ellipse", [(240,245),(64,24)]):
                        firing.power += 1
                        currDeck.append(firing)
                        firing = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def tradeScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    trades = get_cardlist("common", 8)
    hovered = 0
    while True:
        peltcount = 0
        for n in currDeck:
            if n.name == "Rabbit Pelt":
                peltcount+=1
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(8):
            if trades[n] != 0:
                nPos = ((150+(n%4)*44),(73+int(n/4)*64))
                if trades[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = trades[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(8):
                        if hovCheck("rect", [(150+(n%4)*44,73+int(n/4)*64),(44,58)]) and trades[n] != 0 and peltcount > 0:
                            currDeck.append(trades[n])
                            trades[n] = 0
                            for m in range(len(currDeck)):
                                if currDeck[m].name == "Rabbit Pelt":
                                    currDeck.pop(m)
                                    break
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def trapScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    selfTeeth = 100
    peltOpts = [create_card("Rabbit Pelt"),create_card("Wolf Pelt"),create_card("Golden Pelt")]
    hovered = 0
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(3):
            nPos = (194+n*44,138)
            if peltOpts[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = peltOpts[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(3):
                        if 2*n <= selfTeeth:
                            if hovCheck("rect", [(194+n*44,138),(44,58)]):
                                currDeck.append(create_card(peltOpts[n].name))
                                selfTeeth-=2*n
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def choiceCScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    costOpts = random.sample(["cost1", "cost2", "cost3", "costb"], 3)
    costOpts.sort()
    cardOpts = []
    hovered = 0
    for n in range(3):
        cardOpts.append(get_cardlist(costOpts[n], 1)[0])
    cardDisg = get_cardlist("deathcards", 3)
    for n in range(3):
        cardDisg[n].tribe = "XXX"
        cardDisg[n].sigils = []
        cardDisg[n].cost = cardOpts[n].cost
        if cardOpts[n].cost[-1] == "N":
            cardDisg[n].cost = "XN"
        cardDisg[n].health = "x"
        cardDisg[n].power = "x"
        cardDisg[n].name = "XXX"
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(3):
            if cardDisg[n] != 0:
                nPos = ((194+n*44),138)
                if cardDisg[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = cardDisg[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(3):
                        if hovCheck("rect", [(194+n*44,138),(44,58)]) and cardOpts[n] != 0:
                            currDeck.append(cardOpts[n])
                            cardDisg[n] = 0
                            cardOpts[n] = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def choiceDScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    clicked = True
    cardOpts = get_cardlist("common", 3)
    hovered = 0
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(3):
            if cardOpts[n] != 0:
                nPos = (194+n*44,138)
                if cardOpts[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = cardOpts[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(3):
                        if hovCheck("rect", [(194+n*44,138),(44,58)]) and cardOpts[n] != 0:
                            currDeck.append(cardOpts[n])
                            cardOpts[n] = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def choiceTScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    hovered = 0
    clicked = True
    tribOpts = random.sample(["reptiles", "insects", "canines", "avians", "hooved"], 3)
    cardOpts = []
    for n in range(3):
        cardOpts.append(get_cardlist(tribOpts[n], 1)[0])
    cardDisg = get_cardlist("deathcards", 3)
    for n in range(3):
        cardDisg[n].sigils = []
        cardDisg[n].cost = "0N"
        cardDisg[n].health = "x"
        cardDisg[n].power = "x"
        cardDisg[n].name = "XXX"
        cardDisg[n].tribe = cardOpts[n].tribe
        # Eventually change to portraits representing the tribe
        cardDisg[n].portrait = cardDisg[n].tribe
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(3):
            if cardDisg[n] != 0:
                nPos = (194+n*44,138)
                if cardDisg[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = cardDisg[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(3):
                        if hovCheck("rect",[(194+n*44,138),(44,58)]) and cardOpts[n] != 0:
                            currDeck.append(cardOpts[n])
                            cardDisg[n] = 0
                            cardOpts[n] = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def prospectScreen(currDeck):
    clock = pygame.time.Clock()
    counter = 0
    hovered = 0
    clicked = True
    cardOpts = get_cardlist("insects", 2)
    for n in range(2):
        cardOpts[n].sigils2 = [random.choice(sigilList2)]
    cardOpts.append(create_card("Golden Pelt"))
    random.shuffle(cardOpts)
    boulders = [create_card("Boulder"), create_card("Boulder"), create_card("Boulder")]
    while True:
        counter += 1
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        WIN.blit(pyload("Scryption_Display/Background4.png",dimension), (0,0))
        cardPos = []
        if len(currDeck) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(currDeck)-1)+2
        for n in range(3):
            nPos = (194+n*44,138)
            if boulders[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = boulders[n]
        for n in range(len(currDeck)):
            n_x = 240+cardSep*(n-len(currDeck)/2)
            cardPos.append((n_x,215))
            if n == len(currDeck)-1:
                cardSep = 44
            if currDeck[n].show_image(dimension, cardPos[n], 0, WIN, counter, cardSep, 1):
                hovered = currDeck[n]
        if hovered != 0:
            hoverDesc(hovered)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (mousePos[0]-dimension, mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for n in range(3):
                        if hovCheck("rect", [(194+n*44,138),(44,58)]):
                            boulders[n] = cardOpts[n]
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return 0
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension), (0,0))
        pygame.display.update()

def owScreen():
    net = Network()
    p = net.getP()
    clock = pygame.time.Clock()
    currMap = allMaps[0]
    clicked = True
    speed = dimension
    while True:
        clock.tick(60)
        mousePos = pygame.mouse.get_pos()
        mousePos2 = (int(mousePos[0]/dimension), int(mousePos[1]/dimension))
        mousePos = (mousePos2[0]*dimension,mousePos2[1]*dimension)
        p2 = net.send(p)
        p.move()
        WIN.fill((0,0,0))
        for n in range(5):
            WIN.blit(pyload("Scryption_Display/InPaths/"+currMap.trans[4-n]+".png", dimension), (0,60*(n-4)*dimension))
        p2.draw(WIN)
        p.draw(WIN)
        WIN.blit(pyload("Scryption_Display/Cursor.png",dimension),p2.mousePos)
        if clicked == True:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), (p.mousePos[0]-dimension, p.mousePos[1]-dimension))
        else:
            WIN.blit(pyload("Scryption_Display/Cursor.png",dimension), p.mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # ESC
                    return -1
                if event.key > 47 and event.key < 58:
                    return event.key-48
        WIN.blit(pyload("Scryption_Display/Overlay.png",dimension),(0,0))
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    mousePos = (300, 100)
    clicked = False
    # Counter for main menu or whatever
    counter = 0
    scene2 = 1
    scene = 8
    startDeckOpts = [[create_card("Stoat"), create_card("Bullfrog"), create_card("Wolf")], [create_card("Black Goat"), create_card("Moose Buck"), create_card("Mole")],
                     [create_card("Ant Queen"), create_card("Flying Ant"), create_card("Skunk")], [create_card("Mantis God"), create_card("Ring Worm"), create_card("Ring Worm")],
                     [create_card("Kingfisher"), create_card("Kingfisher"), create_card("Great Kraken")], [create_card("Racoon"), create_card("Dire Wolf Pup"), create_card("Coyote")],
                     [create_card("Rabbit"), create_card("Tadpole"), create_card("Geck")], [create_card("Curious Egg"), create_card("Curious Egg"), create_card("Curious Egg")]]
    selfBoard = [0,0,0,0]
    currDeck = startDeckOpts[0]
    while run:
        clock.tick(60)
        mousePos2 = pygame.mouse.get_pos()
        if scene2 == 1:
            if menu1() == 1:
                scene2 = 2
            else:
                run = False
        elif scene2 == 2:
            deckmenu = menu2()
            if deckmenu == 0:
                run = False
            elif deckmenu == 1:
                scene2 = 1
            else:
                net = Network(deckmenu)
                g = net.send((mousePos, pygame.key.get_pressed(), False))
                while not g:
                    print("Reloading...")
                    net = Network(deckmenu)
                    g = net.send((mousePos, pygame.key.get_pressed(), False))
                scene = ""
                scene2 = 0
        elif scene == 0:
            currDeck = battleScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 1:
            currDeck = stonesScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 2:
            currDeck = fireScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 3:
            currDeck = tradeScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 4:
            currDeck = trapScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 5:
            currDeck = choiceCScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 6:
            currDeck = choiceDScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 7:
            currDeck = choiceTScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 8:
            currDeck = prospectScreen(currDeck)
            if currDeck == 0:
                run = False
        elif scene == 9:
            currDeck = mainScreen(net)
            if currDeck == 0:
                run = False
        elif scene == 10:
            check = owScreen()
            print(check)
            if check == -1:
                run = False
            else:
                scene = check
        else:
            currDeck = mainScreen(net)
            if currDeck == 0:
                run = False
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
