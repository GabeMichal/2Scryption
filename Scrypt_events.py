from Scrypt_player import *
from Scrypt_card import *
from Scrypt_pygame import WIN, mainScreen

def get_eventVar(screen, p, mapNum):
    p.hand = []
    p.deck = []
    for n in range(len(p.cards)):
        p.cards[n].deckspot = n
    if screen == "stones":
        return [0,0]
    elif screen == "fire":
        survs = get_cardlist("deathcards",5)
        for n in range(5):
            survs[n].cost = "0N"
        return [survs,0,random.choice(['p','h']),0]
    elif screen == "trader":
        wolfList = get_cardlist("common",8)
        for n in range(8):
            wolfList[n].sigils = [random.choice(sigilList2)]
        return [get_cardlist("common", 8), wolfList, get_cardlist("rare", 4), 0]
    elif screen == "trapper":
        p.hand.append(create_card("Rabbit Pelt"))
        prices = [0,0,0]
        for n in range(3):
            prices[n] = n*(n+2*mapNum+3)/2+2
        return [create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt"), "Skinning Knife", prices]
    elif screen == "choose":
        return get_cardlist("common", 3)
    elif screen == "costch":
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
        return [costO, costDisg]
    elif screen == "tribch":
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
        return [tribO, tribDisg]
    elif screen == 'rocky':
        boulders = [create_card("Boulder"),create_card("Boulder"),create_card("Boulder")]
        for n in range(3):
            boulders[n].trait = "secret"
        bouldD = get_cardlist("insects",2)
        for n in range(2):
            bouldD[n].sigils2 = random.sample(sigilList2,1)
        bouldD.append(create_card("Golden Pelt"))
        random.shuffle(bouldD)
        return [bouldD, boulders]
    elif screen == "item":
        if 0 not in p.items:
            return create_card("Pack Rat")
        return random.sample(itemList2, 3)
    elif screen == 'bone':
        return 0
    elif screen == 'totem':
        if len(p.totparts) >= 7:
            amal = create_card("Amalgam")
            amal.sigils2 = [random.choice(sigilList2)]
            return amal
        headOpts = [n for n in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'] if n not in p.totparts]
        if len(headOpts) >= 2:
            sigilPow = random.randint(0,5)
        else:
            sigilPow = random.randint(1,5)
        totPieces = [0,0,0]
        for n in range(3):
            while True:
                if random.randint(0,1):
                    newHead = random.choice(['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'])
                    if newHead not in p.totparts and newHead not in totPieces:
                        totPieces[n] = newHead
                        break
                else:
                    newSigil = []
                    for m in range(sigilPow+1):
                        newSigil += sigilSort[m]
                    newSigil = random.choice(newSigil)
                    if newSigil not in p.totparts and newSigil not in totPieces:
                        totPieces[n] = newSigil
                        break
        return totPieces
    elif screen == 'myco':
        namesidk = []
        doubles = []
        for n in range(len(p.cards)):
            for m in range(n, len(p.cards)):
                if m != n and p.cards[n].name == p.cards[m].name and p.cards[m].name not in namesidk:
                    doubles.append((p.cards[n],p.cards[m]))
                    namesidk.append(p.cards[n].name)
        return [(0,0), doubles]
    elif screen == 'goob':
        return [0,0]
    elif screen == 'trial':
        trials = random.sample(["Trial of Bones", "Trial of Blood", "Trial of Power", "Trial of Health", "Trial of Wisdom", "Trial of Kin"],3)
        trial2 = []
        for n in range(3):
            trial2.append(create_card(""))
            trial2[n].name = trials[n]
        return [trial2,0]
    elif screen == 'battle':
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
            p.deck.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.trait))
            p.deck[p.cards.index(n)].setEqual(n)
        random.shuffle(p.deck)
        p.draw_card(p.squirrels)
        # Fair hand mechanic
        for n in range(len(p.deck)):
            if p.deck[n].cost == "1B":
                card = p.deck.pop(n)
                if card.name == "":
                    card = get_cardlist("common",1)[0]
                if "Finical Hatchling" in card.sigils+card.sigils2:
                    fhpows = [0, 0, 0, 0, 0]
                    fhhelt = [0, 0, 0, 0, 0]
                    fhtrib = [0, 0, 0, 0, 0]
                    for n in p.cards:
                        if n.power > 0 and n.power < 6:
                            fhpows[n-1]+=1
                        if n.health > 0 and n.health < 6:
                            fhhelt[n-1]+=1
                        if n.tribe == "Reptile":
                            fhtrib[0]+=1
                        if n.tribe == "Insect":
                            fhtrib[1]+=1
                        if n.tribe == "Avian":
                            fhtrib[2]+=1
                        if n.tribe == "Canine":
                            fhtrib[3]+=1
                        if n.tribe == "Hooved":
                            fhtrib[4]+=1
                    if 0 not in fhpows and 0 not in fhhelt and 0 not in fhtrib:
                        p.cards[card.deckspot] = create_card("Hydra")
                        card = create_card("Hydra")
                if len(p.totem) == 2:
                    if p.totem[0] == card.tribe:
                        card.sigilTem = p.totem[1]
                while "Amorphous" in card.sigils:
                    card.sigils[card.sigils.index("Amorphous")] = random.choice(sigilList2)
                while "Amorphous" in card.sigils2:
                    card.sigils2[card.sigils2.index("Amorphous")] = random.choice(sigilList2)
                while card.sigilTem == "Amorphous":
                    card.sigilTem = random.choice(sigilList2)
                p.hand.append(card)
                break
        for n in range(2):
            p.draw_card(p.deck)
        return {}
    elif screen == "hoard":
        for n in range(len(p.deck)):
            if p.deck[n].trait == "ijiraq":
                while p.deck[n].trait == "ijiraq":
                    p.deck[n].setEqual(random.choice(p.deck))
                p.deck[n].trait = "ijiraq"
    return 0

