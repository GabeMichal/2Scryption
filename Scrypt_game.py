from Scrypt_player import Player
from Scrypt_pygame import mainScreen
from Scrypt_card import *
from Scrypt_comms import attack
from Scrypt_map import allMaps

tempScreen = "overworld"

class Game():
    def __init__(self, p1, p2):
        self.players = [p1, p2]
        self.map = allMaps
        self.screen = tempScreen
        self.knifeBought = False
        self.setDefault()
        self.survsDead = 0
        self.movers = []
        self.switch = 0

    def moment(self, p, hovered, counter, win):
        scr = self.screen
        if scr in ["battle", "battleswap"] or "Boss" in scr:
            hovered = self.battleMoment(p, hovered, counter, win)
        else:
            # Show the player's deck if it's there
            if self.players[p].deckShow:
                z = self.players[p].cards
                for k in range(len(z)):
                    if len(z) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332/(len(z)-1)+2
                    cardPos = (240+cardSep*(k-len(z)/2),215)
                    if k == len(z)-1:
                        cardSep = 44
                    if z[k].show_image(dimension,cardPos,0,win,counter,cardSep, 1):
                        hovered = z[k]
            # Show 0 bones, 0 lengths
            renderFont("0", (66, 67), win)
            renderFont(str(len(self.players[p].cards)), (372, 199), win)
            renderFont("10", (420, 199), win)
            # Show the neutral scales
            win.blit(pyload("Scryption_Display/Scales/scale0.png"),(48*dimension,116*dimension))
            if scr == "stones":
                hovered = self.stoneMoment(p, hovered, counter, win)
            elif scr == "fire":
                hovered = self.fireMoment(p, hovered, counter, win)
            elif scr == "trader":
                hovered = self.tradeMoment(p, hovered, counter, win)
            elif scr == "trapper":
                hovered = self.trapMoment(p, hovered, counter, win)
            elif scr in ["choose", "rarech"]:
                hovered = self.cardMoment(p, hovered, counter, win)
            elif scr in ["costch", "tribch", "rocky"]:
                hovered = self.cardSecMoment(p, hovered, counter, win)
            elif scr == "item":
                hovered = self.itemMoment(p, hovered, counter, win)
            elif scr == "bone":
                hovered = self.boneMoment(p, hovered, counter, win)
            elif scr == "totem":
                hovered = self.toteMoment(p, hovered, counter, win)
            elif scr == "myco":
                hovered = self.mycoMoment(p, hovered, counter, win)
            elif scr == "goob":
                hovered = self.goobMoment(p, hovered, counter, win)
            elif scr == "trial":
                hovered = self.trialMoment(p, hovered, counter, win)
        # Show rulebook
        win.blit(pyload("Scryption_Display/bookButton.png"), (69*dimension,188*dimension))
        self.players[p].show_rules(win)
        if not self.players[p].myTurn:
            win.blit(pyload("Scryption_Display/notMyTurn.png"), (0,0))
        return hovered

    def getClick(self, player):
        scr = self.screen
        p = self.players[player]
        turn = False
        # Click events
        if hovCheck("rect", [(69, 188), (27, 19)], p.mousePos):
            p.ruleb = 0
        if not p.myTurn:
            turn = False
        elif scr in ["battle", "battleswap"] or "Boss" in scr:
            if p.screenVer == "hoard" and self.hoardClick(p):
                p.screenVer = ""
            elif "cut" in p.screenVer and self.cutClick(p, self.players[1-player]):
                p.screenVer = ""
            elif self.battleClick(p, self.players[1-player]):
                turn = True
                if self.players[player].playerNum:
                    for k in range(2):
                        if not self.players[k].playerNum:
                            self.players[k].x = self.players[1-k].x
                        self.players[k].playerNum = 1-self.players[k].playerNum
                    self.switch = 1
                if "Boss" in scr:
                    turn = False
                    self.screen = "rarech"
        elif scr == "stones" and self.stoneClick(p):
            turn = True
        elif scr == "fire" and self.fireClick(p):
            turn = True
        elif scr == "trader" and self.tradeClick(p):
            turn = True
        elif scr == "trapper" and self.trapClick(p):
            turn = True
        elif scr in ["choose", "rarech"] and self.cardClick(p):
            turn = True
        elif scr in ["costch", "tribch", "rocky"] and self.cardSecClick(p):
            turn = True
        elif scr == "item" and self.itemClick(p, self.players[1-player]):
            turn = True
        elif scr == "bone" and self.boneClick(p):
            turn = True
        elif scr == "totem" and self.toteClick(p):
            turn = True
        elif scr == "myco" and self.mycoClick(p):
            turn = True
        elif scr == "goob" and self.goobClick(p):
            turn = True
        elif scr == "trial" and self.trialClick(p):
            turn = True
        if turn:
            self.screen = tempScreen
            self.setDefault()
            self.map[0].trans.pop(0)
            self.map[0].segs.pop(0)
            self.map[0].spots.pop(0)
            for k in range(2):
                self.players[k].y = 300

    def battleMoment(self, p, hovered, counter, WIN):
        p2 = self.players[1-p]
        p = self.players[p]
        for n in range(4):
            nPos = (150 + (n * 44), 137)
            if p.board[n] != 0:
                if p.board[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = p.board[n]
            elif hovCheck("rect", [nPos, (44,58)], pygame.mouse.get_pos()):
                if "Grimora" in self.screen or ("Leshy" in self.screen and n == 3):
                    WIN.blit(pyload("Scryption_Display/Selected/Grimora.png"), (nPos[0]*dimension, nPos[1]*dimension))
                elif "PO3" in self.screen or ("Leshy" in self.screen and n == 1):
                    WIN.blit(pyload("Scryption_Display/Selected/PO3.png"), (nPos[0]*dimension, nPos[1]*dimension))
                elif "Magnificus" in self.screen or ("Leshy" in self.screen and n == 0):
                    WIN.blit(pyload("Scryption_Display/Selected/Magnificus.png"), (nPos[0]*dimension, nPos[1]*dimension))
                else:
                    WIN.blit(pyload("Scryption_Display/Selected/Leshy.png"), (nPos[0]*dimension, nPos[1]*dimension))
                WIN.blit(pyload("Scryption_Display/Selected/Outline"+str(int((counter%60)/12))+".png"), (nPos[0]*dimension, nPos[1]*dimension))
            nPos = (nPos[0], nPos[1]-64)
            if p2.board[3 - n] != 0:
                if p2.board[3-n].checkSigil("Sprinter"):
                    p2.board[3-n].repSigil("Sprinter", "SprinterL")
                else:
                    p2.board[3-n].repSigil("SprinterL", "Sprinter")
                if p2.board[3-n].checkSigil("Hefty"):
                    p2.board[3-n].repSigil("Hefty", "HeftyL")
                else:
                    p2.board[3-n].repSigil("HeftyL", "Hefty")
                if p2.board[3-n].checkSigil("Rampager"):
                    p2.board[3-n].repSigil("Rampager", "RampagerL")
                else:
                    p2.board[3-n].repSigil("RampagerL", "Rampager")
                if p2.board[3 - n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = p2.board[3 - n]
            elif hovCheck("rect", [nPos, (44,58)], pygame.mouse.get_pos()):
                if "Grimora" in self.screen or ("Leshy" in self.screen and n == 0):
                    WIN.blit(pyload("Scryption_Display/Selected/Grimora.png"), (nPos[0]*dimension, nPos[1]*dimension))
                elif "PO3" in self.screen or ("Leshy" in self.screen and n == 2):
                    WIN.blit(pyload("Scryption_Display/Selected/PO3.png"), (nPos[0]*dimension, nPos[1]*dimension))
                elif "Magnificus" in self.screen or ("Leshy" in self.screen and n == 3):
                    WIN.blit(pyload("Scryption_Display/Selected/Magnificus.png"), (nPos[0]*dimension, nPos[1]*dimension))
                else:
                    WIN.blit(pygame.transform.flip(pyload("Scryption_Display/Selected/Leshy.png"), 0, 1), (nPos[0]*dimension, nPos[1]*dimension))
                WIN.blit(pyload("Scryption_Display/Selected/Outline"+str(int((counter%60)/12))+".png"), (nPos[0]*dimension, nPos[1]*dimension))
        # Bones
        renderFont(str(p.bones), (66,67), WIN)
        # Deck amounts
        renderFont(str(len(p.deck)), (372, 199), WIN)
        renderFont(str(len(p.squirrels)), (420, 199), WIN)
        # Scales
        dnum = max(-5, min(5, p.damage-p2.damage))
        WIN.blit(pyload("Scryption_Display/Scales/scale"+str(dnum)+".png"), (48*dimension,116*dimension))
        pnum = (122-4*int((-dnum+5)/10)-int((dnum+5)/10), 2*dnum+170-int(dnum/(4+max(0,-dnum))))
        pnum = (pnum[0]*dimension, pnum[1]*dimension)
        p2num = (56+4*int((dnum+5)/10)+int((-dnum+5)/10), -2*dnum+169-int((dnum-1)/(4+max(0,dnum))))
        p2num = (p2num[0]*dimension, p2num[1]*dimension)
        dmgnum = p.damage
        if dmgnum > 10:
            dmgnum = "10+"
        dmgnum2 = p2.damage
        if dmgnum2 > 10:
            dmgnum2 = "10+"
        WIN.blit(pyload("Scryption_Display/Scales/num"+str(dmgnum)+".png"), pnum)
        WIN.blit(pyload("Scryption_Display/Scales/num"+str(dmgnum2)+".png"), p2num)
        if p.screenVer == "hoard":
            for n in range(len(p.deck)):
                if n == len(p.deck) - 1 or len(p.deck) < 9:
                    cardSep = 44
                else:
                    cardSep = 332 / (len(p.deck) - 1) + 2
                if p.deck[n].show_image(dimension, (240+cardSep*(n-len(p.deck)/2), 215), 0, WIN, counter, cardSep, 1):
                    hovered = p.deck[n]
        else:
            for n in range(len(p.hand)):
                # Blood display
                if p.hand[n].selected and p.hand[n].cost[-1] == "B" and not int(p.hand[n].cost[:-1]):
                    WIN.blit(pyload("Scryption_Display/Bloods/bld"+str(p.hand[n].sacNeed)+".png"), (104*dimension,62*dimension))
                if n == len(p.hand) - 1 or len(p.hand) < 9:
                    cardSep = 44
                else:
                    cardSep = 332 / (len(p.hand) - 1) + 2
                if p.hand[n].show_image(dimension,(240+cardSep*(n-len(p.hand)/2),215),0,WIN,counter,cardSep,1):
                    hovered = p.hand[n]
            if p.myTurn and p.drawn and hovCheck("rect", [(50, 77), (91, 36)], p.mousePos):
                WIN.blit(pyload("Scryption_Display/bellDown.png"), (50*dimension, 77*dimension))
        if not p.myTurn:
            WIN.blit(pyload("Scryption_Display/notMyTurn.png"), (0, 0))
        return hovered

    def battleMoment2(self, player):
        p = self.players[player]
        p2 = self.players[1-player]
        for k in range(len(p.hand)):
            card = p.hand[k]
            if card.selected:
                card.counter += 0.1
                if card.counter >= 2*math.pi:
                    card.counter = 0
                break
        for n in range(4):
            if p.board[n] != 0:
                # Set variable powers
                if p.board[n].tempPow == "antpow":
                    p.board[n].power = 0
                    for m in range(4):
                        if p.board[m] != 0 and p.board[m].trait == "ant":
                            p.board[n].power += 1
                elif p.board[n].tempPow == "mirrpow":
                    if p2.board[3 - n] == 0:
                        p.board[n].power = 0
                    else:
                        p.board[n].power = p2.board[3 - n].power
                elif p.board[n].tempPow == "cardpow":
                    p.board[n].power = len(p.hand)
                elif p.board[n].tempPow == "bellpow":
                    p.board[n].power = 3 - n
                    print(p.board[n].power)
                    for m in range(4):
                        if p.board[m] != 0 and p.board[m].trait == "chime":
                            p.board[n].power = max(p.board[n].power, 5 - abs(n - m))
                elif p.board[n].tempPow == "bonpow":
                    p.board[n].power = int(p.bones / 2)
                elif p.board[n].tempPow == "blodpow":
                    p.board[n].power = p.sacNum
                p.board[n].powChange = 0
                if p2.board[3-n] != 0 and p2.board[3-n].checkSigil("Stinky") and not p.board[n].checkSigil("Made of Stone"):
                    p.board[n].powChange -= 1
                if n != 0 and p.board[n-1] != 0 and p.board[n-1].checkSigil("Leader"):
                    p.board[n].powChange += 1
                if n != 3 and p.board[n+1] != 0 and p.board[n+1].checkSigil("Leader"):
                    p.board[n].powChange += 1
        # Starvation sets in...
        if p.myTurn and not p.drawn and len(p.deck)+len(p.squirrels) == 0:
            p.drawn = True
            self.starves.trait += 1
            newStarv = create_card("Starvation")
            newStarv.setEqual(self.starves)
            newStarv.power = newStarv.trait
            newStarv.health = newStarv.trait
            if 0 in p.board:
                for k in range(4):
                    if p2.board[3-k] == 0:
                        p2.board[3-k] = newStarv
                        return
            else:
                for k in range(4):
                    if p2.board[3-k].name != "Starvation":
                        p2.board[3-k] = newStarv
                        return
                minPow = min([m.power for m in p2.board])
                for k in range(4):
                    if p2.board[3-k].power == minPow:
                        p2.board[3-k] = newStarv
                        return

    def battleClick(self, p, p2):
        if p.drawn:
            for n in range(len(p.hand)):
                # Play a card
                if n >= len(p.hand):
                    break
                if p.hand[n].selected:
                    for m in range(4):
                        if hovCheck("rect", [(150 + m * 44, 137), (44, 56)], p.mousePos):
                            if p.cursorMode == "sacrifice" and p.board[m] != 0 and not p.board[m].marked:
                                if p.board[m].trait not in ["terrain", "pelt"] and p.board[m].name != "Chime":
                                    p.board[m].marked = True
                                    if p.board[m].checkSigil("Worthy Sacrifice"):
                                        p.hand[n].sacNeed -= 3
                                    else:
                                        p.hand[n].sacNeed -= 1
                                    if p.hand[n].sacNeed <= 0:
                                        for k in range(4):
                                            if p.board[k] != 0 and p.board[k].marked:
                                                p.sacNum += 1
                                                if p.board[k].checkSigil("Morsel"):
                                                    p.hand[n].power += p.board[k].power
                                                    p.hand[n].health += p.board[k].health
                                                if "cat" in p.board[k].trait and p.board[k].checkSigil("Many Lives"):
                                                    p.board[k].trait = p.board[k].trait[0:2] + str(int(p.board[k].trait[-1])+1)
                                                    if p.board[k].trait == "cat9":
                                                        keepcat = p.board[k]
                                                        p.board[k] = keepcat.create_card("Undead Cat")
                                                        p.board[k].power += keepcat.power
                                                        p.board[k].health += keepcat.health - 1
                                                        p.board[k].sigils += keepcat.sigils
                                                        p.board[k].sigils2 += keepcat.sigils2
                                                        p.board[k].sigils.remove("Many Lives")
                                                elif "child" in p.board[k].trait and p.board[k].checkSigil("Many Lives"):
                                                    p.board[k].trait = p.board[k].trait[0:5] + str(int(p.board[k].trait[5:])+1)
                                                    if int(p.board[k].trait[5:]) % 2 == 1:
                                                        p.board[k].power += 2
                                                        p.board[k].sigils.append("Airborne")
                                                    else:
                                                        p.board[k].power -= 2
                                                        p.board[k].sigils.remove("Airborne")
                                                    if p.board[k].trait == "child13":
                                                        p.board[k] = create_card("Hungry Child")
                                                elif not p.board[k].checkSigil("Many Lives"):
                                                    # Card dies
                                                    if p.board[k].checkSigil("Bone King"):
                                                        p.bones += 3
                                                    if p.board[k].checkSigil("Unkillable"):
                                                        if p.board[k].trait == "ouroboros":
                                                            p.board[k].power += 1
                                                            p.board[k].health += 1
                                                            p.cards[p.board[k].deckspot].power += 1
                                                            p.cards[p.board[k].deckspot].health += 1
                                                        p.board[k].cost = p.board[k].create_card(p.board[k].name).cost
                                                        p.board[k].selected = False
                                                        p.board[k].marked = False
                                                        p.deck.append(p.board[k])
                                                        p.draw_card(p.deck, -1)
                                                    p.board[k] = 0
                                                    p.bones += 1
                                                    for i in range(4):
                                                        if p2.board[i] != 0 and p2.board[i].checkSigil("Scavenger"):
                                                            p2.bones += 1
                                                            break
                                        p.cursorMode = "normal"
                                        p.hand[n].cost = "0N"
                            elif p.cursorMode == "sacrifice" and p.board[m] != 0 and p.board[m].marked:
                                p.board[m].marked = False
                                if p.board[m].checkSigil("Worthy Sacrifice"):
                                    p.hand[n].sacNeed += 3
                                else:
                                    p.hand[n].sacNeed += 1
                            elif p.cursorMode == "sacrifice":
                                p.cursorMode = "normal"
                                p.hand[n].selected = False
                                for k in range(4):
                                    if p.board[k] != 0:
                                        p.board[k].marked = False
                                p.hand[n].sacNeed = int(p.hand[n].cost[:-1])
                            elif p.cursorMode == "normal" and p.board[m] == 0:
                                # Card gets played
                                playing = False
                                if p.hand[n].cost[-1] == "N":
                                    if p.bones >= int(p.hand[n].cost[:-1]):
                                        p.bones -= int(p.hand[n].cost[:-1])
                                        playing = True
                                else:
                                    playing = True
                                if playing:
                                    p.play_card(n, m)
                                    if p.board[m].checkSigil("Hoarder") and len(p.deck) > 0:
                                        for k in range(len(p.deck)):
                                            if p.deck[n].trait == "ijiraq":
                                                while p.deck[n].trait == "ijiraq":
                                                    p.deck[n].setEqual(random.choice(p.deck))
                                                p.deck[n].trait = "ijiraq"
                                        p.screenVer = "hoard"
                                    if p.board[m].checkSigil("Brood Parasite"):
                                        if p2.board[3 - m] == 0:
                                            if random.randint(1, 10) == 10:
                                                p2.board[3 - m] = p.board[m].create_card("Raven Egg")
                                            else:
                                                p2.board[3 - m] = p.board[m].create_card("Broken Egg")
                                    if p2.board[3 - m] == 0:
                                        for k in range(4):
                                            if p2.board[k] != 0 and k != 3 - m and p2.board[k].checkSigil("Guardian"):
                                                p2.board[3 - m] = p2.board[k]
                                                p2.board[k] = 0
                                                break
                            break
                    if not hovCheck("rect", [(150, 137), (176, 56)], p.mousePos):
                        p.hand[n].selected = False
                        if p.cursorMode == "sacrifice":
                            p.cursorMode = "normal"
                            p.hand[n].sacNeed = int(p.hand[n].cost[:-1])
                            for m in range(4):
                                if p.board[m] != 0:
                                    p.board[m].marked = False
                else:
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    n_cp = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if hovCheck("rect", [n_cp, (cardSep, 58)], p.mousePos):
                        if p.hand[n].cost[-1] == "N":
                            if p.bones >= int(p.hand[n].cost[:-1]):
                                p.hand[n].selected = True
                                p.hand[n].counter = 0
                        elif p.hand[n].cost[-1] == "B":
                            sacs = 0
                            for i in range(4):
                                if p.board[i] != 0:
                                    if p.board[i].checkSigil("Worthy Sacrifice"):
                                        sacs += 3
                                    elif p.board[i].trait not in ["terrain", "pelt"] and p.board[i].name != "Chime":
                                        sacs += 1
                            if sacs >= int(p.hand[n].cost[:-1]):
                                p.hand[n].selected = True
                                p.hand[n].counter = 0
                                p.cursorMode = "sacrifice"
            if hovCheck("rect", [(50, 77), (91, 36)], p.mousePos):
                # End turn
                for n in range(4):
                    if p.board[n] != 0:
                        if p.board[n].power > 0:
                            # Attack
                            bif = p.board[n].checkSigil("Bifurcated Strike")
                            trif = p.board[n].checkSigil("Trifurcated Strike")
                            targets = []
                            # find places to attack
                            if p.board[n].checkSigil("Double Strike"):
                                targets.append(n)
                            if bif or trif:
                                if bif:
                                    if n > 0:
                                        targets.append(n + 1)
                                    if n < 3:
                                        targets.append(n - 1)
                                if trif:
                                    targets.append(n)
                                    if n > 0:
                                        targets.append(n + 1)
                                    if n < 3:
                                        targets.append(n - 1)
                            else:
                                targets.append(n)
                            for m in targets:
                                if 0 <= m <= 3:
                                    corpsReady = p2.board[m]
                                    attack(p,p2,n,3-m,p.board[n].power+p.board[n].powChange)
                                    if "Grimora" in self.screen and p2.board[m] != corpsReady:
                                        # Grimora prepares corpses
                                        corpsReady.setEqual(p2.cards[corpsReady.deckspot])
                                        self.corpses.append([corpsReady, 2, self.players.index(p2)])
                                    if "Leshy" in self.screen and p2.board[m] != corpsReady:
                                        corpsReady.setEqual(p2.cards[corpsReady.deckspot])
                                        if len(p2.photos) == 0:
                                            p2.photos.append([corpsReady.cost, corpsReady.portrait])
                                        elif len(p2.photos) == 1:
                                            p2.photos.append([corpsReady.power, corpsReady.health])
                                        elif len(p2.photos) == 2:
                                            p2.photos.append([corpsReady.sigils, corpsReady.sigils2])
                                    if "Leshy" in self.screen and p.damage >= p2.damage+5:
                                        self.runGimmicks(p, p2, m)
                        if p.board[n].checkSigil("Bone Digger"):
                            # Dig for bones
                            p.bones += 1
                        # Movement sigils
                        moveNum = 0
                        if p.board[n].checkSigil("Sprinter") or p.board[n].checkSigil("SprinterL"):
                            moveNum += 1
                        if p.board[n].checkSigil("Rampager") or p.board[n].checkSigil("RampagerL"):
                            moveNum += 1
                        if p.board[n].checkSigil("Hefty") or p.board[n].checkSigil("HeftyL"):
                            moveNum += 1
                        for _ in range(moveNum):
                            self.movers.append(p.board[n])
                    if p2.board[n] != 0:
                        if p2.board[n].checkSigil("Fledgling"):
                            p2.board[n] = p2.board[n].growUp()
                for i in self.movers:
                    m = p.board.index(i)
                    if i.checkSigil("Rampager"):
                        if m == 3:
                            temp = p.board[m-1]
                            if temp == 0 and i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            p.board[m-1] = i
                            p.board[m] = temp
                            i.repSigil("Rampager", "RampagerL")
                        else:
                            temp = p.board[m+1]
                            if temp == 0 and i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            p.board[m+1] = i
                            p.board[m] = temp
                    elif i.checkSigil("RampagerL"):
                        if m == 0:
                            temp = p.board[m+1]
                            if temp == 0 and i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            p.board[m+1] = i
                            p.board[m] = temp
                            i.repSigil("RampagerL", "Rampager")
                        else:
                            temp = p.board[m-1]
                            if temp == 0 and i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            p.board[m-1] = i
                            p.board[m] = temp
                    elif i.checkSigil("Hefty"):
                        hefmov = False
                        for k in range(4-m):
                            if p.board[m+k] == 0:
                                hefmov = True
                        if hefmov:
                            temp = 0
                            if i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            for k in range(4):
                                p.board[m+k], temp = temp, p.board[m+k]
                                if temp == 0:
                                    break
                        else:
                            i.repSigil("Hefty", "HeftyL")
                            for k in range(m):
                                if p.board[k] == 0:
                                    hefmov = True
                            if hefmov:
                                temp = 0
                                if i.trait == "long elk":
                                    temp = i.create_card("Vertebrae")
                                for k in range(4):
                                    p.board[m-k], temp = temp, p.board[m-k]
                                    if temp == 0:
                                        break
                    elif i.checkSigil("HeftyL"):
                        hefmov = False
                        for k in range(m):
                            if p.board[k] == 0:
                                hefmov = True
                                break
                        if hefmov:
                            temp = 0
                            if i.trait == "long elk":
                                temp = i.create_card("Vertebrae")
                            for k in range(4):
                                p.board[m-k], temp = temp, p.board[m-k]
                                if temp == 0:
                                    break
                        else:
                            i.repSigil("HeftyL", "Hefty")
                            for k in range(4-m):
                                if p.board[m+k] == 0:
                                    hefmov = True
                            if hefmov:
                                temp = 0
                                if i.trait == "long elk":
                                    temp = i.create_card("Vertebrae")
                                for k in range(4):
                                    p.board[m+k], temp = temp, p.board[m+k]
                                    if temp == 0:
                                        break
                    elif i.checkSigil("Sprinter"):
                        if m < 3 and p.board[m+1] == 0:
                            p.board[m+1] = i
                            p.board[m] = 0
                            if i.trait == "long elk":
                                p.board[m] = i.create_card("Vertebrae")
                        else:
                            i.repSigil("Sprinter", "SprinterL")
                            if m > 0 and p.board[m-1] == 0:
                                p.board[m-1] = i
                                p.board[m] = 0
                                if i.trait == "long elk":
                                    p.board[m] = i.create_card("Vertebrae")
                    elif i.checkSigil("SprinterL"):
                        if m > 0 and p.board[m-1] == 0:
                            p.board[m-1] = i
                            p.board[m] = 0
                            if i.trait == "long elk":
                                p.board[m] = i.create_card("Vertebrae")
                        else:
                            i.repSigil("SprinterL", "Sprinter")
                            if m < 3 and p.board[m+1] == 0:
                                p.board[m+1] = i
                                p.board[m] = 0
                                if i.trait == "long elk":
                                    p.board[m] = i.create_card("Vertebrae")
                self.movers = []
                # PO3 rotates
                if "PO3" in self.screen:
                    for k in range(4):
                        if k == 0:
                            po3 = p.board[0]
                        if k == 3:
                            p.board[3] = p2.board[0]
                        else:
                            p.board[k] = p.board[k+1]
                    for k in range(4):
                        if k == 3:
                            p2.board[3] = po3
                        else:
                            p2.board[k] = p2.board[k+1]
                # Grimora revives
                if "Grimora" in self.screen:
                    for k in range(len(self.corpses)):
                        self.corpses[k][1] -= 1
                        if self.corpses[k][1] <= 0:
                            self.corpses[k][2].deck.append(self.corpses[k][0])
                            self.corpses[k][2].draw_card(self.corpses[k][2].deck, -1)
                    self.corpses = [k for k in self.corpses if k[1] > 0]
                # Magnificus paints
                if p2.paint:
                    for k in range(4):
                        if p2.board[k] != 0:
                            p2.board[k].sigils = [random.choice(sigilList2)]
                # Done with everything so...
                p.drawn = False
                p.harpyActive = False
                if p.skipper:
                    p.skipper = False
                else:
                    p.myTurn = False
                    p2.myTurn = True
                    p2.drawn = False
                if p.damage >= p2.damage+5:
                    self.rounds -= 1
                    if self.rounds == 0:
                        p.teeth += p.damage-p2.damage-5
                        return True
                    else:
                        p.damage = p2.damage = 0
            for n in range(3):
                # Use an item
                if p.items[n] != 0 and hovCheck("rect", [(360 + 26 * n, 131), (25, 50)], p.mousePos):
                    if p.items[n] == "Fish Hook":
                        p.screenVer = "cut"+str(n)
                    else:
                        if p.items[n] == "Magpies Lens":
                            for k in range(len(p.deck)):
                                if p.deck[n].trait == "ijiraq":
                                    while p.deck[n].trait == "ijiraq":
                                        p.deck[n].setEqual(random.choice(p.deck))
                                    p.deck[n].trait = "ijiraq"
                            p.screenVer = "hoard"
                        elif p.items[n] == "Skinning Knife" or p.items[n] == "Scissors":
                            p.screenVer = "cut"+str(n)
                        elif p.items[n] == "Boulder in a Bottle":
                            p.deck.append(create_card("Boulder"))
                            p.draw_card(p.deck, -1)
                        elif p.items[n] == "Squirrel in a Bottle":
                            p.deck.append(create_card("Squirrel"))
                            p.draw_card(p.deck, -1)
                        elif p.items[n] == "Black Goat in a Bottle":
                            p.deck.append(create_card("Black Goat"))
                            p.draw_card(p.deck, -1)
                        elif p.items[n] == "Frozen Opossum in a Bottle":
                            p.deck.append(create_card("Frozen Opossum"))
                            p.draw_card(p.deck, -1)
                        elif p.items[n] == "Pliers":
                            p.damage += 1
                        elif p.items[n] == "Special Dagger":
                            p.damage += 5
                        elif p.items[n] == "Hoggy Bank":
                            p.bones += 4
                        elif p.items[n] == "Harpies Birdleg Fan":
                            p.harpyActive = True
                        elif p.items[n] == "Wiseclock":
                            for k in range(4):
                                if k == 0:
                                    po3 = p.board[0]
                                if k == 3:
                                    p.board[3] = p2.board[0]
                                else:
                                    p.board[k] = p.board[k+1]
                            for k in range(4):
                                if k == 3:
                                    p2.board[3] = po3
                                else:
                                    p2.board[k] = p2.board[k+1]
                        elif p.items[n] == "Magickal Bleach":
                            for i in range(4):
                                if p2.board[i] != 0:
                                    p2.board[i].sigils = p2.board[i].sigils2 = []
                        elif p.items[n] == "Hourglass":
                            p.skipper = True
                        p.items[n] = 0
        else:
            # Pick a deck to draw from
            if hovCheck("rect", [(356, 188), (30, 19)], p.mousePos) and len(p.deck):
                p.draw_card(p.deck, 0)
                p.drawn = True
            elif hovCheck("rect", [(399, 188), (35, 19)], p.mousePos) and len(p.squirrels):
                p.draw_card(p.squirrels, 0)
                p.drawn = True

    def hoardClick(self, p):
        for n in range(len(p.deck)):
            if n == len(p.deck) - 1 or len(p.deck) < 9:
                cardSep = 44
            else:
                cardSep = 332 / (len(p.deck) - 1) + 2
            n_cp = (240 + cardSep * (n - len(p.deck) / 2), 215)
            if hovCheck("rect", [n_cp, (cardSep, 58)], p.mousePos):
                p.draw_card(p.deck, n)
                return True

    def cutClick(self, p, p2):
        for n in range(4):
            n_cp = (150 + (n * 44), 74)
            if hovCheck("rect", [n_cp, (44, 58)], p.mousePos):
                if p2.board[3 - n] != 0 and p2.board[3 - n].trait not in ["uncuttable","pack mule"]:
                    if p.items[int(p.screenVer[-1])] == "Fish Hook":
                        if p.board[n] == 0:
                            p.board[n] = p2.board[3-n]
                            p2.board[3-n] = 0
                            p.items[int(p.screenVer[-1])] = 0
                    else:
                        p2.board[3-n] = 0
                        if p.items[int(p.screenVer[-1])] == "Skinning Knife":
                            p.hand.append(create_card("Wolf Pelt"))
                        p.items[int(p.screenVer[-1])] = 0
        return True

    def stoneMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        for n in range(2):
            if isinstance(self.stones[n], Card):
                nPos = ((215 - 7 * n), (59 + 74 * n))
                if self.stones[n].show_image(dimension, nPos, n, WIN, counter, 44, 1):
                    hovered = self.stones[n]
        if not p.deckShow:
            if self.stones[0] not in [0, 1] and self.stones[1] not in [0, 1]:
                WIN.blit(pyload("Scryption_Display/Buttons/Stones.png"), (0, 0))
                if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    WIN.blit(pyload("Scryption_Display/Buttons/StonePress.png"), (0, 0))
            else:
                if 1 in [self.stones[0], self.stones[1]]:
                    for n in range(len(p.hand)):
                        if len(p.hand) < 9:
                            cardSep = 44
                        else:
                            cardSep = 332 / (len(p.deck) - 1) + 2
                        nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                        if n == len(p.hand) - 1:
                            cardSep = 44
                        if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                            hovered = p.hand[n]
        return hovered

    def stoneClick(self, p):
        for m in range(2):
            if hovCheck("rect", [(215 - 7 * m, 59 + 74 * m), (44 + 14 * m, 58 - 14 * m)], p.mousePos):
                if self.stones[abs(m - 1)] != 1:
                    self.stones[m] = 1
                    if m == 0:
                        p.hand = [n for n in p.cards if len(n.sigils2) == 0 and n != self.stones[1] and n.trait != "glitch"]
                        if self.stones[1] != 0:
                            sigil1 = set(self.stones[1].sigils)
                            p.hand = [n for n in p.hand if not sigil1.intersection(n.sigils)]
                    if m == 1:
                        p.hand = [n for n in p.cards if len(n.sigils2) == 0 and n != self.stones[0] and len(n.sigils) != 0 and n.trait != "glitch"]
        if not p.deckShow:
            if 1 in (self.stones[0], self.stones[1]):
                for n in range(len(p.hand)):
                    if n >= len(p.hand):
                        break
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    n_cp = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if hovCheck("rect", [n_cp, (cardSep, 58)], p.mousePos):
                        if self.stones[0] == 1:
                            self.stones[0] = p.hand[n]
                        if self.stones[1] == 1:
                            self.stones[1] = p.hand[n]
            elif 0 not in (self.stones[0], self.stones[1]):
                if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    self.stones[0].sigils2 = self.stones[1].sigils
                    p.cards[self.stones[0].deckspot] = self.stones[0]
                    p.cards.pop(self.stones[1].deckspot)
                    self.stones = [0,0]
                    return True

    def fireMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        WIN.blit(pyload("Scryption_Display/Events/fire"+self.fire[2]+".png"), (0, 0))
        for n in range(5):
            nPos = (int(68*math.sin(math.pi*(0.29*n-0.58))+216), int(-68*math.cos(math.pi*(0.29*n-0.58))+110))
            self.fire[0][n].show_image(dimension, nPos, 0, WIN, counter, 44, 0)
        if self.fire[1] == 1:
            if not p.deckShow:
                for n in range(len(p.hand)):
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                        hovered = p.hand[n]
        elif self.fire[1] != 0 and self.fire[3] < 2:
            firPos = (216, 112)
            if self.fire[1].show_image(dimension, firPos, 0, WIN, counter, 44, 1):
                hovered = self.fire[1]
            if not p.deckShow:
                WIN.blit(pyload("Scryption_Display/Buttons/Fire.png"), (0, 0))
                if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    WIN.blit(pyload("Scryption_Display/Buttons/FirePress.png"), (0, 0))
        return hovered

    def fireClick(self, p):
        if hovCheck("rect", [(216, 112), (44, 58)], p.mousePos):
            if self.fire[3] > self.survsDead:
                return True
            else:
                self.fire[1] = 1
                p.hand = [n for n in p.cards if n.trait != "glitch"]
                if self.fire[2] == "p":
                    p.hand = [n for n in p.hand if isinstance(p.power, int)]
        if not p.deckShow:
            if self.fire[1] == 1:
                for n in range(len(p.hand)):
                    if n >= len(p.hand):
                        break
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    n_cp = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if hovCheck("rect", [n_cp, (cardSep, 58)], p.mousePos):
                        self.fire[1] = p.hand[n]
            elif hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos) and self.fire[3] < 2:
                if self.fire[2] == 'p':
                    self.fire[1].power += 1
                else:
                    self.fire[1].health += 2
                if self.fire[3] > 0 and not self.survsDead:
                    if random.randint(0, 1) == 1:
                        p.cards.pop(self.fire[1].deckspot)
                        if 0 in p.items:
                            p.items[p.items.index(0)] = "Hoggy Bank"
                        if self.fire[1].trait == "kills survivors" or self.fire[1].checkSigil("Touch of Death"):
                            self.survsDead = 1
                        return True
                self.fire[3] += 1

    def tradeMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        if self.trades[3] == 0:
            p.hand = [n for n in p.cards if n.name == "Rabbit Pelt"]
        elif self.trades[3] == 1:
            p.hand = [n for n in p.cards if n.name == "Wolf Pelt"]
        else:
            p.hand = [n for n in p.cards if n.name == "Golden Pelt"]
        for n in range(4 * (2 - int(self.trades[3] / 2))):
            if self.trades[self.trades[3]][n] != 0:
                nPos = ((150 + (n % 4) * 44), (73 + int(n / 4) * 64))
                if self.trades[self.trades[3]][n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = self.trades[self.trades[3]][n]
        if not p.deckShow:
            for n in range(len(p.hand)):
                if len(p.hand) < 9:
                    cardSep = 44
                else:
                    cardSep = 332 / (len(p.hand) - 1) + 2
                nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                if n == len(p.hand) - 1:
                    cardSep = 44
                if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                    hovered = p.hand[n]
        return hovered

    def tradeClick(self, p):
        p2 = self.players[1-self.players.index(p)]
        if p.myTurn:
            for n in range(4 * (2 - int(self.trades[3] / 2))):
                if hovCheck("rect", [(150+(n%4)*44,73+int(n/4)*64),(44,58)], p.mousePos) and self.trades[self.trades[3]][n] != 0:
                    if self.trades[3] == 0:
                        p.hand = [n for n in p.cards if n.name == "Rabbit Pelt"]
                    elif self.trades[3] == 1:
                        p.hand = [n for n in p.cards if n.name == "Wolf Pelt"]
                    else:
                        p.hand = [n for n in p.cards if n.name == "Golden Pelt"]
                    p.cards.append(self.trades[self.trades[3]][n])
                    self.trades[self.trades[3]][n] = 0
                    p.cards.remove(p.hand.pop(0))
                    if self.trades[self.trades[3]].count(0) == len(self.trades[self.trades[3]]):
                        if self.trades[3] == 0:
                            self.trades[0] = get_cardlist("common", 8)
                        elif self.trades[3] == 1:
                            self.trades[1] = get_cardlist("common", 8)
                            for k in self.trades[1]:
                                k.sigils2 = [random.choice(sigilList2)]
                        elif self.trades[3] == 2:
                            self.trades[2] = get_cardlist("rare", 4)
                    if len(p.hand)+len(p2.hand) == 0:
                        self.trades[3] += 1
                        if self.trades[3] == 1 and len([n for n in p.cards if n.name == "Wolf Pelt"])+len([n for n in p2.cards if n.name == "Wolf Pelt"]) == 0:
                            self.trades[3] += 1
                        if self.trades[3] == 2 and len([n for n in p.cards if n.name == "Golden Pelt"])+len([n for n in p.cards if n.name == "Golden Pelt"]) == 0:
                            self.trades[3] += 1
                        if len(p2.hand) == 0:
                            return True
                    p.myTurn = False
                    p2.myTurn = True

    def trapMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        WIN.blit(pyload("Scryption_Display/InItems/Skinning_Knife.png"), (159 * dimension, 141 * dimension))
        if hovCheck("rect", [(159, 131), (25, 50)], p.mousePos):
            WIN.blit(pyload("Scryption_Display/HovItems/Skinning_Knife.png"),(159*dimension,141*dimension))
        for n in range(3):
            nPos = (194 + n * 44, 138)
            if self.trap[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = self.trap[n]
        for n in range(4):
            nPos = (150 + n * 44, 138)
            WIN.blit(pyload("Scryption_Display/Events/CostTag.png"),(nPos[0]*dimension,nPos[1]*dimension))
            font = pygame.font.Font("Scrypt_Font.ttf", 10)
            if n == 0:
                pric = font.render(str(7), 0, (0,0,0))
            else:
                pric = font.render(str(self.trap[4][n - 1]), 0, (0, 0, 0))
            pricsiz = pric.get_size()
            pric = pygame.transform.scale(pric,(pricsiz[0]*dimension, pricsiz[1]*dimension))
            if len(str(self.trap[4][n-1])) > 1 and n != 0:
                pric = pygame.transform.scale(pric, (pricsiz[0]*dimension/2, pricsiz[1]*dimension))
            WIN.blit(pric, ((nPos[0]+7)*dimension,(nPos[1]+9)*dimension))
        WIN.blit(pyload("Scryption_Display/Foil.png"), (220*dimension, 110*dimension))
        renderFont("x"+str(p.teeth), (233, 110), WIN)
        if not p.deckShow:
            for n in range(len(p.hand)):
                if len(p.hand) < 9:
                    cardSep = 44
                else:
                    cardSep = 332 / (len(p.hand) - 1) + 2
                nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                if n == len(p.hand) - 1:
                    cardSep = 44
                if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                    hovered = p.hand[n]
        return hovered

    def trapClick(self, p):
        for n in range(3):
            if hovCheck("rect", [(194 + n * 44, 138), (44, 58)], p.mousePos):
                if self.trap[4][n] <= p.teeth:
                    p.hand.append(create_card(self.trap[n].name))
                    p.teeth -= self.trap[4][n]
        if hovCheck("rect", [(159, 141), (25, 50)], p.mousePos) and 0 in p.items and p.teeth >= 7:
            p.items[p.items.index(0)] = "Skinning Knife"
            p.teeth -= 7
        if not p.deckShow:
            for n in range(len(p.hand)):
                if n >= len(p.hand):
                    break
                if len(p.hand) < 9:
                    cardSep = 44
                else:
                    cardSep = 332 / (len(p.hand) - 1) + 2
                n_cp = (240 + cardSep * (n - len(p.hand) / 2), 215)
                if n == len(p.hand) - 1:
                    cardSep = 44
                if hovCheck("rect", [n_cp, (cardSep, 58)], p.mousePos):
                    for k in p.hand:
                        p.cards.append(k)
                    p.hand = []
                    p.myTurn = False
                    if not self.players[1-self.players.index(p)].myTurn:
                        return True

    def cardMoment(self, p, hovered, counter, WIN):
        for n in range(3):
            if self.choice[n] != 0:
                nPos = ((160 + n * 56), 90)
                if self.choice[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = self.choice[n]
        return hovered

    def cardClick(self, p):
        for n in range(3):
            if hovCheck("rect", [(160 + n * 56, 90), (44, 58)], p.mousePos) and self.choice[n] != 0:
                p.cards.append(self.choice[n])
                self.choice[n] = 0
                if p.playerNum == 1 or self.screen == "rarech":
                    return True
                else:
                    p.myTurn = False
                    self.players[1-self.players.index(p)].myTurn = True

    def cardSecMoment(self, p, hovered, counter, WIN):
        if self.screen == "costch":
            var = self.choiceC
        elif self.screen == "tribch":
            var = self.choiceT
        elif self.screen == "rocky":
            var = self.prosps
        for n in range(3):
            if var[2][n] != 0:
                nPos = (160 + n * 56, 90)
                if var[2][n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                    hovered = var[2][n]
        return hovered

    def cardSecClick(self, p):
        if self.screen == "costch":
            var = self.choiceC
        elif self.screen == "tribch":
            var = self.choiceT
        elif self.screen == "rocky":
            var = self.prosps
        for n in range(3):
            if hovCheck("rect", [(160 + n * 56, 90), (44, 58)], p.mousePos) and var[2][n] != 0:
                if var[2][n].trait != "secret":
                    p.cards.append(var[2][n])
                    if p.playerNum == 1:
                        return True
                    else:
                        p.myTurn = False
                        self.players[1-self.players.index(p)].myTurn = True
                        var[2][n] = 0
                        var[2][(n+2)%3] = var[1][(n+2)%3]
                        var[2][(n+4)%3] = var[1][(n+4)%3]
                else:
                    var[2][n] = var[0][n]
                    var[2][(n + 2) % 3] = 0
                    var[2][(n + 4) % 3] = 0

    def itemMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        if isinstance(self.prat, Card):
            if self.prat.show_image(dimension, (216, 112), 0, WIN, counter, 44, 1):
                hovered = self.prat
        elif 0 in p.items:
            for n in range(3):
                if self.prat[n] != 0:
                    nPos = (170 + 56 * n, 122)
                    WIN.blit(pyload("Scryption_Display/InItems/"+"_".join(self.prat[n].split())+".png"),(nPos[0]*dimension, nPos[1]*dimension))
                    if hovCheck("rect", [nPos, (25, 50)], p.mousePos):
                        WIN.blit(pyload("Scryption_Display/HovItems/"+"_".join(self.prat[n].split())+".png"),(nPos[0]*dimension,nPos[1]*dimension))
        return hovered

    def itemClick(self, p, p2):
        for n in range(3):
            if p.items[n] != 0 and hovCheck("rect", [(360 + 26 * n, 131), (25, 50)], p.mousePos):
                p.items[n] = 0
        if isinstance(self.prat, Card):
            if hovCheck("rect", [(216, 112), (44, 58)], p.mousePos):
                p.cards.append(self.prat)
                return True
        elif 0 in p.items:
            for n in range(3):
                nPos = (170 + 56 * n, 122)
                if hovCheck("rect", [nPos, (25, 50)], p.mousePos):
                    p.items[p.items.index(0)] = self.prat[n]
                    self.prat = random.sample(itemList2, 3)
        if 0 not in p.items and not isinstance(self.prat, Card):
            return True
        return False

    def boneMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        if self.bone == 1:
            if not p.deckShow:
                for n in range(len(p.hand)):
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                        hovered = p.hand[n]
        elif self.bone != 0:
            bonPos = (216, 112)
            if self.bone.show_image(dimension, bonPos, 0, WIN, counter, 44, 1):
                hovered = self.bone
            if not p.deckShow:
                WIN.blit(pyload("Scryption_Display/Buttons/Bone.png"), (0, 0))
                if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    WIN.blit(pyload("Scryption_Display/Buttons/BonePress.png"), (0, 0))
        return hovered

    def boneClick(self, p):
        if hovCheck("rect", [(216, 112), (58, 44)], p.mousePos):
            p.hand = [n for n in p.cards if n.trait != "glitch"]
            self.bone = 1
        if not p.deckShow:
            if self.bone == 1:
                for n in range(len(p.hand)):
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if hovCheck("rect", [nPos, (cardSep, 58)], p.mousePos):
                        self.bone = p.hand[n]
            elif isinstance(self.bone, Card) and hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                p.cards.pop(self.bone.deckspot)
                if self.bone.name not in ["Golden Pelt", "Wolf Pelt", "Rabbit Pelt"]:
                    p.boneStart += 1
                if self.bone.trait == "goat":
                    p.boneStart += 7
                return True

    def toteMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        if isinstance(self.carved, Card):
            if self.carved.show_image(dimension, (216, 90), 0, WIN, counter, 44, 1):
                hovered = self.carved
        else:
            if 0 in self.carved:
                listComp = p.totparts
            else:
                listComp = self.carved
            for n in range(len(listComp)):
                nPos = (170 + (n % 3) * 56, 70 + 30 * int(n / 3))
                if listComp[n] in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'] and listComp[n] != p.totem[0]:
                    nPos = (nPos[0], nPos[1] + 24)
                    WIN.blit(pyload("Scryption_Display/InTotems/"+listComp[n]+".png"),(nPos[0]*dimension,nPos[1]*dimension))
                    if hovCheck("rect", [nPos, (25, 25)], p.mousePos):
                        WIN.blit(pyload("Scryption_Display/HovTotems/"+listComp[n]+".png"),(nPos[0]*dimension,nPos[1]*dimension))
                elif listComp[n] in sigilList and listComp[n] != p.totem[1]:
                    WIN.blit(pyload("Scryption_Display/InTotems/Base.png"),(nPos[0] * dimension, nPos[1] * dimension))
                    WIN.blit(pyload("Scryption_Display/InTotems/Baseline.png"),(nPos[0]*dimension,nPos[1]*dimension))
                    if hovCheck("rect", [(nPos[0], nPos[1] + 24), (25, 25)], p.mousePos):
                        WIN.blit(pyload("Scryption_Display/HovTotems/Base.png"),(nPos[0] * dimension, nPos[1] * dimension))
                    thisSigil = sigilSpriteO[sigilList.index(listComp[n])]
                    sigilSize = thisSigil.get_size()
                    sigilImage = pygame.transform.scale(thisSigil, (sigilSize[0] * dimension, sigilSize[1] * dimension))
                    WIN.blit(sigilImage, ((nPos[0] + 4) * dimension, (nPos[1] + 27) * dimension))
        return hovered

    def toteClick(self, p):
        if isinstance(self.carved, Card):
            if hovCheck("rect", [(216, 90), (44, 58)], p.mousePos):
                p.cards.append(self.carved)
                self.carved = [0]
                p.totem = [0, 0]
        else:
            if 0 in self.carved:
                listLen = len(p.totparts)
            else:
                listLen = len(self.carved)
            for n in range(listLen):
                nPos = (170 + (n % 3) * 56, 94 + 30 * int(n / 3))
                if hovCheck("rect", [nPos, (25, 25)], p.mousePos):
                    if 0 in self.carved:
                        # Build totem
                        if p.totparts[n] in p.totem:
                            return
                        if p.totparts[n] in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile']:
                            p.totem[0] = p.totparts[n]
                        else:
                            p.totem[1] = p.totparts[n]
                        if 0 not in p.totem:
                            return True
                    else:
                        # Pick a totem part
                        p.totparts.append(self.carved[n])
                        self.carved[n] = 0
                        p.totem = [0, 0]
                        hasSigil = False
                        hasHead = False
                        for n in p.totparts:
                            if n in sigilList:
                                hasSigil = True
                            if n in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile']:
                                hasHead = True
                        if not (hasSigil and hasHead):
                            return True

    def mycoMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        if self.myco != (0,0):
            if self.myco == (1,1):
                if not p.deckShow:
                    # Phase 1: choose from pairs
                    for n in range(len(p.hand)):
                        if n >= len(p.hand):
                            break
                        if len(p.hand) < 9:
                            cardSep = 54
                        else:
                            cardSep = 332 / (len(p.hand) - 1)+2
                        nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                        if p.hand[n][1].show_image(dimension, nPos, 0, WIN, counter, 10, 1):
                            hovered = p.hand[n][1]
                        cardSep -= 10
                        if n == len(p.hand) - 1:
                            cardSep = 44
                        nPos = (nPos[0]+10, nPos[1])
                        if p.hand[n][0].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                            hovered = p.hand[n][0]
            elif isinstance(self.myco, tuple):
                # Phase 2: ready pair
                if self.myco[0].show_image(dimension, (195, 90), 0, WIN, counter, 44, 1):
                    hovered = self.myco[0]
                if self.myco[1].show_image(dimension, (237, 90), 0, WIN, counter, 44, 1):
                    hovered = self.myco[1]
                if not p.deckShow:
                    WIN.blit(pyload("Scryption_Display/Buttons/Stones.png"), (0, 0))
                    if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                        WIN.blit(pyload("Scryption_Display/Buttons/StonePress.png"), (0, 0))
            else:
                # Phase 3: get fused card
                if self.myco.show_image(dimension, (216, 90), 0, WIN, counter, 44, 1):
                    hovered = self.myco
        return hovered

    def mycoClick(self, p):
        if not isinstance(self.myco, Card) and hovCheck("rect", [(194, 90), (88, 58)], p.mousePos):
            self.myco = (1,1)
        if self.myco != (0,0):
            if self.myco == (1,1):
                if not p.deckShow:
                    # Phase 1: choose from pairs
                    for n in range(len(p.hand)):
                        if n >= len(p.hand):
                            break
                        if len(p.hand) < 9 or n == len(p.hand)-1:
                            cardSep = 54
                        else:
                            cardSep = 332 / (len(p.hand) - 1)+2
                        nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                        if hovCheck("rect", [nPos, (54, 58)], p.mousePos):
                            self.myco = p.hand[n]
            elif isinstance(self.myco, tuple):
                # Phase 2: ready pair
                if not p.deckShow and hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    newcard = Card("test", 0, 0, "0N", "N/A", [], "N/A")
                    newcard.setEqual(self.myco[0])
                    if not isinstance(newcard.power, str):
                        newcard.power += self.myco[1].power
                    newcard.health += self.myco[1].health
                    for n in self.myco[1].sigils:
                        if n not in newcard.sigils and n not in newcard.sigils2:
                            newcard.sigils.append(n)
                    for n in self.myco[1].sigils2:
                        if n not in newcard.sigils and n not in newcard.sigils2:
                            newcard.sigils2.append(n)
                    newcard.mycNum = max(newcard.mycNum, self.myco[1].mycNum) + 1
                    p.cards.remove(self.myco[0])
                    p.cards.remove(self.myco[1])
                    self.myco = newcard
            else:
                # Phase 3: get fused card
                if hovCheck("rect", [(216, 90), (44, 58)], p.mousePos):
                    p.cards.append(self.myco)
                    return True

    def goobMoment(self, p, hovered, counter, WIN):
        p = self.players[p]
        for m in range(2):
            if self.goob[m] not in [0, 1]:
                if self.goob[m].show_image(dimension, (178 + 80 * m, 98), 0, WIN, counter, 44, 1):
                    hovered = self.goob[m]
        if not p.deckShow:
            if self.goob[1] == 1:
                for i in range(len(p.hand)):
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    nPos = (240 + cardSep * (i - len(p.hand) / 2), 215)
                    if i == len(p.hand) - 1:
                        cardSep = 44
                    if p.hand[i].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                        hovered = p.hand[i]
            if self.goob[0] == 0 and self.goob[1] not in [0, 1]:
                WIN.blit(pyload("Scryption_Display/Buttons/Goob.png"), (0, 0))
                if hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                    WIN.blit(pyload("Scryption_Display/Buttons/GoobPress.png"), (0, 0))
        return hovered

    def goobClick(self, p):
        if self.goob[1] == 1:
            if not p.deckShow:
                for n in range(len(p.hand)):
                    if len(p.hand) < 9:
                        cardSep = 44
                    else:
                        cardSep = 332 / (len(p.hand) - 1) + 2
                    nPos = (240 + cardSep * (n - len(p.hand) / 2), 215)
                    if n == len(p.hand) - 1:
                        cardSep = 44
                    if hovCheck("rect", [nPos, (cardSep, 58)], p.mousePos):
                        self.goob[1] = p.hand[n]
        elif hovCheck("rect", [(258, 98), (44, 58)], p.mousePos) and self.goob[0] == 0:
            self.goob[1] = 1
            p.hand = [m for m in p.cards if m.trait != "glitch"]
        elif self.goob[1] != 0 and self.goob[0] == 0:
            if not p.deckShow and hovCheck("ellipse", [(240, 245), (64, 24)], p.mousePos):
                newcard = create_card(self.goob[1].name)
                newcard.setEqual(self.goob[1])
                if random.randint(0, 3) == 0:
                    if random.randint(0, 1) == 0:
                        newcard.power += 1
                    elif newcard.power > 0:
                        newcard.power -= 1
                elif random.randint(0, 2) == 0:
                    if random.randint(0, 1) == 0:
                        newcard.health += 1
                    elif newcard.health > 1:
                        newcard.health -= 1
                elif random.randint(0, 1) == 0 and len(newcard.sigils+newcard.sigils2) > 0:
                    randsigil = random.choice(newcard.sigils + newcard.sigils2)
                    newsigil = random.choice(sigilList2)
                    while newsigil in newcard.sigils + newcard.sigils2:
                        newsigil = random.choice(sigilList2)
                    if randsigil in newcard.sigils:
                        newcard.sigils[newcard.sigils.index(randsigil)] = newsigil
                    else:
                        newcard.sigils2[newcard.sigils2.index(randsigil)] = newsigil
                self.goob[0] = newcard
        elif hovCheck("rect", [(178, 98), (44, 58)], p.mousePos) and self.goob[0] != 0:
            p.cards.append(self.goob[0])
            return True
        return False

    def trialMoment(self, p, hovered, counter, WIN):
        if self.trial[0][0] == self.trial[0][1]:
            if self.trial[1] == 1:
                WIN.blit(pyload("Scryption_Display/Events/trialred.png"), (0, 0))
            elif self.trial[1] == 2:
                WIN.blit(pyload("Scryption_Display/Events/trialgreen.png"), (0, 0))
        if self.trial[1] == 3:
            WIN.blit(pyload("Scryption_Display/Events/trialgreen.png"), (0, 0))
        for m in range(3):
            if self.trial[1] in [1, 2]:
                if self.trial[0][0][m].show_image(dimension, (160 + m * 56, 137), 0, WIN, counter, 44, 1):
                    hovered = self.trial[0][0][m]
            else:
                if self.trial[0][m].show_image(dimension, (160 + m * 56, 137), 0, WIN, counter, 44, 1):
                    hovered = self.trial[0][m]
        return hovered

    def trialClick(self, p):
        if self.trial[1] == 0:
            # Trials
            for n in range(3):
                if hovCheck("rect", [(160 + n * 56, 137), (44, 58)], p.mousePos):
                    self.trial[0] = [[], [], self.trial[0][n].name]
                    self.trial[1] += 1
                    for m in range(3):
                        self.trial[0][0].append(create_card(""))
                        cardChose = random.choice(p.cards)
                        while cardChose in self.trial[0][1] or cardChose.name == "":
                            cardChose = random.choice(p.cards)
                        self.trial[0][1].append(cardChose)
                    trialPass = 0
                    for m in range(3):
                        if self.trial[0][2] == "Trial of Bones" and self.trial[0][1][m].cost[-1] == "N":
                            trialPass += int(self.trial[0][1][m].cost[:-1]) / 5
                        elif self.trial[0][2] == "Trial of Blood" and self.trial[0][1][m].cost[-1] == "B":
                            trialPass += int(self.trial[0][1][m].cost[:-1]) / 4
                        elif self.trial[0][2] == "Trial of Power" and isinstance(self.trial[0][1][m].power, int):
                            trialPass += self.trial[0][1][m].power / 4
                        elif self.trial[0][2] == "Trial of Health" and isinstance(self.trial[0][1][m].health, int):
                            trialPass += self.trial[0][1][m].health / 6
                        elif self.trial[0][2] == "Trial of Wisdom":
                            trialPass += len(self.trial[0][1][m].sigils + self.trial[0][1][m].sigils2) / 3
                        elif ((self.trial[0][1][m].tribe == self.trial[0][1][(m+1)%3].tribe and self.trial[0][1][m].tribe != "") or
                              (self.trial[0][1][m].name == self.trial[0][1][(m+1)%3].name)):
                            trialPass += 1
                    if trialPass >= 1:
                        self.trial[1] += 1
        elif self.trial[1] < 3:
            # Cards chosen for trial
            if self.trial[0][0] == self.trial[0][1]:
                if self.trial[1] == 2:
                    self.trial[1] += 1
                    self.trial[0] = get_cardlist("common", 3)
                    for n in range(3):
                        self.trial[0][n].sigils2 = random.sample(sigilList2, 1)
                else:
                    return True
            else:
                for n in range(3):
                    if hovCheck("rect", [(160 + n * 56, 137), (44, 58)], p.mousePos):
                        self.trial[0][0][n] = self.trial[0][1][n]
        else:
            # Cards earned for winning trial
            for n in range(3):
                if hovCheck("rect", [(160 + n * 56, 137), (44, 58)], p.mousePos):
                    p.cards.append(self.trial[0][n])
                    if p.playerNum == 1:
                        return True
                    else:
                        p.myTurn = False
                        self.players[1-self.players.index(p)].myTurn = True

    def setDefault(self):
        self.players[0].deckShow = False
        self.players[1].deckShow = False
        self.players[0].screen = self.screen
        self.players[1].screen = self.screen
        for k in range(2):
            self.players[k].hand = []
            self.players[k].deck = []
            for n in range(len(self.players[k].cards)):
                self.players[k].cards[n].deckspot = n
            if self.players[k].playerNum:
                self.players[k].myTurn = False
                self.players[k].drawn = False
            else:
                self.players[k].myTurn = True
                self.players[k].drawn = True
        # Stones
        if self.screen == "stones":
            self.stones = [0,0]
        # Fire
        elif self.screen == "fire":
            survs = get_cardlist("deathcards",5)
            for n in range(5):
                survs[n].cost = "0N"
            self.fire = [survs,0,random.choice(['p','h']),0]
        # Trader
        elif self.screen == "trader":
            wolfList = get_cardlist("common",8)
            for n in range(8):
                wolfList[n].sigils2 = [random.choice(sigilList2)]
            self.trades = [get_cardlist("common", 8), wolfList, get_cardlist("rare", 4), 0]
        # Trapper
        elif self.screen == "trapper":
            self.players[1].myTurn = True
            self.players[0].hand.append(create_card("Rabbit Pelt"))
            self.players[1].hand.append(create_card("Rabbit Pelt"))
            prices = [0,0,0]
            for n in range(3):
                prices[n] = int(n*(n-2*len(self.map)+9)/2+2)
            self.trap = [create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt"), "Skinning Knife", prices]
        # Card choice
        elif self.screen == "choose":
            self.choice = get_cardlist("common", 3)
        elif self.screen == "rarech":
            self.choice = get_cardlist("rare", 3)
        # Cost choice
        elif self.screen == "costch":
            costs = sorted(random.sample(['1','2','3','b'],3))
            costO = []
            costDisg = get_cardlist('deathcards',3)
            for n in range(3):
                costO.append(get_cardlist("cost"+costs[n],1)[0])
                costDisg[n].tribe = "XXX"
                costDisg[n].sigils = []
                costDisg[n].cost = costO[n].cost
                if costO[n].cost[-1] == "N":
                    costDisg[n].cost = "XN"
                costDisg[n].health = 'x'
                costDisg[n].power = 'x'
                costDisg[n].name = 'XXX'
                costDisg[n].trait = "secret"
            self.choiceC = [costO, costDisg, costDisg.copy()]
        # Tribe choice
        elif self.screen == "tribch":
            tribs = sorted(random.sample(['reptiles','insects','canines','avians','hooved'],3))
            tribO = []
            tribDisg = get_cardlist('deathcards',3)
            for n in range(3):
                tribO.append(get_cardlist(tribs[n],1)[0])
                tribDisg[n].tribe = tribO[n].tribe
                tribDisg[n].sigils = []
                tribDisg[n].cost = "0N"
                tribDisg[n].health = 'x'
                tribDisg[n].power = 'x'
                tribDisg[n].name = 'XXX'
                tribDisg[n].trait = "secret"
            self.choiceT = [tribO, tribDisg, tribDisg.copy()]
        # Prospector
        elif self.screen == "rocky":
            boulders = [create_card("Boulder"),create_card("Boulder"),create_card("Boulder")]
            for n in range(3):
                boulders[n].trait = "secret"
            bouldD = get_cardlist("insects",2)
            for n in range(2):
                bouldD[n].sigils2 = random.sample(sigilList2,1)
            bouldD.append(create_card("Golden Pelt"))
            random.shuffle(bouldD)
            self.prosps = [bouldD, boulders, boulders.copy()]
        # Bone lord
        elif self.screen == "bone":
            self.bone = 0
        # Goobert
        elif self.screen == "goob":
            self.goob = [0, 0]
        # Deck trial
        elif self.screen == "trial":
            trials = random.sample(["Trial of Bones","Trial of Blood","Trial of Power","Trial of Health","Trial of Wisdom","Trial of Kin"],3)
            trial2 = []
            for n in range(3):
                trial2.append(create_card("Trial"))
                trial2[n].name = trials[n]
                trial2[n].portrait = trials[n]
                if trials[n] == "Trial of Kin":
                    trial2[n].health = 2
                elif trials[n] == "Trial of Wisdom":
                    trial2[n].health = 3
                elif trials[n] in ["Trial of Power", "Trial of Blood"]:
                    trial2[n].health = 4
                elif trials[n] == "Trial of Bones":
                    trial2[n].health = 5
                else:
                    trial2[n].health = 6
            self.trial = [trial2, 0]
        else:
            for o in range(2):
                # Item
                if self.screen == "item" and not self.players[o].playerNum:
                    self.prat = create_card("Pack Rat")
                    if 0 in self.players[o].items:
                        self.prat = random.sample(itemList2, 3)
                # Woodcarver
                elif self.screen == "totem" and not self.players[o].playerNum:
                    if len(self.players[o].totparts) >= 7:
                        amal = create_card("Amalgam")
                        amal.sigils2 = [random.choice(sigilList2)]
                        self.carved = amal
                    headOpts = [n for n in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'] if n not in self.players[o].totparts]
                    if len(headOpts) >= 2:
                        sigilPow = random.randint(0,5)
                    else:
                        sigilPow = random.randint(1,5)
                    totPieces = [0,0,0]
                    for n in range(3):
                        while True:
                            if random.randint(0,1):
                                newHead = random.choice(['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'])
                                if newHead not in self.players[o].totparts and newHead not in totPieces:
                                    totPieces[n] = newHead
                                    break
                            else:
                                newSigil = []
                                for m in range(sigilPow+1):
                                    newSigil += sigilSort[m]
                                newSigil = random.choice(newSigil)
                                if newSigil not in self.players[o].totparts and newSigil not in totPieces:
                                    totPieces[n] = newSigil
                                    break
                    self.carved = totPieces
                # Mycologist
                elif self.screen == "myco" and not self.players[o].playerNum:
                    p = self.players[o]
                    used = []
                    doubles = []
                    for n in range(len(p.cards)):
                        for m in range(n, len(p.cards)):
                            if m > n and p.cards[n].name == p.cards[m].name and n not in used and m not in used:
                                doubles.append((p.cards[n],p.cards[m]))
                                used.append(n)
                                used.append(m)
                    p.hand = doubles
                    self.myco = (0,0)
                # Battle
                elif self.screen in ["battle", "battleswap"] or "Boss" in self.screen:
                    p = self.players[o]
                    p.board = [0,0,0,0]
                    p.bones = p.boneStart
                    p.squirrels = []
                    for n in range(10):
                        p.squirrels.append(create_card("Squirrel"))
                    p.damage = 0
                    if p.playerNum == 0:
                        p.myTurn = True
                    else:
                        p.myTurn = False
                    p.drawn = True
                    for n in p.cards:
                        newcard = create_card(n.name)
                        newcard.setEqual(n)
                        p.deck.append(newcard)
                    random.shuffle(p.deck)
                    p.draw_card(p.squirrels, 0)
                    # Fair hand mechanic
                    for n in range(len(p.deck)):
                        if p.deck[n].cost == "1B":
                            p.draw_card(p.deck, n)
                            break
                    while len(p.hand) < 4:
                        p.draw_card(p.deck, 0)
            if self.screen == "battleswap":
                self.players[0].deck, self.players[1].deck = self.players[1].deck, self.players[0].deck
                self.players[0].hand, self.players[1].hand = self.players[1].hand, self.players[0].hand
            self.starves = create_card("Starvation")
            self.rounds = 1
            if "Boss" in self.screen:
                self.rounds += 1
                if self.screen == "LeshyBoss":
                    self.rounds += 1
                if self.screen == "GrimoraBoss":
                    self.corpses = []

    def runGimmicks(self, p, p2, m):
        # Run Leshy's various gimmicks
        if m == 0:
            # Grimora: kills all cards, gives p corpses
            for k in range(4):
                if p.board[k] != 0:
                    newCorps = create_card(p.board[k].name)
                    newCorps.setEqual(p.board[k])
                    # Card dies
                    if p.board[k].checkSigil("Bone King"):
                        p.bones += 3
                    if p.board[k].checkSigil("Unkillable"):
                        if p.board[k].trait == "ouroboros":
                            p.board[k].power += 1
                            p.board[k].health += 1
                            if isinstance(p.board[k].deckspot, int):
                                p.cards[p.board[k].deckspot].power += 1
                                p.cards[p.board[k].deckspot].health += 1
                        p.deck.append(p.board[k])
                        p.draw_card(p.deck, -1)
                    p.board[k] = 0
                    p.bones += 1
                    for i in range(4):
                        if p2.board[i] != 0 and p2.board[i].checkSigil("Scavenger"):
                            p2.bones += 1
                            break
                    for i in range(len(p.hand)):
                        if p.hand[i].checkSigil("Corpse Eater"):
                            p2.board[k] = p2.hand[i]
                            break
                    # Turn into a corpse
                    newCorps.health = 1
                    newCorps.power = 0
                    newCorps.cost = "0N"
                    p.deck.append(newCorps)
                    p.draw_card(p.deck, -1)
        elif m == 1:
            # Leshy: puts together the card, replaces all cards in that hand with the new card
            newCard = create_card("Squirrel")
            newCard.name = "Amalgam"
            if len(p.photos) > 0:
                newCard.cost = p.photos[0][0]
                newCard.portrait = p.photos[0][1]
            if len(p.photos) > 1:
                newCard.power = p.photos[1][0]
                newCard.health = p.photos[1][1]
            if len(p.photos) > 2:
                newCard.sigils = p.photos[2][0]
                newCard.sigils2 = p.photos[2][1]
            for k in range(len(p.hand)):
                p.hand[k].setEqual(newCard)
        elif m == 2:
            # PO3: Copies best hand in p's board and fills p2's empty slots with it
            biggest = p.board[0]
            for k in range(4):
                if p.board[k] != 0:
                    if p.board[k].power+p.board[k].health > biggest.power+biggest.health:
                        biggest = p.board[k]
            for k in range(4):
                if p2.board[k] == 0:
                    p2.board[k] = create_card(biggest.name)
                    p2.board[k].setEqual(biggest)
        else:
            # Magnificus: Every turn, will replace all sigils on p2's board with [random.choice(sigilList2)]
            p2.paint = True

