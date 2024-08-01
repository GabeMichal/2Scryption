from Scryption_Item_Sigil import *
import random
import math

# Empty card (for board purposes)
Empty = " ____________ |            ||            ||            ||            ||            ||            ||            ||            ||            ||            ||____________|"

# Define card class
class Card:
    def __init__(self, name, power, health, cost, tribe, sigils, sigils2, trait):
        self.name = name
        self.power = power
        self.health = health
        self.cost = cost
        self.tribe = tribe
        self.sigils = sigils
        self.sigils2 = sigils2
        self.trait = trait
        self.tempPow = power
        # Where the card is in a deck (if it is in a deck)
        self.deckspot = ""
        
    def __str__(self):
        if self.name == "":
            arr = [" ____________ ",[],[],[],[],[],[],[],[],[],[],[]]
            for n in range(11):
                arr[n+1].append("|")
                for m in range(12):
                    arr[n+1].append(random.choice(["|", "/", "\\"]))
                arr[n+1].append("|")
                arr[n+1] = "".join(arr[n+1])
        else:
            le = len(self.name)
            if le >= 12:
                dex = self.name.index(" ")
                name1 = self.name[0:dex]
                name2 = self.name[dex+1:]
                le = int((12-len(name1))/2)
                name1 = " "*le+name1+" "*le
                le = int((12-len(name2))/2)
                name2 = " "*le+name2+" "*le
            else:
                name1 = "            "
                le = int((12-le)/2)
                name2 = " "*le+self.name+" "*le
            while len(name1) > 12:
                name1 = name1[0:-2]
            while len(name1) < 12:
                name1 = name1+" "
            while len(name2) > 12:
                name2 = name2[0:-2]
            while len(name2) < 12:
                name2 = name2+" "
            if self.cost[-1] == "B":
                cst = self.cost[:-1]+" BLD"
            elif self.cost[0] == "0":
                cst = "     "
            else:
                cst = self.cost[:-1]+" BNE"
            if self.tempPow == "antpow":
                antpow = Sigils[sigilList.index("Ant Spawner")]
                pwr1 = antpow[3:5]
                pwr = antpow[10:12]
                pwr2 = antpow[17:19]
            elif self.tempPow == "blodpow":
                pwr1 = "||"
                pwr = "--"
                pwr2 = "\/"
            elif self.tempPow == "bonpow":
                pwr1 = "1/"
                pwr = "/2"
                pwr2 = "__"
            else:
                pwr1 = "  "
                pwr2 = "__"
                if self.tempPow == "bellpow":
                    pwr = " B"
                elif self.tempPow == "cardpow":
                    pwr = " C"
                elif self.tempPow == "mirrpow":
                    pwr = " M"
                elif self.tempPow > 9:
                    pwr = str(self.tempPow)
                else:
                    pwr = " "+str(self.tempPow)
            if self.health > 9:
                helt = str(self.health)
            else:
                helt = " "+str(self.health)
            prsigl = ["      ", "      ", "______"]
            if len(self.sigils) == 1:
                n1 = Sigils[sigilList.index(self.sigils[0])]
                prsigl = [n1[1:7],n1[8:14],n1[15:21]]
            elif len(self.sigils) > 1:
                n1 = Sigils2[sigilList.index(self.sigils[0])]
                n2 = Sigils2[sigilList.index(self.sigils[1])]
                prsigl = ["   "+n2[1:4],n1[1:4]+n2[5:8],n1[5:8]+"___"]
            elif len(self.sigils2) == 1:
                n1 = Sigils[sigilList.index(self.sigils2[0])]
                prsigl = [n1[1:7],n1[8:14],n1[15:21]]
            minisigl = []
            for n in range(6):
                if len(self.sigils2) > 1 or len(self.sigils) > 0:
                    if len(self.sigils2) > n:
                        minisigl.append(Sigils2[sigilList.index(self.sigils2[n])])
                    else:
                        minisigl.append("          ")
                else:
                    minisigl.append("          ")
            sgl21 = minisigl[0][1:4]
            sgl22 = minisigl[0][5:8]
            sgl23 = minisigl[1][1:4]
            sgl24 = minisigl[1][5:8]
            sgl25 = minisigl[2][1:4]
            sgl26 = minisigl[2][5:8]
            sgl27 = minisigl[3][1:4]
            sgl28 = minisigl[3][5:8]
            sgl29 = minisigl[4][1:4]
            sgl210 = minisigl[4][5:8]
            sgl211 = minisigl[5][1:4]
            sgl212 = minisigl[5][5:8]
            arr = [" ____________ ",
                   "|"+name1+"|",
                   "|"+name2+"|",
                   "|____________|",
                   "|"+sgl21+sgl25+" "+cst+"|",
                   "|"+sgl22+sgl26+"      |",
                   "|"+sgl23+sgl27+sgl29+sgl211+"|",
                   "|"+sgl24+sgl28+sgl210+sgl212+"|",
                   "|____________|",
                   "|"+pwr1+" "+prsigl[0]+"   |",
                   "|"+pwr+"P"+prsigl[1]+helt+"H|",
                   "|"+pwr2+"_"+prsigl[2]+"___|"]
        return "".join(arr)