def passCheck(p, p2, n, m):
    # Determines if the attack will pass the other card
    # p = attacker, p2 = defender, n = atkspace, m = defspace
    if p2.board[m] == 0:
        return True
    if p2.board[m].checkSigil("Waterborne"):
        return True
    if ((p.board[n] != 0 and p.board[n].checkSigil("Airborne")) or p.harpyActive) and not p2.board[m].checkSigil("Mighty Leap"):
        return True
    return False

def battleMoment(p, p2, hovered, counter, ver):
    for n in range(4):
        nPos = (150+(n*44),137)
        if p.board[n] != 0:
            # Set variable powers
            if p.board[n].tempPow == "antpow":
                p.board[n].power = 0
                for m in range(4):
                    if p.board[m] != 0 and p.board[m].trait == "ant":
                        p.board[n].power += 1
            elif p.board[n].tempPow == "mirrpow":
                if p2.board[3-n] == 0:
                    p.board[n].power = 0
                else:
                    p.board[n].power = p2.board[3-n].power
            elif p.board[n].tempPow == "cardpow":
                p.board[n].power = len(p.hand)
            elif p.board[n].tempPow == "bellpow":
                p.board[n].power = 4-n
                for m in range(4):
                    if p.board[m].trait == "chime":
                        p.board[n].power = max(p.board[n].power, 5-abs(n-m))
            elif p.board[n].tempPow == "bonpow":
                p.board[n].power = int(p.bones/2)
            elif p.board[n].tempPow == "blodpow":
                p.board[n].power = p.sacNum
            if p.board[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = p.board[n]
        if p2.board[3-n] != 0:
            if p2.board[3-n].show_image(dimension, (nPos[0],nPos[1]-64), 0, WIN, counter, 44, 1):
                hovered = p2.board[3-n]
    if ver == "hoard":
        for n in range(len(p.eventVar)):
            if n == len(p.eventVar)-1 or len(p.eventVar) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.eventVar)-1)+2
            if p.eventVar[n].show_image(dimension, (240+cardSep*(n-len(p.eventVar)/2),215), 0, WIN, counter, cardSep, 1):
                hovered = p.eventVar[n]
    else:
        for n in range(len(p.hand)):
            if n == len(p.hand)-1 or len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            if p.hand[n].show_image(dimension, (240+cardSep*(n-len(p.hand)/2),215), 0, WIN, counter, cardSep, 1):
                hovered = p.hand[n]
        if ver == "battle" and not p.myTurn:
            WIN.blit(pyload("Scryption_Display/notMyTurn.png"), (0,0))
    return hovered

