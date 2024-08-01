from Scryption_Item_Sigil import *
import random
import os
import math

def pyload(file):
    file = file.split("/")
    image = pygame.image.load(os.path.join(*file))
    imagesize = image.get_size()
    image = pygame.transform.scale(image, (imagesize[0]*dimension,imagesize[1]*dimension))
    return image

def hovCheck(shape, stats, mousePos):
    mousePos = (mousePos[0]/dimension, mousePos[1]/dimension)
    if shape == "rect":
        # [(x,y),(width,height)]
        if mousePos[0] >= stats[0][0] and mousePos[1] >= stats[0][1] and mousePos[0] <= stats[0][0]+stats[1][0] and mousePos[1] <= stats[0][1]+stats[1][1]:
            return True
    elif shape == "ellipse":
        # [(x,y),(width,height)]
        if (mousePos[0]-stats[0][0])**2/stats[1][0]**2+(mousePos[1]-stats[0][1])**2/stats[1][1]**2 <= 1:
            return True
    return False

def renderFont(text, pos, WIN):
    font = pygame.font.Font("Scrypt_Font.ttf", 10)
    txt1 = font.render(text, 0, (215, 226, 163))
    txt2 = font.render(text, 0, (0, 0, 0))
    txtsiz = txt1.get_size()
    txt1 = pygame.transform.scale(txt1, (txtsiz[0] * dimension, txtsiz[1] * dimension))
    txt2 = pygame.transform.scale(txt2, (txtsiz[0] * dimension, txtsiz[1] * dimension))
    WIN.blit(txt2, ((pos[0]-1) * dimension, (pos[1]-1) * dimension))
    WIN.blit(txt2, ((pos[0]+1) * dimension, (pos[1]-1) * dimension))
    WIN.blit(txt2, ((pos[0]-1) * dimension, (pos[1]+1) * dimension))
    WIN.blit(txt2, ((pos[0]+1) * dimension, (pos[1]+1) * dimension))
    WIN.blit(txt1, (pos[0] * dimension, pos[1] * dimension))

def oneFont(text, pos, WIN):
    font = pygame.font.Font("Scrypt_Font.ttf", 10)
    txt = font.render(text, 0, (0, 0, 0))
    txtsiz = txt.get_size()
    txt = pygame.transform.scale(txt, (txtsiz[0] * dimension, txtsiz[1] * dimension))
    WIN.blit(txt, (pos[0] * dimension, pos[1] * dimension))