def create_card(choice):
    # Card definitions (format: name, power, health, cost, tribe, sigil(s), bonus sigils, trait)
    adder = Card("Adder", 1, 1, "2B", "Reptile", ["Touch of Death"], [], "kills survivors")
    alpha = Card("Alpha", 1, 2, "4N", "Canine", ["Leader"], [], "N/A")
    amalg = Card("Amalgam", 3, 3, "2B", "YES", [], [], "ant")
    ameba = Card("Amoeba", 1, 2, "2N", "N/A", ["Amorphous"], [], "N/A")
    antWork = Card("Worker Ant", "antpow", 2, "1B", "Insect", [], [], "ant")
    antQ = Card("Ant Queen", "antpow", 3, "2B", "Insect", ["Ant Spawner"], [], "ant")
    bat = Card("Bat", 2, 1, "4N", "N/A", ["Airborne"], [], "N/A")
    bever = Card("Beaver", 1, 4, "2B", "N/A", ["Dam Builder"], [], "N/A")
    bee = Card("Bee", 1, 1, "0N", "Insect", ["Airborne"], [], "N/A")
    hive = Card("Beehive", 0, 2, "1B", "Insect", ["Bees Within"], [], "N/A")
    hound = Card("Bloodhound", 2, 3, "2B", "Canine", ["Guardian"], [], "N/A")
    frog = Card("Bullfrog", 1, 2, "1B", "Reptile", ["Mighty Leap"], [], "N/A")
    cage = Card("Caged Wolf", 0, 6, "2B", "Canine", [], [], "terrain")
    cat = Card("Cat", 0, 1, "1B", "N/A", ["Many Lives"], [], "cat0")
    uncat = Card("Undead Cat", 3, 6, "1B", "N/A", [], [], "N/A")
    roach = Card("Cockroach", 1, 1, "4N", "Insect", ["Unkillable"], [], "N/A")
    coyote = Card("Coyote", 2, 1, "4N", "Canine", [], [], "N/A")
    daus = Card("The Daus", 2, 2, "2B", "N/A", ["Bellist"], [], "chimer")
    tail = Card("Tail", 0, 2, "0N", "N/A", [], [], "N/A")
    elk = Card("Elk", 2, 4, "2B", "Hooved", ["Sprinter"], [], "N/A")
    elkfawn = Card("Elk Fawn", 1, 1, "1B", "Hooved", ["Sprinter", "Fledgling"], [], "N/A")
    mice = Card("Field Mice", 2, 2, "2B", "N/A", ["Fecundity"], [], "N/A")
    geck = Card("Geck", 1, 1, "0N", "Reptile", [], [], "N/A")
    goat = Card("Black Goat", 0, 1, "1B", "Hooved", ["Worthy Sacrifice"], [], "goat")
    bear = Card("Grizzly", 4, 6, "3B", "N/A", [], [], "N/A")
    child = Card("Child 13", 0, 1, "1B", "Hooved", ["Many Lives"], [], "child0")
    kingfisher = Card("Kingfisher", 1, 1, "1B", "Avian", ["Airborne", "Waterborne"], [], "N/A")
    maggot = Card("Corpse Maggots", 1, 2, "5N", "Insect", ["Corpse Eater"], [], "N/A")
    magpie = Card("Magpie", 1, 1, "2B", "Avian", ["Airborne", "Hoarder"], [], "N/A")
    mantis = Card("Mantis", 1, 1, "1B", "Insect", ["Bifurcated Strike"], [], "N/A")
    god = Card("Mantis God", 1, 1, "1B", "Insect", ["Trifurcated Strike"], [], "N/A")
    mole = Card("Mole", 0, 4, "1B", "N/A", ["Burrower"], [], "N/A")
    molebig = Card("Mole Man", 0, 6, "1B", "N/A", ["Burrower", "Mighty Leap"], [], "N/A")
    buck = Card("Moose Buck", 3, 7, "3B", "Hooved", ["Hefty"], [], "N/A")
    larva = Card("Strange Larva", 0, 3, "1B", "Insect", ["Fledgling"], [], "N/A")
    pupa = Card("Strange Pupa", 0, 3, "1B", "Insect", ["Fledgling"], [], "N/A")
    mothman = Card("Mothman", 7, 3, "1B", "Insect", ["Airborne"], [], "N/A")
    mule = Card("Pack Mule", 0, 5, "0N", "Hooved", ["Sprinter"], [], "pack mule")
    opossum = Card("Opossum", 1, 1, "2N", "N/A", [], [], "N/A")
    otter = Card("River Otter", 1, 1, "1B", "N/A", ["Waterborne"], [], "N/A")
    boros = Card("Ouroboros", 1, 1, "2B", "Reptile", ["Unkillable"], [], "ouroboros")
    rat = Card("Pack Rat", 2, 2, "2B", "N/A", ["Trinket Bearer"], [], "N/A")
    porci = Card("Porcupine", 1, 2, "1B", "N/A", ["Sharp Quills"], [], "N/A")
    prong = Card("Pronghorn", 1, 3, "2B", "Hooved", ["Sprinter", "Bifurcated Strike"], [], "N/A")
    rabbit = Card("Rabbit", 0, 1, "0N", "N/A", [], [], "N/A")
    king = Card("Rat King", 2, 1, "2B", "N/A", ["Bone King"], [], "N/A")
    rattle = Card("Rattler", 3, 1, "6N", "Reptile", [], [], "N/A")
    raven = Card("Raven", 2, 3, "2B", "Avian", ["Airborne"], [], "N/A")
    ravegg = Card("Raven Egg", 0, 2, "1B", "Avian", ["Fledgling"], [], "N/A")
    shark = Card("Great White", 4, 2, "3B", "N/A", ["Waterborne"], [], "N/A")
    skink = Card("Skink", 1, 2, "1B", "Reptile", ["Loose Tail"], [], "N/A")
    skunk = Card("Skunk", 0, 3, "1B", "N/A", ["Stinky"], [], "N/A")
    turt = Card("River Snapper", 1, 6, "2B", "Reptile", [], [], "N/A")
    lelk = Card("Long Elk", 1, 2, "4N", "Hooved", ["Sprinter", "Touch of Death"], [], "long elk")
    spar = Card("Sparrow", 1, 2, "1B", "Avian", ["Airborne"], [], "N/A")
    tentB = Card("Bell Tentacle", "bellpow", 3, "2B", "N/A", [], [], "chime")
    tentC = Card("Hand Tentacle", "cardpow", 1, "1B", "N/A", [], [], "N/A")
    tentM = Card("Mirror Tentacle", "mirrpow", 1, "1B", "N/A", [], [], "N/A")
    squirrel = Card("Squirrel", 0, 1, "0N", "Squirrel", [], [], "N/A")
    stoat = Card("Stoat", 1, 2, "1B", "N/A", [], [], "N/A")
    yuli = Card("Urayuli", 7, 7, "4B", "N/A", [], [], "N/A")
    vult = Card("Turkey Vulture", 3, 3, "8N", "Avian", ["Airborne"], [], "N/A")
    warren = Card("Warren", 0, 2, "1B", "N/A", ["Rabbit Hole"], [], "N/A")
    wolf = Card("Wolf", 3, 2, "2B", "Canine", [], [], "wolf")
    wolfcub = Card("Wolf Cub", 1, 1, "1B", "Canine", ["Fledgling"], [], "wolf")
    ringworm = Card("Ring Worm", 0, 1, "1B", "Insect", [], [], "kills survivors")
    bull = Card("Wild Bull", 3, 2, "2B", "Hooved", ["Rampager"], [], "N/A")
    cuckoo = Card("Cuckoo", 1, 1, "1B", "Avian", ["Airborne", "Brood Parasite"], [], "N/A")
    ijiraq = Card("Ijiraq", 4, 1, "0N", "N/A", ["Repulsive"], [], "ijiraq")
    antFly = Card("Flying Ant", "antpow", 1, "1B", "Insect", ["Airborne"], [], "ant")
    mudturt = Card("Mud Turtle", 2, 2, "2B", "Reptile", ["Armored"], [], "N/A")
    direpup = Card("Dire Wolf Pup", 1, 1, "2B", "Canine", ["Bone Digger", "Fledgling"], [], "N/A")
    direwolf = Card("Dire Wolf", 2, 5, "3B", "Canine", ["Double Strike"], [], "N/A")
    mealworm = Card("Mealworm", 0, 2, "2N", "Insect", ["Morsel"], [], "N/A")
    wolvi = Card("Wolverine", 1, 3, "5N", "N/A", ["Blood Lust"], [], "N/A")
    racoon = Card("Racoon", 1, 1, "1B", "N/A", ["Scavenger"], [], "N/A")
    lamm = Card("Lammergeier", "bonpow", 4, "3B", "Avian", ["Airborne"], [], "N/A")
    hart = Card("Red Hart", "blodpow", 2, "2B", "Hooved", ["Sprinter"], [], "N/A")
    tadpole = Card("Tadpole", 0, 1, "0N", "Reptile", ["Waterborne", "Fledgling"], [], "N/A")
    lice = Card("Pelt Lice", 1, 1, "4B", "Insect", ["Double Strike"], [], "pelt lice")
    hodag = Card("Hodag", 1, 5, "2B", "N/A", ["Blood Lust"], [], "hodag")
    kraken = Card("Great Kraken", 1, 1, "1B", "N/A", ["Waterborne"], [], "N/A")
    cegg = Card("Curious Egg", 0, 1, "1N", "N/A", ["Finical Hatchling"], [], "N/A")
    hydra = Card("Hydra", 1, 5, "1N", "YES", ["Bifurcated Strike", "Trifurcated Strike"], [], "N/A")

    pelt1 = Card("Rabbit Pelt", 0, 1, "0N", "N/A", [], [], "pelt1")
    pelt2 = Card("Wolf Pelt", 0, 2, "0N", "N/A", [], [], "pelt1")
    pelt3 = Card("Golden Pelt", 0, 3, "0N", "N/A", [], [], "pelt1")

    Boulder = Card("Boulder", 0, 5, "0N", "N/A", [], [], "terrain")
    Dam = Card("Dam", 0, 2, "0N", "N/A", [], [], "terrain")
    GrandFir = Card("Grand Fir", 0, 3, "0N", "N/A", ["Mighty Leap"], [], "terrain")
    SnowFir = Card("Snowy Fir", 0, 4, "0N", "N/A", ["Mighty Leap"], [], "terrain")
    Stump = Card("Stump", 0, 3, "0N", "N/A", [], [], "terrain")
    chime = Card("Chime", 0, 1, "0N", "N/A", [], [], "chime")
    eggbrok = Card("Broken Egg", 0, 1, "0N", "N/A", [], [], "terrain")
    possfroz = Card("Frozen Opossum", 0, 5, "0N", "N/A", ["Frozen Away"], [], "terrain")
    childhung = Card("Hungry Child", 0, 0, "0N", "N/A", [], [], "N/A")
    vert = Card("Vertebrae", 0, 1, "0N", "Hooved", [], [], "N/A")
    glitch = Card("", 0, 0, "0N", "", [], [], "glitch")
    sfrog = Card("Strange Frog", 1, 2, "1B", "Reptile", ["Mighty Leap"], [], "terrain")
    trap = Card("Leaping Trap", 0, 1, "0N", "N/A", ["Mighty Leap", "Steel Trap"], [], "terrain")
    bbucket = Card("Bait Bucket", 0, 1, "0N", "N/A", [], [], "terrain")
    nugget = Card("Gold Nugget", 0, 2, "0N", "N/A", [], [], "terrain")

    Tamara = Card("Tamara", 2, 3, "2B", "N/A", ["Airborne", "Loose Tail"], [], "N/A")
    Kaycee = Card("Kaycee", 1, 2, "1B", "N/A", ["Bifurcated Strike", "Sharp Quills"], [], "N/A")
    David = Card("David", 2, 4, "2B", "N/A", ["Hefty", "Sharp Quills"], [], "N/A")
    Reginald = Card("Reginald", 1, 3, "3N", "N/A", ["Touch of Death"], [], "N/A")
    Louis = Card("Louis", 1, 1, "1B", "N/A", ["Sprinter", "Waterborne"], [], "N/A")
    Cody = Card("Cody", 3, 1, "2B", "N/A", ["Burrower", "Loose Tail"], [], "N/A")
    Berke = Card("Berke", 2, 1, "2B", "N/A", ["Frozen Away", "Guardian"], [], "N/A")
    Sean = Card("Sean", 1, 6, "2B", "N/A", ["Mighty Leap", "Touch of Death"], [], "N/A")
    Oct19 = Card("Oct 19", 3, 2, "1B", "N/A", ["Touch of Death"], [], "N/A")
    Kaminski = Card("Kaminski", 0, 1, "1N", "N/A", ["Guardian", "Sharp Quills"], [], "N/A")
    LukeCarder = Card("Luke Carder", 4, 4, "0N", "N/A", [], [], "N/A")
    Jonah = Card("Jonah", 2, 5, "3B", "N/A", ["Bees Within", "Sharp Quills"], [], "N/A")
    Daniel = Card("Daniel", 2, 2, "2B", "N/A", ["Double Strike"], [], "N/A")
    all_cards = [
        adder, alpha, amalg, ameba, antWork, antQ, bat, bever, bee, hive, hound,
        frog, cage, cat, uncat, roach, coyote, daus, tail, elk, elkfawn, mice, geck,
        goat, bear, child, kingfisher, maggot, magpie, mantis, god, mole, molebig,
        buck, larva, pupa, mothman, mule, opossum, otter, boros, rat, porci, prong,
        rabbit, king, rattle, raven, ravegg, shark, skink, skunk, turt, lelk, spar,
        tentB, tentC, tentM, squirrel, stoat, yuli, vult, warren, wolf, wolfcub,
        ringworm, bull, cuckoo, ijiraq, antFly, mudturt, direpup, direwolf, mealworm,
        wolvi, racoon, lamm, hart, tadpole, lice, hodag, kraken, cegg, hydra,
        pelt1, pelt2, pelt3,
        Boulder, Dam, GrandFir, Stump, chime, eggbrok, possfroz, childhung, vert, glitch,
        sfrog, trap, bbucket, nugget,
        Tamara, Kaycee, David, Reginald, Louis, Cody, Berke, Sean, Oct19, Kaminski, LukeCarder, Jonah, Daniel
    ]
    for n in all_cards:
        if choice == n.name:
            return n
    print("Uhh... yeah "+choice+" is not a card you can define.")
    z = "erm awkward"
    # Force quit
    print(z+1)