def battleClick(p, p2, net):
    if p.drawn and p.myTurn:
        for n in range(len(p.hand)):
            # Play a card
            if n >= len(p.hand):
                break
            if p.hand[n].selected:
                for m in range(4):
                    if hovCheck("rect", [(150+m*44,137),(44,56)]):
                        if p.cursorMode == "sacrifice" and p.board[m] != 0 and not p.board[m].marked:
                            if p.board[m].trait != "terrain" and p.board[m].trait != "chime" and p.board[m].trait != "pelt":
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
                                                p.hand[n].power+=p.board[k].power
                                                p.hand[n].health+=p.board[k].health
                                            if "cat" in p.board[k].trait and p.board[k].checkSigil("Many Lives"):
                                                p.board[k].trait = p.board[k].trait[0:2]+str(int(p.board[k].trait[-1])+1)
                                                if p.board[k].trait == "cat9":
                                                    keepcat = p.board[k]
                                                    p.board[k] = keepcat.create_card("Undead Cat")
                                                    p.board[k].power += keepcat.power
                                                    p.board[k].health += keepcat.health-1
                                                    p.board[k].sigils += keepcat.sigils
                                                    p.board[k].sigils2 += keepcat.sigils2
                                                    p.board[k].sigils.remove("Many Lives")
                                            elif "child" in p.board[k].trait and p.board[k].checkSigil("Many Lives"):
                                                p.board[k].trait = p.board[k].trait[0:5]+str(int(p.board[k].trait[5:])+1)
                                                if int(p.board[k].trait[5:]) % 2 == 1:
                                                    p.board[k].power += 2
                                                    p.board[k].sigils.append("Airborne")
                                                else:
                                                    p.board[k].power -= 2
                                                    p.board[k].sigils.remove("Airborne")
                                                if p.board[k].trait == "child13":
                                                    p.board[k] = p.board[k].create_card("Hungry Child")
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
                                                    p.hand.append(p.board[k])
                                                p.board[k] = 0
                                                p.bones += 1
                                                p.comms["death"] += 1
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
                            if p.hand[n].cost[-1] == "N":
                                if p.bones >= int(p.hand[n].cost[:-1]):
                                    p.bones -= int(p.hand[n].cost[:-1])
                                    p.board[m] = p.hand.pop(n)
                            else:
                                p.board[m] = p.hand.pop(n)
                            if p.board[m].checkSigil("Rabbit Hole"):
                                p.hand.append(p.board[m].create_card("Rabbit"))
                            if p.board[m].checkSigil("Dam Builder"):
                                if m != 3 and p.board[m+1] == 0:
                                    p.board[m+1] = p.board[m].create_card("Dam")
                                if m != 0 and p.board[m-1] == 0:
                                    p.board[m-1] = p.board[m].create_card("Dam")
                            if p.board[m].checkSigil("Bellist"):
                                if m != 3 and p.board[m+1] == 0:
                                    p.board[m+1] = p.board[m].create_card("Chime")
                                if m != 0 and p.board[m-1] == 0:
                                    p.board[m-1] = p.board[m].create_card("Chime")
                            if p.board[m].checkSigil("Hoarder") and len(p.deck) > 0:
                                for k in range(len(p.deck)):
                                    if p.deck[n].trait == "ijiraq":
                                        while p.deck[n].trait == "ijiraq":
                                            p.deck[n].setEqual(random.choice(p.deck))
                                        p.deck[n].trait = "ijiraq"
                                mainScreen(net)
                            if p.board[m].checkSigil("Fecundity"):
                                newCard = p.board[m].create_card(p.board[m].name)
                                newCard.setEqual(p.board[m])
                                if "Fecundity" in newCard.sigils:
                                    newCard.sigils.remove("Fecundity")
                                elif "Fecundity" in newCard.sigils2:
                                    newCard.sigils2.remove("Fecundity")
                                p.hand.append(newCard)
                            if p.board[m].checkSigil("Ant Spawner"):
                                p.hand.append(p.board[m].create_card("Worker Ant"))
                            if p.board[m].checkSigil("Brood Parasite"):
                                if p2.board[m] == 0:
                                    if random.randint(1, 10) == 10:
                                        p.comms["egged"] = [p.board[m].create_card("Raven Egg"),m]
                                    else:
                                        p.comms["egged"] = [p.board[m].create_card("Broken Egg"),m]
                            if p.board[m].checkSigil("Trinket Bearer") and 0 in p.items:
                                p.items[p.items.index(0)] = random.choice(itemList)
                            p.comms["playPlace"] = m
                            if p.board[m].name in ["Rabbit Pelt", "Wolf Pelt", "Golden Pelt"]:
                                for k in range(len(p.hand)):
                                    if p.hand[k].name == "Pelt Lice":
                                        if m != 0:
                                            if p.board[m-1] == 0:
                                                p.board[m-1] = p.hand.pop(k)
                                            continue
                                        if m != 3:
                                            if p.board[m+1] == 0:
                                                p.board[m+1] = p.hand.pop(k)
                                for k in range(len(p.deck)):
                                    if p.deck[k].name == "Pelt Lice":
                                        if m != 0:
                                            if p.board[m-1] == 0:
                                                p.board[m-1] = p.deck.pop(k)
                                            continue
                                        if m != 3:
                                            if p.board[m+1] == 0:
                                                p.board[m+1] = p.deck.pop(k)
                            if p.board[m].trait == "ijiraq":
                                p.board[m] = create_card("Ijiraq")
                            p.board[m].selected = False
                        break
                if not hovCheck("rect", [(150,137),(176,56)]):
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
                    cardSep = 332/(len(p.hand)-1)+2
                n_cp = (240+cardSep*(n-len(p.hand)/2),215)
                if n == len(p.hand)-1:
                    cardSep = 44
                if hovCheck("rect",[n_cp,(cardSep,58)]):
                    p.hand[n].selected = True
                    p.hand[n].counter = 0
                    if p.hand[n].cost[-1] == "B":
                        p.cursorMode = "sacrifice"
                    break
        if hovCheck("rect", [(50,77),(91,36)]):
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
                                    targets.append(n+1)
                                if n < 3:
                                    targets.append(n-1)
                            if trif:
                                targets.append(n)
                                if n > 0:
                                    targets.append(n+1)
                                if n < 3:
                                    targets.append(n-1)
                        else:
                            targets.append(n)
                        targs = []
                        for m in targets:
                            burred = False
                            if passCheck(p, p2, n, 3-m):
                                for k in range(4):
                                    if p.board[k] != 0 and p.board[k].checkSigil("Burrower") and not passCheck(p, p2, n, 3-k) and p.board[m] == 0:
                                        burred = True
                                        break
                                if not burred:
                                    p.damage += p.board[n].power
                            if not passCheck(p, p2, n, 3-m) or burred:
                                targs.append([m, p.board[n].power])
                        p.comms["attack"][n] = targs
                    if p.board[n].checkSigil("Bone Digger"):
                        # Dig for bones
                        p.bones += 1
                    # Move
                    moveNum = 0
                    if p.board[n].checkSigil("Sprinter") or p.board[n].checkSigil("SprinterL"):
                        moveNum += 1
                    if p.board[n].checkSigil("Rampager") or p.board[n].checkSigil("RampagerL"):
                        moveNum += 1
                    if p.board[n].checkSigil("Hefty") or p.board[n].checkSigil("HeftyL"):
                        moveNum += 1
                    for m in range(moveNum):
                        if p.board[n].checkSigil("Rampager"):
                            if n == 3:
                                temp = p.board[n-1]
                                if temp == 0 and p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                p.board[n-1] = p.board[n]
                                p.board[n] = temp
                                if "Rampager" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("Rampager")] = "RampagerL"
                                elif "Rampager" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("Rampager")] = "RampagerL"
                                else:
                                    p.board[n].sigilTem = "RampagerL"
                            else:
                                temp = p.board[n+1]
                                if temp == 0 and p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                p.board[n+1] = p.board[n]
                                p.board[n] = temp
                        elif p.board[n].checkSigil("RampagerL"):
                            if n == 0:
                                temp = p.board[n+1]
                                if temp == 0 and p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                p.board[n+1] = p.board[n]
                                p.board[n] = temp
                                if "RampagerL" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("RampagerL")] = "Rampager"
                                elif "RampagerL" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("RampagerL")] = "Rampager"
                                else:
                                    p.board[n].sigilTem = "Rampager"
                            else:
                                temp = p.board[n-1]
                                if temp == 0 and p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                p.board[n-1] = p.board[n]
                                p.board[n] = temp
                        elif p.board[n].checkSigil("Hefty"):
                            hefmov = False
                            for k in range(4-n):
                                if p.board[n+k] == 0:
                                    hefmov = True
                            if hefmov:
                                temp = 0
                                if p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                for k in range(4-n):
                                    p.board[n+k], temp = temp, p.board[n+k]
                                    if temp == 0:
                                        break
                            else:
                                if "Hefty" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("Hefty")] = "HeftyL"
                                elif "Hefty" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("Hefty")] = "HeftyL"
                                else:
                                    p.board[n].sigilTem = "HeftyL"
                                for k in range(n):
                                    if p.board[k] == 0:
                                        hefmov = True
                                if hefmov:
                                    temp = 0
                                    if p.board[n].trait == "long elk":
                                        temp = p.board[n].create_card("Vertebrae")
                                    for k in range(n):
                                        p.board[n-k], temp = temp, p.board[n-k]
                                        if temp == 0:
                                            break
                        elif p.board[n].checkSigil("HeftyL"):
                            hefmov = False
                            for k in range(n):
                                if p.board[k] == 0:
                                    hefmov = True
                            if hefmov:
                                temp = 0
                                if p.board[n].trait == "long elk":
                                    temp = p.board[n].create_card("Vertebrae")
                                for k in range(n):
                                    p.board[n-k], temp = temp, p.board[n-k]
                                    if temp == 0:
                                        break
                            else:
                                if "HeftyL" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("HeftyL")] = "Hefty"
                                elif "HeftyL" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("HeftyL")] = "Hefty"
                                else:
                                    p.board[n].sigilTem = "Hefty"
                                for k in range(4-n):
                                    if p.board[n+k] == 0:
                                        hefmov = True
                                if hefmov:
                                    temp = 0
                                    if p.board[n].trait == "long elk":
                                        temp = p.board[n].create_card("Vertebrae")
                                    for k in range(4-n):
                                        p.board[n+k], temp = temp, p.board[n+k]
                                        if temp == 0:
                                            break
                        elif p.board[n].checkSigil["Sprinter"]:
                            if n < 3 and p.board[n+1] == 0:
                                p.board[n+1] = p.board[n]
                                p.board[n] = 0
                                if p.board[n+1].trait == "long elk":
                                    p.board[n] = p.board[n+1].create_card("Vertebrae")
                            else:
                                if "Sprinter" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("Sprinter")] = "SprinterL"
                                elif "Sprinter" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("Sprinter")] = "SprinterL"
                                else:
                                    p.board[n].sigilTem = "SprinterL"
                                if n > 0 and p.board[n-1] == 0:
                                    p.board[n-1] = p.board[n]
                                    p.board[n] = 0
                                    if p.board[n-1].trait == "long elk":
                                        p.board[n] = p.board[n-1].create_card("Vertebrae")
                        elif p.board[n].checkSigil["SprinterL"]:
                            if n > 0 and p.board[n-1] == 0:
                                p.board[n-1] = p.board[n]
                                p.board[n] = 0
                                if p.board[n-1].trait == "long elk":
                                    p.board[n] = p.board[n-1].create_card("Vertebrae")
                            else:
                                if "SprinterL" in p.board[n].sigils:
                                    p.board[n].sigils[p.board[n].sigils.index("SprinterL")] = "Sprinter"
                                elif "SprinterL" in p.board[n].sigils2:
                                    p.board[n].sigils[p.board[n].sigils.index("SprinterL")] = "Sprinter"
                                else:
                                    p.board[n].sigilTem = "Sprinter"
                                if n < 3 and p.board[n+1] == 0:
                                    p.board[n+1] = p.board[n]
                                    p.board[n] = 0
                                    if p.board[n+1].trait == "long elk":
                                        p.board[n] = p.board[n+1].create_card("Vertebrae")
            # Done with everything so...
            p.myTurn = False
            p.drawn = False
            p.harpyActive = False
            p.comms["bell"] = True
        for n in range(3):
            # Use an item
            if p.items[n] != 0 and hovCheck("rect", [(360+26*n, 131), (25,50)]):
                if p.items[n] == "Boulder in a Bottle":
                    p.hand.append(create_card("Boulder"))
                elif p.items[n] == "Squirrel in a Bottle":
                    p.hand.append(create_card("Squirrel"))
                elif p.items[n] == "Black Goat in a Bottle":
                    p.hand.append(create_card("Black Goat"))
                elif p.items[n] == "Frozen Opossum in a Bottle":
                    p.hand.append(create_card("Frozen Opossum"))
                elif p.items[n] == "Pliers":
                    p.damage += 1
                elif p.items[n] == "Hoggy Bank":
                    p.bones += 4
                elif p.items[n] == "Fish Hook":
                    mainScreen(net)
                elif p.items[n] == "Harpie's Birdleg Fan":
                    p.harpyActive = True
                elif p.items[n] == "Magickal Bleach":
                    p.comms["bleached"] = True
                elif p.items[n] == "Magpie's Lens":
                    mainScreen(net)
                elif p.items[n] == "Skinning Knife" or p.items[n] == "Scissors":
                    if mainScreen(net) and p.items[n] == "Skinning Knife":
                        p.hand.append(create_card("Wolf Pelt"))
    elif p.myTurn:
        # Pick a deck to draw from
        if hovCheck("rect", [(356,188),(30,19)]):
            p.draw_card(p.deck)
            p.drawn = True
        elif hovCheck("rect", [(399,188),(35,19)]):
            p.draw_card(p.squirrels)
            p.drawn = True

