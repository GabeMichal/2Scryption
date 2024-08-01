import pygame
from Scrypt_card import *
from Scrypt_battle import *


# Define player class
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1
        self.mousePos = (0,0)
        self.damage = 0
        self.bones = 0
        self.hand = []
        self.board = [0,0,0,0]
        self.squirrels = []
        for n in range(10):
            self.squirrels.append(create_card("Squirrel"))
        self.deck = []
        self.cards = []
        self.teeth = 0
        self.boneStart = 0
        self.totparts = []
        self.totem = [0,0]
        self.items = ["Squirrel in a Bottle", "Pliers", "Fish Hook"]
        self.sacNum = 0
        # Tells if the Harpie's Birdleg Fan is active for the turn
        self.harpyActive = False
        self.cursorMode = "normal"
        self.mousePos = (0,0)
        self.playerNum = 0
        self.eventVar = 0
        self.myTurn = False
        self.drawn = False
        self.skipper = False
        self.deckShow = False
        self.screen = ""
        self.photos = []
        self.paint = False
        self.ruleb = ""
        self.screenVer = ""

    def draw(self, win):
        rect = ((self.x-self.width/2)*dimension, (self.y-self.height/2)*dimension, self.width*dimension, self.height*dimension)
        pygame.draw.rect(win, self.color, rect)

    def move(self, keys, map):
        if map.segs[0].getColl(self.x, self.y) and (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]):
            dist = 0
            while True:
                dist += 1
                if not map.segs[0].getColl(self.x+dist, self.y):
                    self.x += dist
                    break
                elif not map.segs[0].getColl(self.x-dist, self.y):
                    self.x -= dist
                    break
                elif not map.segs[0].getColl(self.x, self.y+dist):
                    self.y += dist
                    break
                elif not map.segs[0].getColl(self.x, self.y-dist):
                    self.y -= dist
                    break
        if keys[pygame.K_a]:
            if not map.segs[0].getColl(self.x-self.vel, self.y) or map.segs[0].getColl(self.x, self.y):
                self.x-=self.vel
        if keys[pygame.K_d]:
            if not map.segs[0].getColl(self.x+self.vel, self.y) or map.segs[0].getColl(self.x, self.y):
                self.x+=self.vel
        if keys[pygame.K_w]:
            if not map.segs[0].getColl(self.x, self.y-self.vel) or map.segs[0].getColl(self.x, self.y):
                self.y-=self.vel
        if keys[pygame.K_s]:
            if not map.segs[0].getColl(self.x, self.y+self.vel) or map.segs[0].getColl(self.x, self.y):
                self.y+=self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.mousePos = pygame.mouse.get_pos()


    def draw_card(self, deck, spot):
        if len(deck) == 0:
            return
        else:
            card = deck.pop(spot)
            # Magnificus rewrites
            if "Magnificus" in self.screen:
                card.sigils2 = [random.choice(sigilList2)]
                card.sigils = []
            if card.trait == "glitch":
                card = get_cardlist("common",1)[0]
            if "Finical Hatchling" in card.sigils+card.sigils2:
                fhpows = [0, 0, 0, 0, 0]
                fhhelt = [0, 0, 0, 0, 0]
                fhtrib = [0, 0, 0, 0, 0]
                for n in self.cards:
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
                    self.cards[card.deckspot] = create_card("Hydra")
                    card = create_card("Hydra")
            if card.trait == "ijiraq":
                if len(self.deck) == 0:
                    card = create_card("Squirrel")
                else:
                    while card.trait == "ijiraq":
                        card.setEqual(random.choice(deck))
                card.trait = "ijiraq"
            if len(self.totem) == 2:
                if self.totem[0] == card.tribe:
                    card.sigilTem = self.totem[1]
            while "Amorphous" in card.sigils:
                card.sigils[card.sigils.index("Amorphous")] = random.choice(sigilList2)
            while "Amorphous" in card.sigils2:
                card.sigils2[card.sigils2.index("Amorphous")] = random.choice(sigilList2)
            while card.sigilTem == "Amorphous":
                card.sigilTem = random.choice(sigilList2)
            self.hand.append(card)

    def play_card(self, n, m):
        self.board[m] = self.hand.pop(n)
        if self.board[m].checkSigil("Rabbit Hole"):
            self.deck.append(self.board[m].create_card("Rabbit"))
            self.draw_card(self.deck, -1)
        if self.board[m].checkSigil("Dam Builder"):
            if m != 3 and self.board[m + 1] == 0:
                self.board[m + 1] = self.board[m].create_card("Dam")
            if m != 0 and self.board[m - 1] == 0:
                self.board[m - 1] = self.board[m].create_card("Dam")
        if self.board[m].checkSigil("Bellist"):
            if m != 3 and self.board[m + 1] == 0:
                self.board[m + 1] = self.board[m].create_card("Chime")
            if m != 0 and self.board[m - 1] == 0:
                self.board[m - 1] = self.board[m].create_card("Chime")
        if self.board[m].checkSigil("Fecundity"):
            newCard = self.board[m].create_card(self.board[m].name)
            newCard.setEqual(self.board[m])
            if "Fecundity" in newCard.sigils:
                newCard.sigils.remove("Fecundity")
            elif "Fecundity" in newCard.sigils2:
                newCard.sigils2.remove("Fecundity")
            else:
                newCard.sigilTem = ""
            newCard.selected = False
            newCard.cost = create_card(newCard.name).cost
            self.deck.append(newCard)
            self.draw_card(self.deck, -1)
        if self.board[m].checkSigil("Ant Spawner"):
            newCard = self.board[m].create_card("Worker Ant")
            if "Ant Spawner" in newCard.sigils:
                newCard.sigils.remove("Ant Spawner")
            if "Ant Spawner" in newCard.sigils2:
                newCard.sigils2.remove("Ant Spawner")
            self.deck.append(newCard)
            self.draw_card(self.deck, -1)
        if self.board[m].checkSigil("Trinket Bearer") and 0 in self.items:
            self.items[self.items.index(0)] = random.choice(itemList2)
        if self.board[m].name in ["Rabbit Pelt", "Wolf Pelt", "Golden Pelt"]:
            liceCheck = [k for k in self.deck + self.hand if k.trait == "pelt lice"]
            for k in liceCheck:
                if m != 0 and self.board[m-1] == 0:
                    if k in self.hand:
                        self.play_card(self.hand.index(k), m-1)
                        continue
                    if k in self.deck:
                        self.draw_card(self.deck, self.deck.index(k))
                        self.play_card(-1, m-1)
                        continue
                if m != 3 and self.board[m+1] == 0:
                    self.board[m + 1] = k
                    if k in self.hand:
                        self.play_card(self.hand.index(k), m+1)
                    if k in self.deck:
                        self.draw_card(self.deck, self.deck.index(k))
                        self.play_card(-1, m+1)
                    break
        if self.board[m].trait == "ijiraq":
            self.board[m] = create_card("Ijiraq")
        self.board[m].selected = False

    def show_rules(self, WIN):
        if isinstance(self.ruleb, int):
            WIN.blit(pyload("Scryption_Display/Rulebook.png"), (0,0))
            ruleNum = self.ruleb
            if ruleNum >= len(sigilListDesc):
                ruleNum -= len(sigilListDesc)
                WIN.blit(pyload("Scryption_Display/InItems/"+"_".join(itemList[ruleNum].split())+".png"), (37*dimension, 222*dimension))
                oneFont(itemList[ruleNum], (70, 210), WIN)
                for k in range(len(itemsDesc[ruleNum])):
                    oneFont(itemsDesc[ruleNum][k], (70, 225+10*k), WIN)
                if ruleNum+1 < len(itemList):
                    WIN.blit(pyload("Scryption_Display/InItems/"+"_".join(itemList[ruleNum+1].split())+".png"),(245*dimension,222*dimension))
                    oneFont(itemList[ruleNum+1], (278, 210), WIN)
                    for k in range(len(itemsDesc[ruleNum+1])):
                        oneFont(itemsDesc[ruleNum+1][k], (278, 225+10*k), WIN)
            else:
                WIN.blit(pyload("Scryption_Display/InSigils/"+"_".join(sigilListDesc[ruleNum].split())+".png"), (41*dimension, 238*dimension))
                oneFont(sigilListDesc[ruleNum], (70, 210), WIN)
                for k in range(len(sigilDesc[ruleNum])):
                    oneFont(sigilDesc[ruleNum][k], (70, 225+10*k), WIN)
                if ruleNum+1 < len(sigilListDesc):
                    WIN.blit(pyload("Scryption_Display/InSigils/"+"_".join(sigilListDesc[ruleNum+1].split())+".png"),(249*dimension,238*dimension))
                    oneFont(sigilListDesc[ruleNum+1], (278, 210), WIN)
                    for k in range(len(sigilDesc[ruleNum+1])):
                        oneFont(sigilDesc[ruleNum+1][k], (278, 225+10*k), WIN)
                else:
                    ruleNum -= len(sigilListDesc)
                    WIN.blit(pyload("Scryption_Display/InItems/" + "_".join(itemList[ruleNum + 1].split()) + ".png"),(245 * dimension, 222 * dimension))
                    oneFont(itemList[ruleNum + 1], (278, 220), WIN)
                    for k in range(len(sigilDesc[ruleNum + 1])):
                        oneFont(itemsDesc[ruleNum + 1][k], (278, 235+10*k), WIN)

    """
    def play_card(self, card, anti):
        spot = -1
        # "B" = blood cost, "N" = bone cost
        if card.cost[-1] == "B":
            sacsNeed = int(card.cost[:-1])
            # Blood cost
            possibleSacs = 0
            # Count number of sacrifices available
            for n in self.board:
                if n != 0:
                    if n.trait != "terrain" and n.trait[0:-1] != "pelt" and n.trait != "chime":
                        if "Worthy Sacrifice" in n.sigils+n.sigils2:
                            possibleSacs+=3
                        else:
                            possibleSacs+=1
            if possibleSacs >= sacsNeed:
                while sacsNeed >= 1:
                    print(f"This card costs {card.cost[:-1]} blood. Which card will you sacrifice?")
                    sac = pickcard(self.board)
                    for crd in range(len(self.board)):
                        if self.board[crd] != 0:
                            if crd == sac and self.board[crd].trait != "terrain"  and self.board[crd].trait != "chime" and self.board[crd].trait[0:-1] != "pelt":
                                sacsNeed-=1
                                # Anything that takes place during sacrificing
                                self.sacNum+=1
                                if "Worthy Sacrifice" in self.board[crd].sigils+self.board[crd].sigils2:
                                    sacsNeed-=2
                                if "Morsel" in self.board[crd].sigils+self.board[crd].sigils2:
                                    card.power += self.board[crd].power
                                    card.health += self.board[crd].health
                                # Any traits that happen during sacrificing
                                if self.board[crd].trait[0:-1] == "child" or self.board[crd].trait[0:-2] == "child":
                                    self.board[crd].trait = self.board[crd].trait[0:5]+str(int(self.board[crd].trait[5:])+1)
                                    if int(self.board[crd].trait[5:]) % 2 == 1:
                                        self.board[crd].power += 2
                                        self.board[crd].sigils.append("Airborne")
                                    else:
                                        self.board[crd].power -= 2
                                        self.board[crd].sigils.remove("Airborne")
                                    if self.board[crd].trait == "child13":
                                        self.board[crd] = create_card("Hungry Child")
                                if self.board[crd].trait[0:2] == "cat":
                                    self.board[crd].trait = self.board[crd].trait[0:2]+str(int(self.board[crd].trait[-1])+1)
                                    if self.board[crd].trait == "cat9":
                                        keepcat = self.board[crd]
                                        self.board[crd] = create_card("Undead Cat")
                                        self.board[crd].power += keepcat.power
                                        self.board[crd].health += keepcat.health
                                        self.board[crd].sigils += keepcat.sigils
                                        self.board[crd].sigils2 += keepcat.sigils2
                                if "Many Lives" not in self.board[crd].sigils+self.board[crd].sigils2:
                                    # Card's death
                                    if "Bone King" in self.board[crd].sigils+self.board[crd].sigils2:
                                        self.bones+=3
                                    if "Unkillable" in self.board[crd].sigils+self.board[crd].sigils2:
                                        self.hand.append(self.board[crd])
                                        if self.board[crd].trait == "ouroboros":
                                            self.hand[-1].power+=1
                                            self.hand[-1].health+=1
                                            self.cards[self.hand[-1].deckspot].power+=1
                                            self.cards[self.hand[-1].deckspot].health+=1
                                    self.board[crd] = 0
                                    self.bones+=1
                                    for opp in anti.board:
                                        if opp != 0:
                                            if opp.trait == "Scavenger":
                                                anti.bones+=1
                                                break
                                elif self.board[crd].name == "Undead Cat":
                                    self.board[crd].sigils.remove("Many Lives")
                            elif crd == sac and (self.board[crd].trait == "terrain" or self.board[crd].trait[0:-1] == "pelt" or self.board[crd].trait == "chime"):
                                print("That card cannot be sacrificed!")
                        elif crd == sac:
                            print("No card is there to be sacrificed.")
                self.hand.remove(card)
                printcards(self.board)
                while True:
                    spot = input("Where do you want to play the card? ")
                    if spot == '1' or spot == '2' or spot == '3' or spot == '4':
                        spot = int(spot)-1
                        if self.board[spot] == 0:
                            break
                        else:
                            print("Selected spot is occupied.")
                    else:
                        print("Please select a number between 1 and 4.")
            else:
                print("You do not have enough blood on the board.")
        else:
            # Bone cost
            if card in self.hand and self.bones >= int(card.cost[:-1]):
                self.hand.remove(card)
                if card.trait != "ijiraq":
                    self.bones -= int(card.cost[:-1])
                while True:
                    spot = input("Where do you want to play the card? ")
                    if spot == '1' or spot == '2' or spot == '3' or spot == '4':
                        spot = int(spot)-1
                        if self.board[spot] == 0:
                            break
                        else:
                            print("Selected spot is occupied.")
                    else:
                        print("Please select a number between 1 and 4.")
            else:
                print("You do not have enough bones to play this card.")
        # Playing the card
        if spot > -1:
            self.board[spot] = card
            if "Rabbit Hole" in card.sigils or "Rabbit Hole" in card.sigils2:
                self.hand.append(create_card("Rabbit"))
            if "Dam Builder" in card.sigils or "Dam Builder" in card.sigils2:
                if spot != 3:
                    if self.board[spot+1] == 0:
                        self.board[spot+1] = create_card("Dam")
                if spot != 0:
                    if self.board[spot-1] == 0:
                        self.board[spot-1] = create_card("Dam")
            if "Bellist" in card.sigils or "Bellist" in card.sigils2:
                if spot != 3:
                    if self.board[spot+1] == 0:
                        self.board[spot+1] = create_card("Chime")
                if spot != 0:
                    if self.board[spot-1] == 0:
                        self.board[spot-1] = create_card("Chime")
            if ("Hoarder" in card.sigils or "Hoarder" in card.sigils2) and len(self.deck) > 0:
                deck = self.deck.copy()
                for n in range(len(deck)):
                    if deck[n].trait == "ijiraq":
                        while deck[n].trait == "ijiraq":
                            deck[n] = random.choice(deck)
                        deck[n].trait = "ijiraq"
                print("You may now pick one of your own cards to draw.")
                drawn = pickcards(self.deck)
                self.hand.append(deck[drawn])
                self.deck.remove(deck[drawn])
                # All the junk that happens when you draw the card
                if drawn.name == "":
                    print("01100100 01100101 01100101 01110000 01100010 01100101 01101110 01100101 01100001 01110100 01101000")
                    drawn = get_cardlist(common,1)[0]
                if len(self.totem) == 2:
                    if self.totem[0] == drawn.tribe:
                        drawn.sigils2.append(self.totem[1])
                    print(f"Your {drawn.tribe} gained the {self.totem[1]} sigil.")
                if "Amorphous" in drawn.sigils:
                    drawn.sigils.remove("Amorphous")
                    drawn.sigils.append(random.choice(sigilList2))
                    print(f"This card's sigil is {drawn.sigils[-1]}")
                if "Amorphous" in drawn.sigils2:
                    drawn.sigils2.remove("Amorphous")
                    drawn.sigils2.append(random.choice(sigilList2))
                    print(f"This card's sigil is {drawn.sigils2[-1]}")
                if "Finical Hatchling" in drawn.sigils+drawn.sigils2:
                    fhpows = [0, 0, 0, 0, 0]
                    fhhelt = [0, 0, 0, 0, 0]
                    fhtrib = [0, 0, 0, 0, 0]
                    for n in self.cards:
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
                        print(f"Your {drawn.name} has hatched... what a wonderful form.")
                        drawn = create_card("Hydra")
                        self.cards[drawn.deckspot] = create_card("Hydra")
            if "Fecundity" in card.sigils+card.sigils2:
                self.hand.append(Card(card.name, card.power, card.health, card.cost, card.tribe, card.sigils, card.sigils2, card.trait))
                if "Fecundity" in card.sigils:
                    self.hand[-1].sigils.remove("Fecundity")
                else:
                    self.hand[-1].sigils2.remove("Fecundity")
            if "Ant Spawner" in card.sigils+card.sigils2:
                self.hand.append(create_card("Worker Ant"))
            if "Brood Parasite" in card.sigils+card.sigils2:
                if anti.board[spot] == 0:
                    if random.randint(1, 10) == 10:
                        print("The egg survived the fall... how curious.")
                        anti.board[spot] == create_card("Raven Egg")
                    else:
                        anti.board[spot] == create_card("Broken Egg")
            if "Trinket Bearer" in card.sigils+card.sigils2:
                self.items.append(random.choice(itemList))
            print(f"{self.name} plays {card.name}")
            for n in range(len(anti.board)):
                if anti.board[n] != 0:
                    if "Guardian" in anti.board[n].sigils+anti.board[n].sigils2:
                        if anti.board[spot] == 0:
                            anti.board[spot] = anti.board[n]
                            anti.board[n] = 0
            # This doesn't use traits, simply so ijiraq's disguise will work correctly
            if card.name == "Rabbit Pelt" or card.name == "Wolf Pelt" or card.name == "Golden Pelt":
                for n in range(len(self.hand)):
                    if self.hand[n].name == "Pelt Lice":
                        if spot != 0:
                            if self.board[spot-1] == 0:
                                self.board[spot-1] = self.hand.pop(n)
                        if spot != 3:
                            if self.board[spot+1] == 0:
                                self.board[spot+1] = self.hand.pop(n)
                for n in range(len(self.deck)):
                    if self.deck[n].trait == "pelt lice":
                        if spot != 0:
                            if self.board[spot-1] == 0:
                                self.board[spot-1] = self.deck.pop(n)
                        if spot != 3:
                            if self.board[spot+1] == 0:
                                self.board[spot+1] = self.deck.pop(n)
            if card.trait == "ijiraq":
                self.board[spot] = create_card("Ijiraq")
                print("... But intriguingly, it was a disguise. The true creature revealed itself...")

    def receive_damage(self, damage):
        self.damage += damage

    def end_turn(self, opponent):
        # Ant power tracker
        antscount = 0
        for n in self.board:
            if n != 0:
                if n.trait == "ant":
                    antscount+=1
        for n in range(len(self.board)):
            if self.board[n] != 0:
                if self.board[n].power == "mirrpow":
                    if opponent.board[n] != 0:
                        if opponent.board[n].power == "mirrpow":
                            self.board[n].tempPow = 0
                        else:
                            self.board[n].tempPow = opponent.board[n].tempPow
                    else:
                        self.board[n].tempPow = 0
                elif self.board[n].power == "antpow":
                    self.board[n].tempPow = antscount
                elif self.board[n].power == "bonpow":
                    self.board[n].tempPow = self.bones/2
                elif self.board[n].power == "blodpow":
                    self.board[n].tempPow = self.sacNum
                elif self.board[n].power == "cardpow":
                    self.board[n].tempPow = len(self.hand)
                elif self.board[n].power == "bellpow":
                    self.board[n].tempPow = 4-n
                else:
                    self.board[n].tempPow = self.board[n].power
        for n in range(len(self.board)):
            if self.board[n] != 0:
                # Weird types of attacks
                if "Bifurcated Strike" in self.board[n].sigils+self.board[n].sigils2:
                    if n != 3:
                        attack(self.board[n], opponent, n+1, self, n)
                    if n != 0:
                        attack(self.board[n], opponent, n-1, self, n)
                if "Trifurcated Strike" in self.board[n].sigils+self.board[n].sigils2:
                    if n != 3:
                        attack(self.board[n], opponent, n+1, self, n)
                    if n != 0:
                        attack(self.board[n], opponent, n-1, self, n)
                    attack(self.board[n], opponent, n, self, n)
                if "Double Strike" in self.board[n].sigils+self.board[n].sigils2:
                    attack(self.board[n], opponent, n, self, n)
                    attack(self.board[n], opponent, n, self, n)
                # If it doesn't have any weird attacking things
                z = self.board[n]
                if "Bifurcated Strike" not in z.sigils+z.sigils2 and "Trifurcated Strike" not in z.sigils+z.sigils2 and "Double Strike" not in z.sigils+z.sigils2:
                    attack(self.board[n], opponent, n, self, n)
                if "Bone Digger" in self.board[n].sigils+self.board[n].sigils2:
                    self.bones+=1
                if "Sprinter" in self.board[n].sigils+self.board[n].sigils2 or "Hefty" in self.board[n].sigils+self.board[n].sigils2 or "Rampager" in self.board[n].sigils+self.board[n].sigils2:
                    if n != 3:
                        if self.board[n+1] == 0:
                            # Normal move
                            self.board[n+1] = self.board[n]
                            self.board[n] = 0
                            if self.board[n+1].trait == "long elk":
                                self.board[n] = create_card("Vertebrae")
                        elif n != 0:
                            if self.board[n-1] == 0:
                                if "Sprinter" in self.board[n].sigils+self.board[n].sigils2:
                                    # Turns around if a card is blocking
                                    if "Sprinter" in self.board[n].sigils:
                                        self.board[n].sigils[self.board[n].sigils.index("Sprinter")] = "SprinterL"
                                    else:
                                        self.board[n].sigils2[self.board[n].sigils2.index("Sprinter")] = "SprinterL"
                                    self.board[n-1] = self.board[n]
                                    self.board[n] = 0
                                    if self.board[n-1].trait == "long elk":
                                        self.board[n] = create_card("Vertebrae")
                            if "Hefty" in self.board[n].sigils+self.board[n].sigils2:
                                # Can the hefty sigil move things?
                                hefmov = False
                                for m in range(len(self.board[n:])):
                                    if self.board[n+m] == 0:
                                        hefmov = True
                                if hefmov == True:
                                    # How far can the hefty sigil move?
                                    lasmov = 0
                                    for m in range(len(self.board[n:])):
                                        if self.board[3-m] == 0:
                                            lasmov = 3-m
                                    # Actually move
                                    while lasmov > n:
                                        self.board[lasmov] = self.board[lasmov-1]
                                        lasmov-=1
                                    self.board[n] = 0
                                else:
                                    # Turns around if cards are blocking
                                    if "Hefty" in self.board[n].sigils:
                                        self.board[n].sigils[self.board[n].sigils.index("Hefty")] = "HeftyL"
                                    else:
                                        self.board[n].sigils2[self.board[n].sigils2.index("Hefty")] = "HeftyL"
                                    # How far can the hefty sigil move?
                                    lasmov = 3
                                    movin = False
                                    for m in range(len(self.board[:n])):
                                        if self.board[m] == 0:
                                            lasmov = m
                                    # Actually move
                                    while lasmov < n:
                                        self.board[lasmov] = self.board[lasmov+1]
                                        lasmov+=1
                                        movin = True
                                    if movin:
                                        self.board[n] = 0
                            if "Rampager" in self.board[n].sigils+self.board[n].sigils2:
                                # Launch something over itself
                                page = self.board[n]
                                self.board[n] = self.board[n+1]
                                self.board[n+1] = page
                    else:
                        # It's on the rightmost side
                        if self.board[n-1] == 0 and "Sprinter" in self.board[n].sigils+self.board[n].sigils2:
                            # Turns around
                            if "Sprinter" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("Sprinter")] = "SprinterL"
                            else:
                                self.board[n].sigils2[self.board[n].sigils2.index("Sprinter")] = "SprinterL"
                            self.board[n-1] = self.board[n]
                            self.board[n] = 0
                            if self.board[n-1].trait == "long elk":
                                self.board[n] = create_card("Vertebrae")
                        if "Hefty" in self.board[n].sigils+self.board[n].sigils2:
                            if "Hefty" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("Hefty")] = "HeftyL"
                            else:
                                self.board[n].sigils[self.board[n].sigils.index("Hefty")] = "HeftyL"
                            # How far can hefty move?
                            lasmov = 3
                            movin = False
                            for m in range(len(self.board[:n])):
                                if self.board[m] == 0:
                                    lasmov = m
                            # Actually move
                            while lasmov < n:
                                self.board[lasmov] = self.board[lasmov+1]
                                lasmov+=1
                                movin = True
                            if movin:
                                self.board[n] = 0
                        if "Rampager" in self.board[n].sigils+self.board[n].sigils2:
                            # Turns around
                            if "Rampager" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("Rampager")] = "RampagerL"
                            else:
                                self.board[n].sigils[self.board[n].sigils.index("Rampager")] = "RampagerL"
                            page = self.board[n]
                            self.board[n] = self.board[n-1]
                            self.board[n-1] = page
                if "SprinterL" in self.board[n].sigils+self.board[n].sigils2 or "HeftyL" in self.board[n].sigils+self.board[n].sigils2 or "RampagerL" in self.board[n].sigils+self.board[n].sigils2:
                    if n != 0:
                        if self.board[n-1] == 0:
                            # Normal move
                            self.board[n-1] = self.board[n]
                            self.board[n] = 0
                            if self.board[n-1].trait == "long elk":
                                self.board[n] = create_card("Vertebrae")
                        elif n != 3:
                            if self.board[n+1] == 0:
                                if "SprinterL" in self.board[n].sigils+self.board[n].sigils2:
                                    # Turns around if a card is blocking
                                    if "SprinterL" in self.board[n].sigils:
                                        self.board[n].sigils[self.board[n].sigils.index("SprinterL")] = "Sprinter"
                                    else:
                                        self.board[n].sigils2[self.board[n].sigils2.index("SprinterL")] = "Sprinter"
                                    self.board[n+1] = self.board[n]
                                    self.board[n] = 0
                                    if self.board[n+1].trait == "long elk":
                                        self.board[n] = create_card("Vertebrae")
                            if "HeftyL" in self.board[n].sigils+self.board[n].sigils2:
                                # Can the hefty sigil move things?
                                hefmov = False
                                for m in range(len(self.board[:n])):
                                    if self.board[m] == 0:
                                        hefmov = True
                                if hefmov == True:
                                    # How far can the hefty sigil move?
                                    lasmov = 3
                                    for m in range(len(self.board[:n])):
                                        if self.board[m] == 0:
                                            lasmov = m
                                    # Actually move
                                    while lasmov < n:
                                        self.board[lasmov] = self.board[lasmov+1]
                                        lasmov+=1
                                    self.board[n] = 0
                                else:
                                    # Turns around if a cards are blocking
                                    if "HeftyL" in self.board[n].sigils:
                                        self.board[n].sigils[self.board[n].sigils.index("HeftyL")] = "Hefty"
                                    else:
                                        self.board[n].sigils2[self.board[n].sigils2.index("HeftyL")] = "Hefty"
                                    # How far can the hefty sigil move?
                                    lasmov = 0
                                    movin = False
                                    for m in range(len(self.board[n:])):
                                        if self.board[3-m] == 0:
                                            lasmov = 3-m
                                    # Actually move
                                    while lasmov > n:
                                        self.board[lasmov] = self.board[lasmov-1]
                                        lasmov-=1
                                        movin = True
                                    if movin:
                                        self.board[n] = 0
                            if "RampagerL" in self.board[n].sigils+self.board[n].sigils2:
                                # Launch something over itself
                                page = self.board[n]
                                self.board[n] = self.board[n-1]
                                self.board[n-1] = page
                    else:
                        # It's on the leftmost side
                        if self.board[n+1] == 0 and "SprinterL" in self.board[n].sigils+self.board[n].sigils2:
                            # Turns around
                            if "SprinterL" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("SprinterL")] = "Sprinter"
                            else:
                                self.board[n].sigils2[self.board[n].sigils2.index("SprinterL")] = "Sprinter"
                            self.board[n+1] = self.board[n]
                            self.board[n] = 0
                            if self.board[n+1].trait == "long elk":
                                self.board[n] = create_card("Vertebrae")
                        if "HeftyL" in self.board[n].sigils+self.board[n].sigils2:
                            if "HeftyL" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("HeftyL")] = "Hefty"
                            else:
                                self.board[n].sigils[self.board[n].sigils.index("HeftyL")] = "Hefty"
                            # How far can hefty move?
                            lasmov = 0
                            movin = False
                            for m in range(len(self.board[n:])):
                                if self.board[3-m] == 0:
                                    lasmov = 3-m
                            # Actually move
                            while lasmov > n:
                                self.board[lasmov] = self.board[lasmov-1]
                                lasmov-=1
                                movin = True
                            if movin:
                                self.board[n] = 0
                        if "RampagerL" in self.board[n].sigils+self.board[n].sigils2:
                            # Turns around
                            if "RampagerL" in self.board[n].sigils:
                                self.board[n].sigils[self.board[n].sigils.index("RampagerL")] = "Rampager"
                            else:
                                self.board[n].sigils[self.board[n].sigils.index("RampagerL")] = "Rampager"
                            page = self.board[n]
                            self.board[n] = self.board[n+1]
                            self.board[n+1] = page

    def item_use(self, item, enemy):
        if item == "Boulder in a Bottle":
            self.hand.append(create_card("Boulder"))
            return 1
        elif item == "Squirrel in a Bottle":
            self.hand.append(create_card("Squirrel"))
            return 1
        elif item == "Special Dagger":
            print("... Ow.")
            enemy.damage += 5
            return 1
        elif item == "Pliers":
            print("... Ow.")
            enemy.damage += 1
            return 1
        elif item == "Hoggy Bank":
            self.bones += 4
            return 1
        elif item == "Hourglass":
            if self == player1:
                p2skip = True
            else:
                p1skip = True
            return 1
        elif item == "Black Goat in a Bottle":
            self.hand.append(create_card("Black Goat"))
            return 1
        elif item == "Frozen Opossum in a Bottle":
            self.hand.append(create_card("Frozen Opossum"))
            return 1
        elif item == "Fish Hook":
            fhcnt = 0
            for n in range(4):
                if self.board[n] == 0 and enemy.board[n] != 0 and enemy.board[n].trait != "uncuttable" and enemy.board[n].triat != "pack mule":
                    fhcnt+=1
            if fhcnt >= 0:
                while True:
                    printcards(enemy.board)
                    printcards(self.board)
                    print("Which card would you like to take?")
                    chose = pickcard(enemy.board)
                    if enemy.board[chose].trait == "uncuttable" or enemy.board[chose].trait == "pack mule":
                        print("That card is too large to steal.")
                    elif self.board[chose] == 0 and enemy.board[chose] != 0:
                        self.board[chose] = enemy.board[chose]
                        enemy.board[chose] = 0
                        return 1
                    else:
                        print("You have a card in front of that.")
            else:
                print("You can't steal yet.")
                return 0
        elif item == "Harpie's Birdleg Fan":
            self.harpyActive = True
        elif item == "Wiseclock":
            for n in range(4):
                if n == 0:
                    p1_3 = player1.board[3]
                elif n == 3:
                    player1.board[0] = player2.board[0]
                else:
                    player1.board[3-n] = player1.board[2-n]
            for n in range(4):
                if n == 3:
                    player2.board[3] = p1_3
                else:
                    player2.board[n] = player2.board[n+1]
            return 1
        elif item == "Magickal Bleach":
            for n in range(4):
                enemy.board[n].sigils = []
                enemy.board[n].sigils2 = []
            return 1
        elif item == "Magpie's Lens":
            deck = self.deck.copy()
            for n in range(len(deck)):
                if deck[n].trait == "ijiraq":
                    while deck[n].trait == "ijiraq":
                        deck[n] = random.choice(deck)
                    deck[n].trait = "ijiraq"
            print("You may now pick one of your own cards to draw.")
            drawn = pickcards(self.deck)
            self.hand.append(deck[drawn])
            self.deck.remove(deck[drawn])
            # All the junk that happens when you draw the card
            if drawn.name == "":
                print("01100100 01100101 01100101 01110000 01100010 01100101 01101110 01100101 01100001 01110100 01101000")
                drawn = get_cardlist(common,1)[0]
            if len(self.totem) == 2:
                if self.totem[0] == drawn.tribe:
                    drawn.sigils2.append(self.totem[1])
                print(f"Your {drawn.tribe} gained the {self.totem[1]} sigil.")
            if "Amorphous" in drawn.sigils:
                drawn.sigils.remove("Amorphous")
                drawn.sigils.append(random.choice(sigilList2))
                print(f"This card's sigil is {drawn.sigils[-1]}")
            if "Amorphous" in drawn.sigils2:
                drawn.sigils2.remove("Amorphous")
                drawn.sigils2.append(random.choice(sigilList2))
                print(f"This card's sigil is {drawn.sigils2[-1]}")
            if "Finical Hatchling" in drawn.sigils+drawn.sigils2:
                fhpows = [0, 0, 0, 0, 0]
                fhhelt = [0, 0, 0, 0, 0]
                fhtrib = [0, 0, 0, 0, 0]
                for n in self.cards:
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
                    print(f"Your {drawn.name} has hatched... what a wonderful form.")
                    drawn = create_card("Hydra")
                    self.cards[drawn.deckspot] = create_card("Hydra")
            return 1
        elif item == "Skinning Knife" or item == "Scissors":
            canuse = False
            for n in enemy.board:
                if n != 0 and n.trait != "uncuttable" and n.trait != "pack mule":
                    canuse = True
            printcards(enemy.board)
            if canuse:
                while True:
                    print("Which card would you like to cut?")
                    chose = pickcard(enemy.board)
                    if enemy.board[chose].trait == "uncuttable" or enemy.board[chose].trait == "pack mule":
                        print("That card is too big to cut.")
                    else:
                        # Death of a creature
                        enemy.board[chose] = 0
                        enemy.bones += 1
                        if item == "Skinning Knife":
                            self.hand.append(create_card("Rabbit Pelt"))
                        return 1
            else:
                print("The opponent has no cards you can cut.")
                return 0
        
    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Bones: {self.bones})"
"""