def get_cardlist(group, num):
    if group == "rare":
        group = [create_card("Amalgam"), create_card("Amoeba"), create_card("Child 13"), create_card("Geck"), create_card("Hodag"), create_card("Ijiraq"),
                 create_card("Long Elk"), create_card("Mantis God"), create_card("Mole Man"), create_card("Strange Larva"), create_card("Ouroboros"), create_card("Pack Rat"), create_card("Pelt Lice"),
                 create_card("The Daus"), create_card("Urayuli")]
    elif group == "deathcards":
        group = [create_card("Tamara"), create_card("Kaycee"), create_card("David"), create_card("Reginald"), create_card("Louis"), create_card("Cody"),
                 create_card("Berke"), create_card("Sean"), create_card("Oct 19"), create_card("Kaminski"), create_card("Luke Carder"),
                 create_card("Jonah"), create_card("Daniel")]
    else:
        common = [
            create_card("Adder"), create_card("Alpha"), create_card("Worker Ant"),create_card("Ant Queen"), create_card("Bat"), create_card("Beaver"), create_card("Beehive"), create_card("Bloodhound"),
            create_card("Bullfrog"), create_card("Cat"), create_card("Cockroach"), create_card("Coyote"), create_card("Elk"), create_card("Elk Fawn"), create_card("Field Mice"), create_card("Black Goat"),
            create_card("Grizzly"), create_card("Kingfisher"), create_card("Corpse Maggots"), create_card("Magpie"), create_card("Mantis"), create_card("Mole"), create_card("Moose Buck"),
            create_card("Opossum"), create_card("River Otter"), create_card("Porcupine"), create_card("Pronghorn"), create_card("Rat King"), create_card("Rattler"), create_card("Raven"),
            create_card("Raven Egg"), create_card("Great White"), create_card("Skink"), create_card("Skunk"), create_card("Mud Turtle"), create_card("Sparrow"), create_card("Bell Tentacle"),
            create_card("Hand Tentacle"), create_card("Mirror Tentacle"), create_card("Stoat"), create_card("Turkey Vulture"), create_card("Warren"), create_card("Mealworm"), create_card("Wolverine"),
            create_card("Racoon"), create_card("Lammergeier"), create_card("Red Hart"), create_card("Tadpole"), create_card("")
        ]
        if group == "cost1":
            group = [card for card in common if card.cost == "1B"]
        elif group == "cost2":
            group = [card for card in common if card.cost == "2B"]
        elif group == "cost3":
            group = [card for card in common if card.cost == "3B"]
        elif group == "costb":
            group = [card for card in common if card.cost[-1] == "N" and card.cost[0] != "0"]
        elif group == "reptiles":
            group = [card for card in common if card.tribe == "Reptile" or card.tribe == "YES"]
        elif group == "insects":
            group = [card for card in common if card.tribe == "Insect" or card.tribe == "YES"]
        elif group == "avians":
            group = [card for card in common if card.tribe == "Avian" or card.tribe == "YES"]
        elif group == "canines":
            group = [card for card in common if card.tribe == "Canine" or card.tribe == "YES"]
        elif group == "hooved":
            group = [card for card in common if card.tribe == "Hooved" or card.tribe == "YES"]
        elif group == "common":
            group = common
        else:
            print("Uhh... yeah that's not a list you can get.")
            z = "erm awkward"
            # Force quit
            print(z+1)
    return random.sample(group, num)