def hoardClick(p):
    for n in range(len(p.eventVar)):
        if n == len(p.eventVar)-1 or len(p.eventVar) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(p.eventVar)-1)+2
        n_cp = (240+cardSep*(n-len(p.eventVar)/2),215)
        if hovCheck("rect", [n_cp, (cardSep,58)]):
            p.hand.append(p.eventVar.pop(n))
            p.deck.pop(n)
            return True

def hookClick(p, p2):
    for n in range(4):
        n_cp = (150+(n*44),74)
        if hovCheck("rect", [n_cp, (44,58)]):
            if p2.board[3-n] != 0 and p.board[n] == 0 and p2.board[3-n].trait not in ["uncuttable", "pack mule"]:
                p.board[n] = p2.board[3-n]
                p2.board[3-n] = 0
    return True

def stoneMoment(p, hovered, counter):
    for n in range(2):
        if p.eventVar[n] not in [0,1]:
            nPos = ((215-7*n),(59+74*n))
            if p.eventVar[n].show_image(dimension, nPos, n, WIN, counter, 44, 1):
                hovered = p.eventVar[n]
    if p.eventVar[0] not in [0,1] and p.eventVar[1] not in [0,1]:
        WIN.blit(pyload("Scryption_Display/Buttons/Stones.png"),(0,0))
        if hovCheck("ellipse", [(240,245),(64,24)]):
            WIN.blit(pyload("Scryption_Display/Buttons/StonePress.png"),(0,0))
    else:
        if p.eventVar[0] == 1:
            p.hand = [n for n in p.cards if len(n.sigils2) == 0 and n != p.eventVar[1]]
        if p.eventVar[1] == 1:
            p.hand = [n for n in p.cards if len(n.sigils2) == 0 and n != p.eventVar[0] and len(n.sigils) != 0]
        if p.eventVar[0] == 1 or p.eventVar[1] == 1:
            for n in range(len(p.hand)):
                if len(p.hand) < 9:
                    cardSep = 44
                else:
                    cardSep = 332/(len(p.deck)-1)+2
                nPos = (240+cardSep*(n-len(p.hand)/2), 215)
                if n == len(p.hand)-1:
                    cardSep = 44
                if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                    hovered = p.hand[n]
    return hovered