# Define card class
class Card:
    def __init__(self, name, power, health, cost, tribe, sigils, trait):
        self.name = name
        self.power = power
        self.health = health
        self.cost = cost
        self.tribe = tribe
        self.sigils = sigils
        self.sigils2 = []
        self.sigilTem = 0
        self.trait = trait
        self.tempPow = power
        # Where the card is in a deck (if it is in a deck)
        self.deckspot = ""
        self.portrait = "_".join(self.name.split())
        self.selected = False
        self.counter = 0
        if self.trait == "glitch":
            self.colorslist = []
            for n in range(40):
                self.colorslist.append([])
                for m in range(54):
                    self.colorslist[n].append(0)
        self.bg = "normal"
        if trait == "terrain" or name in ["Chime", "Wolf Pelt", "Rabbit Pelt"]:
            self.bg = "terrain"
        if name in ["Gold Nugget", "Golden Pelt"]:
            self.bg = "gold"
        self.mycNum = 0
        self.marked = False
        self.sacNeed = 0
        if cost[-1] == "B":
            self.sacNeed = int(cost[:-1])
        self.powChange = 0

    def setEqual(self, card2):
        self.name = card2.name
        self.power = card2.power
        self.health = card2.health
        self.cost = card2.cost
        self.tribe = card2.tribe
        self.sigils = card2.sigils.copy()
        self.sigils2 = card2.sigils2.copy()
        self.sigilTem = card2.sigilTem
        self.trait = card2.trait
        self.tempPow = card2.tempPow
        self.deckspot = card2.deckspot
        self.portrait = card2.portrait
        self.selected = card2.selected
        self.counter = card2.counter
        self.bg = card2.bg
        self.mycNum = card2.mycNum
        self.marked = card2.marked
        self.sacNeed = card2.sacNeed

    def growUp(self):
        newCard = self
        if self.name == "Wolf Cub":
            newCard = self.create_card("Wolf")
        elif self.name == "Elk Fawn":
            newCard = self.create_card("Elk")
        elif self.name == "Raven Egg":
            newCard = self.create_card("Raven")
        elif self.name == "Strange Larva":
            newCard = self.create_card("Strange Pupa")
        elif self.name == "Strange Pupa":
            newCard = self.create_card("Mothman")
        elif self.name == "Dire Wolf Pup":
            newCard = self.create_card("Dire Wolf")
        elif self.name == "Tadpole":
            newCard = self.create_card("Bullfrog")
        elif self.name in ["Worker Ant", "Flying Ant"]:
            newCard = self.create_card("Ant Queen")
        elif self.name == "Elk":
            newCard = self.create_card("Moose Buck")
        elif self.name == "Mole":
            newCard = self.create_card("Mole Man")
        elif self.name == "Mantis":
            newCard = self.create_card("Mantis God")
        else:
            if "Fledgling" in newCard.sigils:
                newCard.sigils.remove("Fledgling")
            elif "Fledgling" in newCard.sigils2:
                newCard.sigils2.remove("Fledgling")
            elif newCard.sigilTem == "Fledgling":
                newCard.sigilTem = ""
            if isinstance(newCard.power, int):
                newCard.power += 1
            newCard.health += 2
            # Any name changes
            z = newCard.name
            if z == "Alpha":
                z = "Omega"
            elif z == "Child 13":
                z = "Child 14"
            elif z == "Dam":
                z = "God Dam"
            elif z == "Long Elk":
                z = "Longer Elk"
            elif z == "Opossum":
                z = "Awesome Opossum"
            elif z == "Mothman":
                z = "Final Form"
            elif z == "Great White":
                z = "Greater White"
            elif z == "Curious Egg":
                z = "Extra Curious Egg"
            else:
                z = "Elder "+z
            newCard.name = z
        newCard.cost = "0N"
        return newCard

    def checkSigil(self, sigil):
        return sigil in self.sigils+self.sigils2 or sigil == self.sigilTem

    def repSigil(self, old, new):
        if not self.checkSigil(old):
            return False
        if old in self.sigils:
            self.sigils[self.sigils.index(old)] = new
        elif old in self.sigils2:
            self.sigils2[self.sigils2.index(old)] = new
        elif old == self.sigilTem:
            self.sigilTem = new
        return True

    def create_card(self, name):
        newCard = create_card(name)
        defself = create_card(self.name)
        if isinstance(self.power, int) or isinstance(newCard.power, int):
            newCard.power = max(0, newCard.power+self.power-defself.power)
        newCard.health = max(1, newCard.health+self.health-defself.health)
        newsigils = []
        for n in self.sigils:
            if n not in defself.sigils:
                newsigils.append(n)
        newCard.sigils += newsigils
        newCard.sigils2 = [n for n in self.sigils2 if n not in newCard.sigils]
        return newCard

    def show_image(self, dimension, pos, rotated, window, counter, cardSep, selectable):
        if rotated:
            card = pygame.Surface((58*dimension,44*dimension)).convert_alpha()
        else:
            card = pygame.Surface((44*dimension,58*dimension)).convert_alpha()
        card.fill((0,0,0,0))
        counter %= 60
        pos = (pos[0]*dimension, pos[1]*dimension)
        if self.selected == True:
            pos = (pos[0]+2*dimension*math.cos(self.counter),pos[1]+4*dimension*math.sin(self.counter))
        if self.trait == "glitch":
            card.blit(pyload("Scryption_Display/Incard_Outline.png"), (0,0))
            for n in range(40):
                for m in range(54):
                    if counter%6 == 0:
                        if random.randint(0,1):
                            self.colorslist[n][m] = (0,0,0)
                        else:
                            self.colorslist[n][m] = (215,226,163)
                    pygame.draw.rect(card, self.colorslist[n][m], ((2+n)*dimension,(2+m)*dimension,dimension,dimension))
        else:
            cardbg = pyload("Scryption_Display/"+self.bg+"_Background.png")
            try:
                cardpt = pyload("Scryption_Display/InPortraits/"+self.portrait+".png")
            except FileNotFoundError:
                cardpt = pyload("Scryption_Display/InPortraits/_.png")
            cardsig = self.sigils+self.sigils2
            cardsg = []
            for n in range(len(self.sigils)):
                cardsg.append(pyload("Scryption_Display/InSigils/"+"_".join(cardsig[n].split())+".png"))
            for n in range(len(self.sigils2)):
                if len(cardsg) == 2:
                    cardsg.append(pyload("Scryption_Display/SigilPlus.png"))
                    break
                cardsg.append(pyload("Scryption_Display/InSigilBlue/"+"_".join(cardsig[n+len(self.sigils)].split())+".png"))
            if self.sigilTem != 0:
                if len(cardsg) == 2:
                    cardsg.append(pyload("Scryption_Display/SigilPlus.png"))
                elif len(cardsg) < 2:
                    cardsg.append(pyload("Scryption_Display/InSigilOrange/"+"_".join(self.sigilTem.split())+".png"))
            cardcs = pyload("Scryption_Display/InCosts/"+self.cost+".png")
            cardol = pyload("Scryption_Display/Incard_Outline.png")
            if self.name in ["Child 13", "Long Elk", "Mantis God", "Geck", "Ouroboros", "Mole Man", "Amalgam", "Pack Rat", "The Daus", "Urayuli", "Amoeba", "Pelt Lice", "Ijiraq", "Great Kraken", "Hodag", "Curious Egg", "Hydra"]:
                cardol = pyload("Scryption_Display/Incard_Rare_Outline.png")
            if isinstance(self.power, int):
                cardpw = []
                pwr = str(max(0, self.power+self.powChange))
                for n in pwr:
                    cardpw.append(pyload("Scryption_Display/InPowers/Pow_"+n+".png"))
            else:
                cardpw = [pyload("Scryption_Display/InPowers/Pow_"+self.power+".png")]
            if isinstance(self.health, int):
                cardht = []
                for n in str(max(0, self.health)):
                    cardht.append(pyload("Scryption_Display/InPowers/Pow_"+n+".png"))
            else:
                cardht = [pyload("Scryption_Display/InPowers/Pow_"+self.health+".png")]
            imgarr = [cardbg, cardol, cardsg, cardpt, cardcs, cardpw, cardht]
            for n in range(7):
                if n == 2:
                    # Sigils
                    for m in range(len(imgarr[n])):
                        if len(imgarr[n]) == 1:
                            sglpos = (14*dimension, 32*dimension)
                            if rotated:
                                sglpos = (32*dimension, 14*dimension)
                        elif m == 0:
                            sglpos = (4*dimension, 32*dimension)
                            if rotated:
                                sglpos = (32*dimension, 23*dimension)
                        elif m == 1:
                            sglpos = (23*dimension, 32*dimension)
                            if rotated:
                                sglpos = (32*dimension, 4*dimension)
                        else:
                            sglpos = (0,0)
                        if rotated:
                            imgarr[n][m] = pygame.transform.rotate(imgarr[n][m], 90)
                        imgarr[n][m] = [imgarr[n][m], sglpos]
                elif n > 4:
                    # Power/health
                    for m in range(len(imgarr[n])):
                        pwPos = (6*m-(6*len(imgarr[n])-39)*(n-5))*dimension
                        if self.health == "x" and n == 6:
                            pwPos = pwPos-dimension
                        if rotated:
                            imgarr[n][m] = [pygame.transform.rotate(imgarr[n][m],90), (0,-pwPos)]
                        else:
                            imgarr[n][m] = [imgarr[n][m], (pwPos, 0)]
                else:
                    imgarr[n] = [imgarr[n], (0,0)]
                    if rotated:
                        imgarr[n][0] = pygame.transform.rotate(imgarr[n][0],90)
                if n in [2,5,6]:
                    # Sigils, power, or health
                    for m in range(len(imgarr[n])):
                        card.blit(imgarr[n][m][0], imgarr[n][m][1])
                else:
                    card.blit(imgarr[n][0],imgarr[n][1])
        if self.marked:
            card.blit(pyload("Scryption_Display/marker.png"), (0,0))
        window.blit(card, pos)
        if selectable:
            if rotated == 0:
                if hovCheck("rect", [(pos[0]/dimension, pos[1]/dimension), (cardSep,58)], pygame.mouse.get_pos()):
                    window.blit(pyload("Scryption_Display/Selected/Outline"+str(int((counter%60)/12))+".png"), pos)
                    return True
            else:
                if hovCheck("rect", [(pos[0]/dimension, pos[1]/dimension), (59,cardSep)], pygame.mouse.get_pos()):
                    window.blit(pygame.transform.rotate(pyload("Scryption_Display/Selected/Outline"+str(int((counter%60)/12))+".png"), 90), pos)
                    return True
        return False