# Prints a list of cards (hand, board, etc)
def printcards(cardlist):
    c = cardlist.copy()
    if len(c) <= 7:
        for m in range(12):
            printed = []
            for n in c:
                if n == 0:
                    n = Empty
                printed.append(str(n)[(m*14):(m+1)*14])
            print(" ".join(printed))
    elif len(c) % 7 == 0:
        for k in range(int(len(c)/7)):
            for m in range(12):
                printed = []
                for n in c[(k*7):(k+1)*7]:
                    if n == 0:
                        n = Empty
                    printed.append(str(n)[(m*14):(m+1)*14])
                print(" ".join(printed))
    else:
        for k in range(int(len(c)/7)+1):
            for m in range(12):
                printed = []
                for n in c[(k*7):(k+1)*7]:
                    if n == 0:
                        n = Empty
                    printed.append(str(n)[(m*14):(m+1)*14])
                print(" ".join(printed))

# Prints the current board state
def print_board(player1, player2):
    lane1 = []
    lane2 = []
    for n in player1.board:
        if n == 0:
            lane1.append(Empty)
        else:
            lane1.append(str(n))
    for n in player2.board:
        if n == 0:
            lane2.append(Empty)
        else:
            lane2.append(str(n))
    printcards(lane1)
    printcards(lane2)