def stoneClick(p):
    for m in range(2):
        if hovCheck("rect", [(215-7*m,59+74*m),(44+14*m,58-14*m)]):
            if p.eventVar[abs(m-1)] != 1:
                p.eventVar[m] = 1
    if p.eventVar[0] == 1 or p.eventVar[1] == 1:
        for n in range(len(p.hand)):
            if n >= len(p.hand):
                break
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            n_cp = (240+cardSep*(n-len(p.hand)/2),215)
            if n == len(p.hand)-1:
                cardSep = 44
            if hovCheck("rect", [n_cp, (cardSep, 58)]):
                if p.eventVar[0] == 1:
                    p.eventVar[0] = p.hand[n]
                if p.eventVar[1] == 1:
                    p.eventVar[1] = p.hand[n]
    else:
        if hovCheck("ellipse", [(240,245),(64,24)]):
            p.eventVar[0].sigils2 = p.eventVar[1].sigils
            p.eventVar[1] = 0
            p.cards[p.eventVar[0].deckspot] = p.eventVar[0]
            p.eventVar[0] = 0
            return True

def fireMoment(p, hovered, counter):
    for n in range(5):
        nPos = (int(68*math.sin(0.29*n*math.pi-math.pi*0.58)+216),int(-68*math.cos(0.29*n*math.pi-math.pi*0.58)+110))
        p.eventVar[0][n].show_image(dimension, nPos, 0, WIN, counter, 44, 0)
    if p.eventVar[1] == 1:
        for n in range(len(p.hand)):
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            nPos = (240+cardSep*(n-len(p.hand)/2), 215)
            if n == len(p.hand)-1:
                cardSep = 44
            if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                hovered = p.hand[n]
    elif p.eventVar[1] != 0:
        firPos = (216,112)
        if p.eventVar[1].show_image(dimension, firPos, 0, WIN, counter, 44, 1):
            hovered = p.eventVar[1]
        WIN.blit(pyload("Scryption_Display/Buttons/Fire.png"),(0,0))
        if hovCheck("ellipse", [(240,245),(64,24)]):
            WIN.blit(pyload("Scryption_Display/Buttons/FirePress.png"),(0,0))
    return hovered

def fireClick(p):
    if hovCheck("rect", [(216,112),(44,58)]):
        if p.eventVar[1] == 0:
            p.eventVar[1] = 1
            p.hand = [n for n in p.cards if n.trait != "glitch"]
        if p.eventVar[3] >= 1:
            return True
    if p.eventVar[1] == 1:
        for n in range(len(p.hand)):
            if n >= len(p.hand):
                break
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            n_cp = (240+cardSep*(n-len(p.hand)/2),215)
            if n == len(p.hand)-1:
                cardSep = 44
            if hovCheck("rect", [n_cp, (cardSep,58)]):
                p.eventVar[1] = p.hand[n]
    elif hovCheck("ellipse", [(240,245),(64,24)]):
        if p.eventVar[2] == 'p':
            p.eventVar[1].power += 1
        else:
            p.eventVar[1].health += 2
        if p.eventVar[3] > 0:
            if random.randint(0,1) == 0:
                p.cards.pop(p.eventVar[1].deckspot)
                p.eventVar[1] = 0
                if 0 in p.items:
                    p.items[p.items.index(0)] = "Hoggy Bank"
            return True
        p.eventVar[3] += 1

def tradeMoment(p, hovered, counter):
    if p.eventVar[3] == 0:
        p.hand = [n for n in p.cards if n.name == "Rabbit Pelt"]
    elif p.eventVar[3] == 1:
        p.hand = [n for n in p.cards if n.name == "Wolf Pelt"]
    else:
        p.hand = [n for n in p.cards if n.name == "Golden Pelt"]
    for n in range(4*(2-int(p.eventVar[3]/2))):
        if p.eventVar[p.eventVar[3]][n] != 0:
            nPos = ((150+(n%4)*44),(73+int(n/4)*64))
            if p.eventVar[p.eventVar[3]][n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = p.eventVar[p.eventVar[3]][n]
    for n in range(len(p.hand)):
        if len(p.hand) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(p.hand)-1)+2
        nPos = (240+cardSep*(n-len(p.hand)/2),215)
        if n == len(p.hand)-1:
            cardSep = 44
        if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
            hovered = p.hand[n]
    return hovered

def tradeClick(p):
    for n in range(4*(2-int(p.eventVar[3]/2))):
        if hovCheck("rect", [(150+(n%4)*44,73+int(n/4)*64),(44,58)]) and p.eventVar[p.eventVar[3]][n] != 0:
            p.cards.append(p.eventVar[p.eventVar[3]][n])
            p.eventVar[p.eventVar[3]][n] = 0
            p.cards.remove(p.hand.pop(0))
            if len(p.eventVar[p.eventVar[3]]) == 0:
                if p.eventVar[3] == 0:
                    p.eventVar[0] = get_cardlist("common", 8)
                elif p.eventVar[3] == 1:
                    p.eventVar[1] = get_cardlist("common", 8)
                elif p.eventVar[3] == 2:
                    p.eventVar[2] = get_cardlist("rare", 4)
            if len(p.hand) == 0:
                p.eventVar[3] += 1
                if p.eventVar[3] >= 3:
                    return True