def create_card(choice):
    # Card definitions (format: name, power, health, cost, tribe, sigil(s), bonus sigils, trait)
    stats = {
        "Adder": [1, 1, "2B", "Reptile", ["Touch of Death"], "kills survivors"],
        "Alpha": [1, 2, "4N", "Canine", ["Leader"], "N/A"],
        "Amalgam": [3, 3, "2B", "YES", [], "ant"],
        "Amoeba": [1, 2, "2N", "", ["Amorphous"], "N/A"],
        "Worker Ant": ["antpow", 2, "1B", "Insect", [], "ant"],
        "Ant Queen": ["antpow", 3, "2B", "Insect", ["Ant Spawner"], "ant"],
        "Bat": [2, 1, "4N", "", ["Airborne"], "N/A"],
        "Beaver": [1, 4, "2B", "", ["Dam Builder"], "N/A"],
        "Bee": [1, 1, "0N", "Insect", ["Airborne"], "N/A"],
        "Beehive": [0, 2, "1B", "Insect", ["Bees Within"], "N/A"],
        "Bloodhound": [2, 3, "2B", "Canine", ["Guardian"], "N/A"],
        "Bullfrog": [1, 2, "1B", "Reptile", ["Mighty Leap"], "N/A"],
        "Caged Wolf": [0, 6, "2B", "Canine", [], "terrain"],
        "Cat": [0, 1, "1B", "", ["Many Lives"], "cat0"],
        "Undead Cat": [3, 6, "1B", "", [], "N/A"],
        "Cockroach": [1, 1, "4N", "Insect", ["Unkillable"], "N/A"],
        "Coyote": [2, 1, "4N", "Canine", [], "N/A"],
        "The Daus": [2, 2, "2B", "", ["Bellist"], "chimer"],
        "Tail": [0, 2, "0N", "", [], "N/A"],
        "Elk": [2, 4, "2B", "Hooved", ["Sprinter"], "N/A"],
        "Elk Fawn": [1, 1, "1B", "Hooved", ["Sprinter", "Fledgling"], "N/A"],
        "Field Mice": [2, 2, "2B", "", ["Fecundity"], "N/A"],
        "Geck": [1, 1, "0N", "Reptile", [], "N/A"],
        "Black Goat": [0, 1, "1B", "Hooved", ["Worthy Sacrifice"], "goat"],
        "Grizzly": [4, 6, "3B", "", [], "N/A"],
        "Child 13": [0, 1, "1B", "Hooved", ["Many Lives"], "child0"],
        "Kingfisher": [1, 1, "1B", "Avian", ["Airborne", "Waterborne"], "N/A"],
        "Corpse Maggots": [1, 2, "5N", "Insect", ["Corpse Eater"], "N/A"],
        "Magpie": [1, 1, "2B", "Avian", ["Airborne", "Hoarder"], "N/A"],
        "Mantis": [1, 1, "1B", "Insect", ["Bifurcated Strike"], "N/A"],
        "Mantis God": [1, 1, "1B", "Insect", ["Trifurcated Strike"], "N/A"],
        "Mole": [0, 4, "1B", "", ["Burrower"], "N/A"],
        "Mole Man": [0, 6, "1B", "", ["Burrower", "Mighty Leap"], "N/A"],
        "Moose Buck": [3, 7, "3B", "Hooved", ["Hefty"], "N/A"],
        "Strange Larva": [0, 3, "1B", "Insect", ["Fledgling"], "N/A"],
        "Strange Pupa": [0, 3, "1B", "Insect", ["Fledgling"], "N/A"],
        "Mothman": [7, 3, "1B", "Insect", ["Airborne"], "N/A"],
        "Pack Mule": [0, 5, "0N", "Hooved", ["Sprinter"], "pack mule"],
        "Opossum": [1, 1, "2N", "", [], "N/A"],
        "River Otter": [1, 1, "1B", "", ["Waterborne"], "N/A"],
        "Ouroboros": [1, 1, "2B", "Reptile", ["Unkillable"], "ouroboros"],
        "Pack Rat": [2, 2, "2B", "", ["Trinket Bearer"], "N/A"],
        "Porcupine": [1, 2, "1B", "", ["Sharp Quills"], "N/A"],
        "Pronghorn": [1, 3, "2B", "Hooved", ["Sprinter", "Bifurcated Strike"], "N/A"],
        "Rabbit": [0, 1, "0N", "", [], "N/A"],
        "Rat King": [2, 1, "2B", "", ["Bone King"], "N/A"],
        "Rattler": [3, 1, "6N", "Reptile", [], "N/A"],
        "Raven": [2, 3, "2B", "Avian", ["Airborne"], "N/A"],
        "Raven Egg": [0, 2, "1B", "Avian", ["Fledgling"], "N/A"],
        "Great White": [4, 2, "3B", "", ["Waterborne"], "N/A"],
        "Skink": [1, 2, "1B", "Reptile", ["Loose Tail"], "N/A"],
        "Skunk": [0, 3, "1B", "", ["Stinky"], "N/A"],
        "River Snapper": [1, 6, "2B", "Reptile", [], "N/A"],
        "Long Elk": [1, 2, "4N", "Hooved", ["Sprinter", "Touch of Death"], "long elk"],
        "Sparrow": [1, 2, "1B", "Avian", ["Airborne"], "N/A"],
        "Bell Tentacle": ["bellpow", 3, "2B", "", [], "chime"],
        "Hand Tentacle": ["cardpow", 1, "1B", "", [], "N/A"],
        "Mirror Tentacle": ["mirrpow", 1, "1B", "", [], "N/A"],
        "Squirrel": [0, 1, "0N", "Squirrel", [], "N/A"],
        "Stoat": [1, 2, "1B", "", [], "N/A"],
        "Urayuli": [7, 7, "4B", "", [], "N/A"],
        "Turkey Vulture": [3, 3, "8N", "Avian", ["Airborne"], "N/A"],
        "Warren": [0, 2, "1B", "", ["Rabbit Hole"], "N/A"],
        "Wolf": [3, 2, "2B", "Canine", [], "wolf"],
        "Wolf Cub": [1, 1, "1B", "Canine", ["Fledgling"], "wolf"],
        "Ring Worm": [0, 1, "1B", "Insect", [], "kills survivors"],
        "Wild Bull": [3, 2, "2B", "Hooved", ["Rampager"], "N/A"],
        "Cuckoo": [1, 1, "1B", "Avian", ["Airborne", "Brood Parasite"], "N/A"],
        "Ijiraq": [4, 1, "0N", "", ["Repulsive"], "ijiraq"],
        "Flying Ant": ["antpow", 1, "1B", "Insect", ["Airborne"], "ant"],
        "Mud Turtle": [2, 2, "2B", "Reptile", ["Armored"], "N/A"],
        "Dire Wolf Pup": [1, 1, "2B", "Canine", ["Bone Digger", "Fledgling"], "N/A"],
        "Dire Wolf": [2, 5, "3B", "Canine", ["Double Strike"], "N/A"],
        "Mealworm": [0, 2, "2N", "Insect", ["Morsel"], "N/A"],
        "Wolverine": [1, 3, "5N", "", ["Blood Lust"], "N/A"],
        "Racoon": [1, 1, "1B", "", ["Scavenger"], "N/A"],
        "Lammergeier": ["bonpow", 4, "3B", "Avian", ["Airborne"], "N/A"],
        "Red Hart": ["blodpow", 2, "2B", "Hooved", ["Sprinter"], "N/A"],
        "Tadpole": [0, 1, "0N", "Reptile", ["Waterborne", "Fledgling"], "N/A"],
        "Pelt Lice": [1, 1, "4B", "Insect", ["Double Strike"], "pelt lice"],
        "Hodag": [1, 5, "2B", "", ["Blood Lust"], "hodag"],
        "Great Kraken": [1, 1, "1B", "", ["Waterborne"], "N/A"],
        "Curious Egg": [0, 1, "1N", "", ["Finical Hatchling"], "N/A"],
        "Hydra": [1, 5, "1N", "YES", ["Bifurcated Strike", "Trifurcated Strike"], "N/A"],

        "Rabbit Pelt": [0, 1, "0N", "", [], "pelt"],
        "Wolf Pelt": [0, 2, "0N", "", [], "pelt"],
        "Golden Pelt": [0, 3, "0N", "", [], "pelt"],

        "Boulder": [0, 5, "0N", "", [], "terrain"],
        "Dam": [0, 2, "0N", "", [], "terrain"],
        "Grand Fir": [0, 3, "0N", "", ["Mighty Leap"], "terrain"],
        "Snowy Fir": [0, 4, "0N", "", ["Mighty Leap"], "terrain"],
        "Stump": [0, 3, "0N", "", [], "terrain"],
        "Chime": [0, 1, "0N", "", [], "chime"],
        "Broken Egg": [0, 1, "0N", "", [], "terrain"],
        "Frozen Opossum": [0, 5, "0N", "", ["Frozen Away"], "terrain"],
        "Hungry Child": [0, 0, "0N", "", [], "N/A"],
        "Vertebrae": [0, 1, "0N", "Hooved", [], "N/A"],
        "": [0, 0, "0N", "", [], "glitch"],
        "Strange Frog": [1, 2, "1B", "Reptile", ["Mighty Leap"], "terrain"],
        "Leaping Trap": [0, 1, "0N", "", ["Mighty Leap", "Steel Trap"], "terrain"],
        "Bait Bucket": [0, 1, "0N", "", [], "terrain"],
        "Gold Nugget": [0, 2, "0N", "", [], "terrain"],
        "Starvation": [0, 0, "0N", "", ["Repulsive"], 0],

        "Tamara": [2, 3, "2B", "", ["Airborne", "Loose Tail"], "N/A"],
        "Kaycee": [1, 2, "1B", "", ["Bifurcated Strike", "Sharp Quills"], "N/A"],
        "David": [2, 4, "2B", "", ["Hefty", "Sharp Quills"], "N/A"],
        "Reginald": [1, 3, "3N", "", ["Touch of Death"], "N/A"],
        "Louis": [1, 1, "1B", "", ["Sprinter", "Waterborne"], "N/A"],
        "Cody": [3, 1, "2B", "", ["Burrower", "Loose Tail"], "N/A"],
        "Berke": [2, 1, "2B", "", ["Frozen Away", "Guardian"], "N/A"],
        "Sean": [1, 6, "2B", "", ["Mighty Leap", "Touch of Death"], "N/A"],
        "Oct 19": [3, 2, "1B", "", ["Touch of Death"], "N/A"],
        "Kaminski": [0, 1, "1N", "", ["Guardian", "Sharp Quills"], "N/A"],
        "Luke Carder": [4, 4, "0N", "", [], "N/A"],
        "Jonah": [2, 5, "3B", "", ["Bees Within", "Sharp Quills"], "N/A"],
        "Daniel": [2, 2, "2B", "", ["Double Strike"], "N/A"],

        "Trial": ["", "", "0N", "", [], "N/A"]
    }
    if choice in stats:
        return Card(choice, *stats[choice])
    print("Uhh... yeah "+choice+" is not a card you can define.")
    z = "erm awkward"
    # Force quit
    print(z+1)