# Whenever someone needs to pick a card
def pickcard(cards):
    while True:
        printcards(cards)
        print("Make your choice.")
        choices = []
        choicenum = []
        picked = input()
        for n in range(len(cards)):
            if cards[n] != 0:
                if picked.lower() == cards[n].name.lower():
                    choices.append(cards[n])
                    choicenum.append(n)
        if len(choices) == 0:
            if picked[0] == "?":
                print("Have a question?")
                sigilq = []
                for n in cards:
                    for m in n.sigils:
                        if m not in sigilq:
                            sigilq.append(m)
                    for m in n.sigils2:
                        if m not in sigilq:
                            sigilq.append(m)
                print("Here is what you can ask about:")
                print(", ".join(sigilq))
                choice2 = input()
                for n in sigilList:
                    if choice2.lower() == n.lower():
                        print(Sigils[sigilList.index(n)])
                        print("Description: "+sigilDesc[sigilList.index(n)])
                for m in itemList:
                    if choice2.lower() == m.lower():
                        print(itemDispl[itemList.index(m)])
                        print("Description: "+itemDesc[itemList.index(m)])
            else:
                print("... That card is unavailable.")
        elif len(choices) == 1:
            return choicenum[0]
        else:
            print("More than one of this card were presented.")
            print(str(len(choices))+", to be exact.")
            while True:
                printcards(choices)
                print("Please give a number, or N if you changed your mind.")
                choice2 = input()
                try:
                    choice2 = int(choice2)
                    if choice2-1 <= len(choices):
                        return choicenum[choice2-1]
                except ValueError:
                    if choice2.lower()[0] == "n":
                        break

create_card("Luke Carder")