def trapMoment(p, hovered, counter):
    WIN.blit(pyload("Scryption_Display/InItems/Skinning_Knife.png"), (159*dimension, 141*dimension))
    if hovCheck("rect", [(159,131),(25,50)]):
        WIN.blit(pyload("Scryption_Display/HovItems/Skinning_Knife.png"), (159*dimension, 141*dimension))
    for n in range(3):
        nPos = (194+n*44,138)
        if p.eventVar[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
            hovered = p.eventVar[n]
    for n in range(len(p.hand)):
        if len(p.hand) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(p.hand)-1)+2
        nPos = (240+cardSep*(n-len(p.hand)/2),215)
        if n == len(p.hand)-1:
            cardSep = 44
        if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
            hovered = p.hand[n]
    return hovered

def trapClick(p):
    for n in range(3):
        if hovCheck("rect", [(194+n*44,138),(44,58)]):
            if p.eventVar[4][n] <= p.teeth:
                p.hand.append(create_card(p.eventVar[n].name))
                p.teeth -= p.eventVar[4][n]
    if hovCheck("rect", [(159,141),(25,50)]) and 0 in p.items and p.teeth >= 7:
        p.items[p.items.index(0)] = "Skinning Knife"
        p.teeth -= 7
    for n in range(len(p.hand)):
        if n >= len(p.hand):
            break
        if len(p.hand) < 9:
            cardSep = 44
        else:
            cardSep = 332/(len(p.hand)-1)+2
        n_cp = (240+cardSep*(n-len(p.hand)/2),215)
        if n == len(p.hand)-1:
            cardSep = 44
        if hovCheck("rect", [n_cp, (cardSep, 58)]):
            return True