def get_cardlist(group, num):
    if group == "all":
        group = ["Adder", "Alpha", "Amalgam", "Amoeba", "Worker Ant", "Ant Queen", 'Bat', 'Beaver', 'Bee',
                 'Beehive', 'Bloodhound', 'Bullfrog', 'Caged Wolf', 'Cat', 'Undead Cat', 'Cockroach', 'Coyote',
                 'The Daus', 'Tail', 'Elk', 'Elk Fawn', 'Field Mice', 'Geck', 'Black Goat', 'Grizzly', 'Child 13',
                 'Kingfisher', 'Corpse Maggots', 'Magpie', 'Mantis', 'Mantis God', 'Mole', 'Mole Man',
                 'Moose Buck', 'Strange Larva', 'Strange Pupa', 'Mothman', 'Pack Mule', 'Opossum', 'River Otter',
                 'Ouroboros', 'Pack Rat', 'Porcupine', 'Pronghorn', 'Rabbit', 'Rat King', 'Rattler', 'Raven',
                 'Raven Egg', 'Great White', 'Skink', 'Skunk', 'River Snapper', 'Long Elk', 'Sparrow',
                 'Bell Tentacle', 'Hand Tentacle', 'Mirror Tentacle', 'Squirrel', 'Stoat', 'Urayuli',
                 'Turkey Vulture', 'Warren', 'Wolf', 'Wolf Cub', 'Ring Worm', 'Wild Bull', 'Cuckoo', 'Ijiraq',
                 'Flying Ant', 'Mud Turtle', 'Dire Wolf Pup', 'Dire Wolf', 'Mealworm', 'Wolverine', 'Racoon',
                 'Lammergeier', 'Red Hart', 'Tadpole', 'Pelt Lice', 'Hodag', 'Great Kraken', 'Curious Egg',
                 'Hydra', 'Rabbit Pelt', 'Wolf Pelt', 'Golden Pelt', 'Boulder', 'Dam', 'Grand Fir', 'Snowy Fir',
                 'Stump', 'Chime', 'Broken Egg', 'Frozen Opossum', 'Hungry Child', 'Vertebrae', '',
                 'Strange Frog', 'Leaping Trap', 'Bait Bucket', 'Gold Nugget', 'Tamara', 'Kaycee', 'David',
                 'Reginald', 'Louis', 'Cody', 'Berke', 'Sean', 'Oct 19', 'Kaminski', 'Luke Carder', 'Jonah', 'Daniel']
    elif group == "rare":
        group = ["Amalgam", "Amoeba", "Child 13", "Geck", "Hodag", "Ijiraq", "Long Elk", "Mantis God", "Mole Man",
                 "Strange Larva", "Ouroboros", "Pack Rat", "Pelt Lice", "The Daus", "Urayuli"]
    elif group == "deathcards":
        group = ["Tamara", "Kaycee", "David", "Reginald", "Louis", "Cody", "Berke", "Sean", "Oct 19", "Kaminski",
                 "Luke Carder", "Jonah", "Daniel"]
    elif group == "common":
        group = ["Adder", "Alpha", "Worker Ant", "Ant Queen", "Bat", "Beaver", "Beehive", "Bloodhound",
                 "Bullfrog", "Cat", "Cockroach", "Coyote", "Elk", "Elk Fawn", "Field Mice", "Black Goat",
                 "Grizzly", "Kingfisher", "Corpse Maggots", "Magpie", "Mantis", "Mole", "Moose Buck", "Opossum",
                 "River Otter", "Porcupine", "Pronghorn", "Rat King", "Rattler", "Raven", "Raven Egg",
                 "Great White", "Skink", "Skunk", "River Snapper", "Sparrow", "Bell Tentacle", "Hand Tentacle",
                 "Mirror Tentacle", "Turkey Vulture", "Warren", "Wolf", "Wolf Cub", "Ring Worm",
                 "Wild Bull", "Cuckoo", "Flying Ant", "Mud Turtle", "Dire Wolf Pup", "Dire Wolf", "Mealworm",
                 "Wolverine", "Racoon", "Lammergeier", "Red Hart", "Tadpole", ""]
    elif group == "cost1":
        group = ["Worker Ant", "Beehive","Bullfrog", "Cat", "Elk Fawn", "Black Goat", "Kingfisher", "Mantis",
                 "Mole", "River Otter", "Porcupine", "Raven Egg", "Skink", "Skunk", "Sparrow", "Hand Tentacle",
                 "Mirror Tentacle", "Warren","Wolf Cub", "Ring Worm", "Cuckoo", "Flying Ant", "Racoon"]
    elif group == "cost2":
        group = ["Adder", "Ant Queen", "Beaver", "Bloodhound", "Elk", "Field Mice", "Magpie", "Pronghorn",
                 "Rat King", "Raven", "River Snapper", "Bell Tentacle", "Wolf", "Wild Bull", "Mud Turtle",
                 "Dire Wolf Pup", "Red Hart"]
    elif group == "cost3":
        group = ["Grizzly", "Moose Buck", "Great White", "Dire Wolf", "Lammergeier"]
    elif group == "costb":
        group = ["Alpha", "Bat", "Cockroach", "Coyote", "Corpse Maggots", "Opossum", "Rattler", "Turkey Vulture",
                 "Mealworm", "Wolverine"]
    elif group == "reptiles":
        group = ["Adder", "Bullfrog", "Rattler", "Skink", "River Snapper", "Mud Turtle", "Tadpole"]
    elif group == "insects":
        group = ["Worker Ant", "Ant Queen", "Bee", "Beehive", "Cockroach", "Corpse Maggots", "Mantis",
                 "Ring Worm", "Flying Ant", "Mealworm"]
    elif group == "avians":
        group = ["Kingfisher", "Magpie", "Raven", "Raven Egg", "Sparrow", "Turkey Vulture", "Cuckoo",
                 "Lammergeier"]
    elif group == "canines":
        group = ["Alpha", "Bloodhound", "Coyote", "Wolf", "Wolf Cub", "Dire Wolf Pup", "Dire Wolf"]
    elif group == "hooved":
        group = ["Elk", "Elk Fawn", "Black Goat", "Moose Buck", "Pronghorn", "Wild Bull", "Red Hart"]
    else:
        print("Uhh... yeah that's not a list you can get.")
        z = "erm awkward"
        # Force quit
        print(z+1)
    group = random.sample(group, num)
    for n in range(num):
        group[n] = create_card(group[n])
    return group

if __name__ == "__main__":
    dimension = 2
    WIN = pygame.display.set_mode((704*dimension, 464*dimension))
    pygame.display.set_caption("Inscryption Card Test")
    clock = pygame.time.Clock()

    test_list = get_cardlist("all",114)
    while True:
        clock.tick(60)
        WIN.fill((100,100,100))
        for n in range(114):
            nPos = ((44*n)%704, 58*(n//16))
            test_list[n].show_image(dimension, nPos, 0, WIN, 0, 44, 0)
        WIN.blit(pyload("Scryption_Display/Overlay.png"),(0,0))
        WIN.blit(pyload("Scryption_Display/Overlay.png"),(480*dimension,0))
        WIN.blit(pyload("Scryption_Display/Overlay.png"),(0,300*dimension))
        WIN.blit(pyload("Scryption_Display/Overlay.png"),(480*dimension,300*dimension))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

#battleScreen
#stonesScreen
#fireScreen
#tradeScreen
#trapScreen
#choiceCScreen
#choiceDScreen
#choiceTScreen
#prospectScreen