def cardMoment(p, hovered, counter):
    for n in range(3):
        if p.eventVar[n] != 0:
            nPos = ((160+n*56),90)
            if p.eventVar[n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = p.eventVar[n]
    return hovered

def cardClick(p):
    for n in range(3):
        if hovCheck("rect", [(160+n*56,90),(44,58)]) and p.eventVar[n] != 0:
            p.cards.append(p.eventVar[n])
            return True

def cardSecMoment(p, hovered, counter):
    for n in range(3):
        if p.eventVar[1][n] != 0:
            nPos = (160+n*56,90)
            if p.eventVar[1][n].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = p.eventVar[1][n]
    return hovered

def cardSecClick(p):
    for n in range(3):
        if hovCheck("rect", [(160+n*56,90),(44,58)]) and p.eventVar[1][n] != 0:
            if p.eventVar[1][n].trait != "secret":
                p.cards.append(p.eventVar[1][n])
                return True
            p.eventVar[1][n] = p.eventVar[0][n]
            p.eventVar[1][(n+2)%3] = 0
            p.eventVar[1][(n+4)%3] = 0

def itemMoment(p, hovered, counter):
    if isinstance(p.eventVar, Card):
        if p.eventVar.show_image(dimension, (216, 112), 0, WIN, counter, 44, 1):
            hovered = p.eventVar
    elif 0 in p.items:
        for n in range(3):
            if p.eventVar[n] != 0:
                nPos = (170+56*n,122)
                WIN.blit(pyload("Scryption_Display/InItems/"+"_".join(p.eventVar[n].split())+".png"), (nPos[0]*dimension, nPos[1]*dimension))
                if hovCheck("rect", [nPos,(25,50)]):
                    WIN.blit(pyload("Scryption_Display/HovItems/"+"_".join(p.eventVar[n].split())+".png"), (nPos[0]*dimension, nPos[1]*dimension))
    return hovered

def itemClick(p, p2):
    for n in range(3):
        if p.items[n] != 0 and hovCheck("rect", [(360+26*n, 131), (25,50)]):
            p.items[n] = 0
    if isinstance(p.eventVar, Card):
        if hovCheck("rect", [(216,112), (44,58)]):
            p.cards.append(p.eventVar)
            return True
    elif 0 in p.items:
        for n in range(3):
            nPos = (170+56*n,122)
            if hovCheck("rect", [nPos,(25,50)]):
                p.items[p.items.index(0)] = p.eventVar[n]
                p.eventVar = random.sample(itemList2, 3)
    if 0 not in p.items and 0 not in p2.items and not isinstance(p.eventVar, Card):
        return True
    return False

def boneMoment(p, hovered, counter):
    p.hand = [n for n in p.cards if n.trait != "glitch"]
    if p.eventVar == 1:
        for n in range(len(p.hand)):
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            nPos = (240+cardSep*(n-len(p.hand)/2), 215)
            if n == len(p.hand)-1:
                cardSep = 44
            if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                hovered = p.hand[n]
    elif p.eventVar != 0:
        bonPos = (216,112)
        if p.eventVar.show_image(dimension, bonPos, 0, WIN, counter, 44, 1):
            hovered = p.eventVar
        WIN.blit(pyload("Scryption_Display/Buttons/Bone.png"),(0,0))
        if hovCheck("ellipse", [(240,245),(64,24)]):
            WIN.blit(pyload("Scryption_Display/Buttons/BonePress.png"),(0,0))
    return hovered

def boneClick(p):
    if p.eventVar == 1:
        for n in range(len(p.hand)):
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            nPos = (240+cardSep*(n-len(p.hand)/2), 215)
            if n == len(p.hand)-1:
                cardSep = 44
            if hovCheck("rect", [nPos,(cardSep,58)]):
                p.eventVar = p.hand[n]
    elif p.eventVar != 0 and hovCheck("ellipse", [(240,245),(64,24)]):
        p.cards.pop(p.eventVar.deckspot)
        if p.eventVar.name not in ["Golden Pelt", "Wolf Pelt", "Rabbit Pelt"]:
            p.boneStart += 1
        if p.eventVar.trait == "goat":
            p.boneStart += 7
        return True
    else:
        if hovCheck("rect", [(216,112),(58,44)]):
            p.eventVar = 1
    return False

def toteMoment(p, hovered, counter):
    if isinstance(p.eventVar,Card):
        if p.eventVar.show_image(dimension, (216, 90), 0, WIN, counter, 44, 1):
            hovered = p.eventVar
    else:
        if 0 in p.eventVar:
            listComp = p.totparts
        else:
            listComp = p.eventVar
        for n in range(len(listComp)):
            nPos = (170+(n%3)*56,70+30*int(n/3))
            if listComp[n] in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile'] and listComp[n] != p.totem[0]:
                nPos = (nPos[0],nPos[1]+24)
                WIN.blit(pyload("Scryption_Display/InTotems/"+listComp[n]+".png"),(nPos[0]*dimension,nPos[1]*dimension))
                if hovCheck("rect", [nPos,(25,25)]):
                    WIN.blit(pyload("Scryption_Display/HovTotems/"+listComp[n]+".png"),(nPos[0]*dimension,nPos[1]*dimension))
            elif listComp[n] in sigilList and listComp[n] != p.totem[1]:
                WIN.blit(pyload("Scryption_Display/InTotems/Base.png"),(nPos[0]*dimension,nPos[1]*dimension))
                if hovCheck("rect", [(nPos[0],nPos[1]+24),(25,25)]):
                    WIN.blit(pyload("Scryption_Display/HovTotems/Base.png"),(nPos[0]*dimension,nPos[1]*dimension))
                thisSigil = sigilSpriteO[sigilList.index(listComp[n])]
                sigilSize = thisSigil.get_size()
                sigilImage = pygame.transform.scale(thisSigil, (sigilSize[0]*dimension, sigilSize[1]*dimension))
                WIN.blit(sigilImage,((nPos[0]+4)*dimension,(nPos[1]+27)*dimension))
    return hovered

def toteClick(p):
    if isinstance(p.eventVar, Card):
        if hovCheck("rect", [(216,90), (44,58)]):
            p.cards.append(p.eventVar)
            p.eventVar = [0]
            p.totem = [0,0]
    else:
        if 0 in p.eventVar:
            listLen = len(p.totparts)
        else:
            listLen = len(p.eventVar)
        for n in range(listLen):
            nPos = (170+(n%3)*56,94+30*int(n/3))
            if hovCheck("rect", [nPos, (25,25)]):
                if 0 in p.eventVar:
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
                    p.totparts.append(p.eventVar[n])
                    p.eventVar[n] = 0
                    p.totem = [0,0]
                    hasSigil = False
                    hasHead = False
                    for n in p.totparts:
                        if n in sigilList:
                            hasSigil = True
                        if n in ['Canine', 'Insect', 'Avian', 'Hooved', 'Reptile']:
                            hasHead = True
                    if not (hasSigil and hasHead):
                        return True

def mycoMoment(p, hovered, counter):
    if p.eventVar[0] == (0,0):
        for n in range(6):
            if n >= len(p.eventVar[1]):
                break
            nPos = (150+57*(n%3),62+66*int(n/3))
            if p.eventVar[1][n][1].show_image(dimension, nPos, 0, WIN, counter, 44, 1):
                hovered = p.eventVar[1][n][1]
            nPos = (158+57*(n%3),54+66*int(n/3))
            if p.eventVar[1][n][0].show_image(dimension, nPos, 0, WIN, counter, 10, 1):
                hovered = p.eventVar[1][n][0]
    elif isinstance(p.eventVar[0], tuple):
        if p.eventVar[0][0].show_image(dimension, (194,105), 0, WIN, counter, 44, 1):
            hovered = p.eventVar[0][0]
        if p.eventVar[0][1].show_image(dimension, (238,105), 0, WIN, counter, 44, 1):
            hovered = p.eventVar[0][1]
        WIN.blit(pyload("Scryption_Display/Buttons/Myco.png"),(0,0))
        if hovCheck("ellipse", [(240,245),(64,24)]):
            WIN.blit(pyload("Scryption_Display/Buttons/MycoPress.png"),(0,0))
    else:
        if p.eventVar[0].show_image(dimension, (216,105), 0, WIN, counter, 44, 1):
            hovered = p.eventVar[0]
    return hovered

def mycoClick(p):
    if p.eventVar[0] == (0,0):
        for n in range(6):
            if n >= len(p.eventVar[1]):
                break
            nPos = (150+57*(n%3),54+66*int(n/3))
            if hovCheck("rect", [nPos, (48,62)]):
                p.eventVar[0] = p.eventVar[1][n]
    elif isinstance(p.eventVar[0], tuple):
        if hovCheck("rect", [(194,105),(88,58)]):
            p.eventVar[0] = (0,0)
        elif hovCheck("ellipse", [(240,245),(64,24)]):
            newcard = Card("test", 0, 0, "0N", "N/A", [], "N/A")
            newcard.setEqual(p.eventVar[0][0])
            newcard.power += p.eventVar[0][1].power
            newcard.health += p.eventVar[0][1].health
            for n in p.eventVar[0][1].sigils:
                if n not in newcard.sigils and n not in newcard.sigils2:
                    newcard.sigils.append(n)
            for n in p.eventVar[0][1].sigils2:
                if n not in newcard.sigils and n not in newcard.sigils2:
                    newcard.sigils2.append(n)
            newcard.mycNum = max(newcard.mycNum, p.eventVar[0][1].mycNum)+1
            p.cards.pop(p.eventVar[0][0].deckspot)
            p.cards.pop(p.eventVar[0][1].deckspot)
            p.eventVar[0] = newcard
    else:
        if hovCheck("rect", [(216,105),(44,58)]):
            p.cards.append(p.eventVar[0])
            return True
    return False

def goobMoment(p, hovered, counter):
    for n in range(2):
        if p.eventVar[n] not in [0,1]:
            if p.eventVar[n].show_image(dimension, (173+80*n,94), 0, WIN, counter, 44, 1):
                hovered = p.eventVar[n]
    p.hand = [n for n in p.cards if n.trait != "glitch"]
    if p.eventVar[1] == 1:
        for n in range(len(p.hand)):
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            nPos = (240+cardSep*(n-len(p.hand)/2), 215)
            if n == len(p.hand)-1:
                cardSep = 44
            if p.hand[n].show_image(dimension, nPos, 0, WIN, counter, cardSep, 1):
                hovered = p.hand[n]
    if p.eventVar[0] == 0 and p.eventVar[1] not in [0,1]:
        WIN.blit(pyload("Scryption_Display/Buttons/Goob.png"),(0,0))
        if hovCheck("ellipse", [(240,245),(64,24)]):
            WIN.blit(pyload("Scryption_Display/Buttons/GoobPress.png"),(0,0))
    return hovered

def goobClick(p):
    if p.eventVar[1] == 1:
        for n in range(len(p.hand)):
            if len(p.hand) < 9:
                cardSep = 44
            else:
                cardSep = 332/(len(p.hand)-1)+2
            nPos = (240+cardSep*(n-len(p.hand)/2), 215)
            if n == len(p.hand)-1:
                cardSep = 44
            if hovCheck("rect", [nPos, (cardSep,58)]):
                p.eventVar[1] = p.hand[n]
    elif hovCheck("rect", [(253,94),(44,58)]) and p.eventVar[0] == 0:
        p.eventVar[1] = 1
    elif p.eventVar[1] != 0:
        if hovCheck("ellipse", [(240,245),(64,24)]):
            newcard = Card("test", 0, 0, "0N", "N/A", [], "N/A")
            newcard.setEqual(p.eventVar[1])
            if random.randint(0,3) == 0:
                if random.randint(0,1) == 0:
                    newcard.power += 1
                elif newcard.power > 0:
                    newcard.power -= 1
            elif random.randint(0,2) == 0:
                if random.randint(0,1) == 0:
                    newcard.health += 1
                elif newcard.health > 1:
                    newcard.health -= 1
            elif random.randint(0,1) == 0:
                randsigil = random.choice(newcard.sigils+newcard.sigils2)
                newsigil = random.choice(sigilList2)
                while newsigil in newcard.sigils+newcard.sigils2:
                    newsigil = random.choice(sigilList2)
                if randsigil in newcard.sigils:
                    newcard.sigils[newcard.sigils.index(randsigil)] = newsigil
                else:
                    newcard.sigils2[newcard.sigils2.index(randsigil)] = newsigil
            p.eventVar[0] = newcard
    elif hovCheck("rect", [(173,94),(44,58)]):
        p.cards.append(p.eventVar[0])
        return True
    return False

def trialMoment(p, hovered, counter):
    if p.eventVar[0][0] == p.eventVar[0][1]:
        if p.eventVar[1] == 1:
            WIN.blit(pyload("Scryption_Display/Events/trialred.png"), (0,0))
        elif p.eventVar[1] == 2:
            WIN.blit(pyload("Scryption_Display/Events/trialgreen.png"), (0,0))
    if p.eventVar[1] == 3:
        WIN.blit(pyload("Scryption_Display/Events/trialgreen.png"), (0,0))
    for n in range(3):
        if p.eventVar[1] in [1,2]:
            if p.eventVar[0][0][n].show_image(dimension, (160+n*56,137), 0, WIN, counter, 44, 1):
                hovered = p.eventVar[0][0][n]
        else:
            if p.eventVar[0][n].show_image(dimension, (160+n*56,137), 0, WIN, counter, 44, 1):
                hovered = p.eventVar[0][n]
    return hovered

def trialClick(p):
    if p.eventVar[1] == 0:
        # Trials
        for n in range(3):
            if hovCheck("rect", [(160+n*56,137),(44,58)]):
                p.eventVar[0] = [[],[],p.eventVar[0][n].name]
                p.eventVar[1] += 1
                for m in range(3):
                    p.eventVar[0][0].append(create_card(""))
                    cardChose = random.choice(p.cards)
                    while cardChose in p.eventVar[0][1] or cardChose.name == "":
                        cardChose = random.choice(p.cards)
                    p.eventVar[0][1].append(cardChose)
                trialPass = 0
                for m in range(3):
                    if p.eventVar[0][2] == "Trial of Bones" and p.eventVar[0][1][m].cost[-1] == "N":
                        trialPass += int(p.eventVar[0][1][m].cost[:-1])/5
                    elif p.eventVar[0][2] == "Trial of Blood" and p.eventVar[0][1][m].cost[-1] == "B":
                        trialPass += int(p.eventVar[0][1][m].cost[:-1])/4
                    elif p.eventVar[0][2] == "Trial of Power" and isinstance(p.eventVar[0][1][m].power, int):
                        trialPass += p.eventVar[0][1][m].power/4
                    elif p.eventVar[0][2] == "Trial of Health" and isinstance(p.eventVar[0][1][m].health, int):
                        trialPass += p.eventVar[0][1][m].health/6
                    elif p.eventVar[0][2] == "Trial of Wisdom":
                        trialPass += len(p.eventVar[0][1][m].sigils+p.eventVar[0][1][m].sigils2)/3
                    elif ((p.eventVar[0][1][m].tribe == p.eventVar[0][1][(m+1)%3].tribe and p.eventVar[0][1][m].tribe != "") or
                          (p.eventVar[0][1][m].name == p.eventVar[0][1][(m+1)%3].name)):
                        trialPass += 1
                if trialPass >= 1:
                    p.eventVar[1] += 1
    elif p.eventVar[1] < 3:
        # Cards chosen for trial
        if p.eventVar[0][0] == p.eventVar[0][1]:
            if p.eventVar[1] == 2:
                p.eventVar[1] += 1
                p.eventVar[0] = get_cardlist("common",3)
                for n in range(3):
                    p.eventVar[0][n].sigils2 = random.sample(sigilList2,1)
            else:
                return True
        else:
            for n in range(3):
                if hovCheck("rect", [(160+n*56,137),(44,58)]):
                    p.eventVar[0][0][n] = p.eventVar[0][1][n]
    else:
        # Cards earned for winning trial
        for n in range(3):
            if hovCheck("rect", [(160+n*56,137),(44,58)]):
                p.cards.append(p.eventVar[0][n])
                return True