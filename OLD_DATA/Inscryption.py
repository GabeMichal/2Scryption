import random
# importing all lists for items/sigils
from Scryption_Item_Sigil import *
# importing card class as well as all cards/list of cards
from Scrypt_card import *
# import player class as well as all functions involved
from Scrypt_player import *
# import all functions involved in battling
from Scrypt_battle import *

print("First things first: set a seed. (Print 'a' if you don't want one)")
while True:
    sead = input()
    if sead == "a":
        break
    else:
        try:
            sead = int(sead)
            random.seed(sead)
            break
        except ValueError:
            print("Invalid value. Try again.")

# Two players
p1name = input("\nPlayer 1, enter your name. ")
player1 = Player(p1name)
p2name = input("Player 2, enter your name. ")
player2 = Player(p2name)

# Options for the players to choose decks from
deckopts = [[create_card("Stoat"), create_card("Bullfrog"), create_card("Wolf")],
            [create_card("Black Goat"), create_card("Moose Buck"), create_card("Mole")],
            [create_card("Ant Queen"), create_card("Flying Ant"), create_card("Skunk")],
            [create_card("Mantis God"), create_card("Ring Worm"), create_card("Ring Worm")],
            [create_card("Kingfisher"), create_card("Kingfisher"), create_card("Great Kraken")],
            [create_card("Racoon"), create_card("Dire Wolf Pup"), create_card("Coyote")],
            [create_card("Rabbit"), create_card("Tadpole"), create_card("Geck")],
            [create_card("Curious Egg"), create_card("Curious Egg"), create_card("Curious Egg")]]

# Create a deck of cards and shuffle it
print(f"\n{player1.name}, select a deck.")
while True:
    #Player 1 chooses a deck
    print("Here are your options:")
    print("Vanilla:")
    printcards(deckopts[0])
    print("\nHigh Cost:")
    printcards(deckopts[1])
    print("\nAnt:")
    printcards(deckopts[2])
    print("\nMantis God:")
    printcards(deckopts[3])
    print("\nWaterborne:")
    printcards(deckopts[4])
    print("\nBone:")
    printcards(deckopts[5])
    print("\nNo Cost:")
    printcards(deckopts[6])
    print("\nCurious Egg:")
    printcards(deckopts[7])
    deck = input()
    deck = deck.lower()
    if deck == "vanilla":
        player1.cards.append(create_card("Stoat"))
        player1.cards.append(create_card("Bullfrog"))
        player1.cards.append(create_card("Wolf"))
    elif deck == "high cost":
        player1.cards.append(create_card("Black Goat"))
        player1.cards.append(create_card("Moose Buck"))
        player1.cards.append(create_card("Mole"))
    elif deck == "ant":
        player1.cards.append(create_card("Ant Queen"))
        player1.cards.append(create_card("Flying Ant"))
        player1.cards.append(create_card("Skunk"))
    elif deck == "mantis god":
        player1.cards.append(create_card("Mantis God"))
        player1.cards.append(create_card("Ring Worm"))
        player1.cards.append(create_card("Ring Worm"))
    elif deck == "waterborne":
        player1.cards.append(create_card("Kingfisher"))
        player1.cards.append(create_card("Kingfisher"))
        player1.cards.append(create_card("Great Kraken"))
    elif deck == "bone":
        player1.cards.append(create_card("Racoon"))
        player1.cards.append(create_card("Dire Wolf Pup"))
        player1.cards.append(create_card("Coyote"))
    elif deck == "no cost":
        player1.cards.append(create_card("Rabbit"))
        player1.cards.append(create_card("Tadpole"))
        player1.cards.append(create_card("Geck"))
    elif deck == "curious egg":
        player1.cards.append(create_card("Curious Egg"))
        player1.cards.append(create_card("Curious Egg"))
        player1.cards.append(create_card("Curious Egg"))
    else:
        print("Not an option! Try again!")
    if player1.cards != []:
        player1.cards.append(create_card("Rabbit Pelt"))
        player1.cards.append(create_card("Rabbit Pelt"))
        break
print("Your deck is of the following cards:")
printcards(player1.cards)
print("\n")

print(f"{player2.name}, select a deck.")
while True:
    #Player 2 chooses a deck
    print("Here are your options:")
    print("Vanilla:")
    printcards(deckopts[0])
    print("\nHigh Cost:")
    printcards(deckopts[1])
    print("\nAnt:")
    printcards(deckopts[2])
    print("\nMantis God:")
    printcards(deckopts[3])
    print("\nWaterborne:")
    printcards(deckopts[4])
    print("\nBone:")
    printcards(deckopts[5])
    print("\nNo Cost:")
    printcards(deckopts[6])
    print("\nCurious Egg:")
    printcards(deckopts[7])
    deck = input()
    deck = deck.lower()
    if deck == "vanilla":
        player2.cards.append(create_card("Stoat"))
        player2.cards.append(create_card("Bullfrog"))
        player2.cards.append(create_card("Wolf"))
    elif deck == "high cost":
        player2.cards.append(create_card("Black Goat"))
        player2.cards.append(create_card("Moose Buck"))
        player2.cards.append(create_card("Mole"))
    elif deck == "ant":
        player2.cards.append(create_card("Ant Queen"))
        player2.cards.append(create_card("Flying Ant"))
        player2.cards.append(create_card("Skunk"))
    elif deck == "mantis god":
        player2.cards.append(create_card("Mantis God"))
        player2.cards.append(create_card("Ring Worm"))
        player2.cards.append(create_card("Ring Worm"))
    elif deck == "waterborne":
        player2.cards.append(create_card("Kingfisher"))
        player2.cards.append(create_card("Kingfisher"))
        player2.cards.append(create_card("Great Kraken"))
    elif deck == "bone":
        player2.cards.append(create_card("Racoon"))
        player2.cards.append(create_card("Dire Wolf Pup"))
        player2.cards.append(create_card("Coyote"))
    elif deck == "no cost":
        player2.cards.append(create_card("Rabbit"))
        player2.cards.append(create_card("Tadpole"))
        player2.cards.append(create_card("Geck"))
    elif deck == "curious egg":
        player2.cards.append(create_card("Curious Egg"))
        player2.cards.append(create_card("Curious Egg"))
        player2.cards.append(create_card("Curious Egg"))
    else:
        print("Not an option! Try again!")
    if player2.cards != []:
        player2.cards.append(create_card("Rabbit Pelt"))
        player2.cards.append(create_card("Rabbit Pelt"))
        break
print("Your deck is of the following cards:")
printcards(player2.cards)
print("\n")

# Deck trial function
def deck_trial(trial, player):
    print(player.name+", your turn.")
    # The cards the player gets
    trialcards = random.sample(player.cards,3)
    # Whether or not the player won
    win = False
    print("Here are your cards:")
    printcards(trialcards)
    print("Let us begin.")
    # Bone trial
    if trial == "Bon":
        bon = 0
        for n in trialcards:
            if n.cost[-1] == "N":
                print(n.cost[:-1]+" from "+n.name+".")
                bon+=int(n.cost[:-1])
            else:
                print("0 from "+n.name+".")
        print("That makes "+str(bon)+".")
        if bon >= 5:
            win = True
    # Blood trial
    if trial == "Blo":
        blo = 0
        for n in trialcards:
            if n.cost[-1] == "B":
                print(n.cost[:-1]+" from "+n.name+".")
                blo+=int(n.cost[:-1])
            else:
                print("0 from "+n.name+".")
        print("That makes "+str(blo)+".")
        if blo >= 4:
            win = True
    # Power check
    if trial == "Pow":
        powe = 0
        for n in trialcards:
            print(str(n.power)+" from "+n.name+".")
            powe+=n.power
        print("That makes "+str(powe)+".")
        if powe >= 4:
            win = True
    # Health check
    if trial == "Hea":
        hea = 0
        for n in trialcards:
            print(str(n.health)+" from "+n.name+".")
            hea+=n.health
        print("That makes "+str(hea)+".")
        if hea >= 6:
            win = True
    # Wisdom trial
    if trial == "Wis":
        wis = 0
        for n in trialcards:
            print(str(len(n.sigils))+" from "+n.name+".")
            wis+=len(n.sigils)
            print("That makes "+str(wis)+".")
        if wis >= 3:
            win = True
    # Kin trial
    if trial == "Kin":
        kin = trialcards
        for n in trialcards:
            print(n.tribe+" from "+n.name+".")
        if ((kin[0].tribe == kin[1].tribe or kin[1].tribe == kin[2].tribe) and kin[1].tribe != "N/A") or (kin[0].tribe == kin[2].tribe and kin[0].tribe != "N/A"):
            win = True
    # Check if the trial was won
    if win == True:
        print("Success.")
        print("Here are your possible rewards:")
        # 3 cards with 2 extra sigils
        reward = get_cardlist("common", 3)
        for n in reward:
            while len(n.sigils2) < 2:
                addit = random.choice(sigilList)
                if addit not in n.sigils2:
                    n.sigils2.append(addit)
        choose = pickcard(reward)
        print("You have claimed your "+reward[choose].name)
        player.deck.append(reward[choose])
    else:
        print("Failure.")
        
def goobert(copycard):
    newcard = Card(copycard.name, copycard.power, copycard.health, copycard.cost, copycard.tribe, copycard.sigils, copycard.sigils2, copycard.trait)
    a = random.randint(0,4)
    # if a = 0, nothing changes
    if a == 1:
        # power changes
        if random.randint(0,1) == 0:
            newcard.power += 1
        elif newcard.power > 0:
            newcard.power -= 1
    elif a == 2:
        # health changes
        if random.randint(0,1) == 0:
            newcard.health += 1
        elif newcard.health > 1:
            newcard.health -= 1
    elif a == 3:
        # sigil changes
        if len(newcard.sigils) > 0:
            siglchange = random.randint(0,len(newcard.sigils)-1)
            newcard.sigils[siglchange] = random.choice(sigilList)
        elif len(newcard.sigils2) > 0:
            siglchange = random.randint(0,len(newcard.sigils2)-1)
            newcard.sigils2[siglchange] = random.choice(sigilList)
    elif a == 4:
        # cost changes
        if newcard.cost[-1] == "B":
            if random.randint(0,1) == 0:
                newcard.cost = str(int(newcard.cost[:-1])+1)+"B"
            elif newcard.cost != "1B":
                newcard.cost = str(int(newcard.cost[:-1])-1)+"B"
            else:
                newcard.cost = "0N"
        else:
            if random.randint(0,1) == 0:
                if newcard.cost[:-1] != "0":
                    newcard.cost = str(int(newcard.cost[:-1])+1)+"N"
                else:
                    newcard.cost = "1B"
            elif newcard.cost[:-1] != "0":
                newcard.cost = str(int(newcard.cost[:-1])-1)+"N"
    print("GUUOOOH! HERE IS YOUR NEW CARD!")
    printcards([newcard])
    print("DO YOU LIKE IT? PLEASE TELL ME YOU LIKE IT!")

spaces1 = {"Battle": ["Normal"],
          "New Card": ["Card Choice", "Cost Choice", "Tribe Choice", "Trapper", "Prospector", "Trial"],
          "Support": ["Woodcarver", "Sigil swap", "Item", "Campfire"]}

spaces = {"Battle": ["Normal"],
          "New Card": ["Card Choice", "Cost Choice", "Tribe Choice", "Trapper", "Trader", "Trial"],
          "Support": ["Woodcarver", "Mycologist", "Bone", "Sigil swap", "Item", "Campfire", "Copy Card"]}
maps = [["Woodlands"], ["Wetlands"], ["Snow Line"]]
map1 = random.choice(maps)
maps.remove(map1)
map2 = random.choice(maps)
maps.remove(map2)
map3 = maps
map2 = [map2]
map1 = [map1]
maps = [map1, map2, map3]

battleNum = 4
for k in range(3):
    for n in range(battleNum):
        if n == 0 and k == 0:
            maps[k].append(["Trader"])
        spacenum = random.choice([1,1,1,2,2,3])
        if n == 0:
            maps[k].append(random.sample(spaces1["New Card"], 1))
        elif n > 0 or k > 0:
            maps[k].append(random.sample(spaces["New Card"], 1))
        for m in range(random.randint(1,2)):
            if n == 0:
                maps[k].append(random.sample(spaces1["Support"], spacenum))
            else:
                maps[k].append(random.sample(spaces["Support"], spacenum))
        if n == battleNum-1:
            maps[k].append(["Boss"])
        else:
            maps[k].append(["Battle"])

for n in range(3):
    if maps[n][0][0] == "Woodlands":
        maps[n][-1][-1] = "BOSS - Prospector"
    elif maps[n][0][0] == "Wetlands":
        maps[n][-1][-1] = "BOSS - Angler"
    else:
        maps[n][-1][-1] = "BOSS - Trapper"

finalmap = [["Trader", "Campfire", "Item", "Sigil Swap"], ["Final Boss"]]

# Knife hasn't been bought yet
knifeBought = False

# Campfire survivors alive
survDead = False

# Trial options
trials = ["Trial of Bones: The 3 drawn cards must cost at least 5 bones combined to pass.",
          "Trial of Blood: The 3 drawn cards must cost at least 4 blood combined to pass.",
          "Trial of Power: The 3 drawn cards must have at least 4 power combined to pass.",
          "Trial of Health: The 3 drawn cards must have at least 6 health combined to pass.",
          "Trial of Wisdom: The 3 drawn cards must have at least 3 sigils combined to pass.",
          "Trial of Kin: 2 of the 3 drawn cards must be kin to pass."]

# Keeps track of map number for trader
mapNum = 0

# Testing maps (comment out later)
maps = [[["Trader"]]]
player1.cards = [create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt")]
player2.cards = [create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt")]
#player1.cards = [create_card("Dire Wolf Pup"), create_card("Turkey Vulture"), create_card("Caged Wolf")]

for mapc in maps:
    mapNum+=1
    while len(mapc) > 0:
        # Make sure decks are synced up
        for n in range(len(player1.cards)):
            player1.cards[n].deckspot = n
        for n in range(len(player2.cards)):
            player2.cards[n].deckspot = n
        # Options for the player to go to; player 2 decides
        spaces = mapc[0]
        print(f"{player2.name} may choose where to go.")
        if len(spaces) > 1:
            print("The next possible spaces are: "+", ".join(spaces))
            spaceLow = spaces.copy()
            for n in range(len(spaceLow)):
                spaceLow[n] = spaceLow[n].lower()
            while True:
                selection = input()
                try:
                    selection = int(selection)
                    if selection-1 > len(spaces):
                        print("You gave a value too large.")
                    else:
                        space = mapc[0][selection-1]
                        break
                except ValueError:
                    if selection.lower() not in spaceLow:
                        print("That space is not an option.")
                    else:
                        space = spaces[spaceLow.index(selection.lower())]
                        break
        else:
            print(f"Only one path is visible: to a {spaces[0]}.")
            garbage = input()
            space = spaces[0]
            print("...")
        print("Current Space: "+space)
        # Map openers
        if space == "Woodlands":
            story = random.randint(1,4)
            if story == 1:
                print("The sun rose over the sleepy firs... Birds fluttered across the paths of wolves and elk... You were embarking upon... the Woodlands.")
            elif story == 2:
                print("Pine needles crunched beneath your feet... You drew in a breath of the fresh scented air... You were embraced by... the Woodlands.")
            elif story == 3:
                print("You beheld the beauty of the dawn... Only a faint clinking sound ahead could distract you from the sight... You set out upon... the Woodlands.")
            elif story == 4:
                print("You heard the howling of wolves, greeting the morning sun... The sight of a nearby coyote caused you to quickened your pace... You had reached... the Woodlands.")
        elif space == "Wetlands":
            story = random.randint(1,5)
            if story == 1:
                print("The rank smell of rot and mold permeated the humid air. Every step forward was answered by some nearby slip or slither. You tread cautiously into... the Wetlands.")
            elif story == 2:
                print("A hideous swarm of insects gathered around you. Reptiles slipped and slithered around your feet. You were now engulfed by... the Wetlands.")
            elif story == 3:
                print("As the air grew humid your boots became harder to pull from the mud. The dank smell of tepid water invaded your nostrils. You had reached... the Wetlands.")
            elif story == 4:
                print("Tepid water flooded your boots. Flies swarmed around you. You had entered... the Wetlands.")
            elif story == 5:
                print("The air grew thick with moisture. The buzzing and chirping of insects drowned out the sound of your footfalls. You beheld...the Wetlands.")
        elif space == "Snow Line":
            story = random.randint(1,4)
            if story == 1:
                print("A frigid gust bellowed, unwelcome, into your lungs. The beauty of the falling snow failed to distract you from the chill in your bones. You had ascended to... the Snow Line.")
            elif story == 2:
                print("Sheets of icy snow battered your body as you fought your way up to a vantage point. The snow-covered trees jutted from the landscape like prickly misplaced teeth. You continued on through... the Snow Line.")
            elif story == 3:
                print("The beauty of the falling snow could not distract you from the chill in your bones. Your body quaked in a futile attempt to maintain warmth. You had finally reached... the Snow Line.")
            elif story == 4:
                print("The relief of the fresh air quickly gave way to a bone-shaking chill. You guessed at the path ahead as the snow increasingly obscured it. You had climbed to... the Snow Line.")
        # Battles
        elif space == "Battle":
            batlwin = battle(space, player1, player2)
            if batlwin == 0:
                print("... How... disappointing.")
                print("Neither of you won...")
                print("However, I shall still reverse the player order.")
                print("If nothing else but to keep the game fresh.")
                z = player1
                player1 = player2
                player2 = z
            elif batlwin == 10:
                print("... Neither of you were strong enough to overcome the other.")
                print(f"However... {player1.name} was in the lead at the time...")
                print("So they are the winner. The player order remains the same.")
            elif batlwin == 20:
                print("... Neither of you were strong enough to overcome the other.")
                print(f"However... {player2.name} was in the lead at the time...")
                print("So they are the winner. The player order was reversed.")
                z = player1
                player1 = player2
                player2 = z
            else:
                print("The game has ended.")
                if batlwin == player1:
                    print(f"{player1.name} won... so there will be no change.")
                else:
                    print(f"{player2.name} won... so the player order shall be reversed.")
                    z = player1
                    player1 = player2
                    player2 = z
        elif space[:3] == "BOSS":
            batlwin = battle(space, player1, player2)
            if batlwin == 0:
                print("... You tie... during one of my heated boss battles.")
                print("How disappointing of you. Very well then. Neither of you will receive one of my coveted rare cards.")
            elif batlwin == 10:
                print("... You failed to finish one of my boss battles...")
                print("This is highly disappointing... however, {player1.name} was in the lead at the time...")
                print("Therefore, the player order shall remain the same.")
                print("... But no. You have not earned the right to a rare card.")
            elif batlwin == 20:
                print("... You failed to finish one of my boss battles...")
                print("This is highly disappointing... however, {player2.name} was in the lead at the time...")
                print("Therefore, the player order shall be reversed.")
                z = player1
                player1 = player2
                player2 = z
                print("... But no. You have not earned the right to a rare card.")
            else:
                print("The game has ended.")
                if batlwin == player1:
                    print(f"{player1.name} won. You may now select a rare.")
                    rarechoice = get_cardlist("rare", 3)
                    for n in range(3):
                        if rarechoice[n] == ijiraq:
                            rarechoice[n] = get_cardlist("rare",1)[0]
                            while rarechoice[n] == ijiraq:
                                rarechoice[n] = get_cardlist("rare",1)[0]
                            rarechoice[n].name = rarechoice[n].name+"?"
                            rarechoice[n].trait = "ijiraq"
                    newrare = pickcard(rarechoice)
                    if rarechoice[newrare].trait == "ijiraq":
                        rarechoice[newrare] = create_card("Ijiraq")
                    player1.cards.append(rarechoice[newrare])
                    print(f"The {rare[newrare].name} was added to your deck.")
                else:
                    print(f"{player1.name} won. First, you may select a rare.")
                    rarechoice = get_cardlist("rare",3)
                    for n in range(3):
                        if rarechoice[n] == ijiraq:
                            rarechoice[n] = get_cardlist("rare",1)[0]
                            while rarechoice[n] == ijiraq:
                                rarechoice[n] = get_cardlist("rare",1)[0]
                            rarechoice[n].name = rarechoice[n].name+"?"
                            rarechoice[n].trait = "ijiraq"
                    newrare = pickcard(rarechoice)
                    if rarechoice[newrare].trait == "ijiraq":
                        rarechoice[newrare] = create_card("Ijiraq")
                    player2.cards.append(rarechoice[newrare])
                    print(f"The {rare[newrare].name} was added to your deck.")
                    print("The player order shall also be reversed.")
                    z = player1
                    player1 = player2
                    player2 = z
        #elif space == "Final Boss": #(Leshy fight or whatever this is gonna be)
        # New Cards
        elif space == "Card Choice":
            clover1 = True
            clover2 = True
            print("You will each receive options for three cards.")
            print("You may also use a Clover, if you so desire.")
            print(f"{player1.name}, here are your options:")
            options = get_cardlist("common", 3)
            printcards(options)
            while True:
                choice = input("Would you like to use your clover (Y/N)? ")
                if choice[0].lower() == "n":
                    choice = pickcard(options)
                    print("Very well then. "+options[choice].name+" has been added to your deck.")
                    player1.cards.append(options[choice])
                    options.pop(choice)
                    break
                elif choice[0].lower() == "y":
                    if clover1 == True:
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = get_cardlist("common",3)
                        printcards(options)
                        clover1 = False
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
            print("\n")
            print(f"{player2.name}, it is your turn. You will get a choice from {player1.name}'s leftovers.")
            printcards(options)
            while True:
                choice = input("Would you like to use your clover (Y/N)? ")
                if choice[0].lower() == "n":
                    choice = pickcard(options)
                    print("Very well then. "+options[choice].name+" has been added to your deck.")
                    player2.cards.append(options[choice])
                    break
                elif choice[0].lower() == "y":
                    if clover2 == True:
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = get_cardlist("common",2)
                        printcards(options)
                        print("... Were you expecting more?")
                        clover2 = False
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
                    print(choice)
        elif space == "Cost Choice":
            clover1 = True
            clover2 = True
            print("You will each receive a choice of 3 cards... but will only get to see their costs.")
            print("You may also use a clover to reroll, if you so choose.")
            print(f"{player1.name}, here are your options:")
            options = []
            costs = random.sample(["1B", "2B", "3B", "Bones"], 3)
            costs.sort()
            if "1B" in costs:
                options.append(get_cardlist("cost1",1)[0])
            if "2B" in costs:
                options.append(get_cardlist("cost2",1)[0])
            if "3B" in costs:
                options.append(get_cardlist('cost3',1)[0])
            if "Bones" in costs:
                options.append(get_cardlist('costb',1)[0])
            for n in options:
                if n.cost[-1] == "B":
                    print(n.cost[:-1]+" Blood")
                else:
                    print("X Bones")
            while True:
                choice = input("Please provide your chosen cost. Alternatively, you may use your clover. ")
                if (choice.lower() == "1 blood" or choice == "1") and "1B" in costs:
                    print("You have gained " + options[costs.index("1B")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[costs.index("1B")])
                    options.pop(costs.index("1B"))
                    costs.remove("1B")
                    break
                elif (choice.lower() == "2 blood" or choice == "2") and "2B" in costs:
                    print("You have gained " + options[costs.index("2B")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[costs.index("2B")])
                    options.pop(costs.index("2B"))
                    costs.remove("2B")
                    break
                elif (choice.lower() == "3 blood" or choice == "3") and "3B" in costs:
                    print("You have gained " + options[costs.index("3B")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[costs.index("3B")])
                    options.pop(costs.index("3B"))
                    costs.remove("3B")
                    break
                elif (choice.lower() == "x bones" or choice.lower() == "x" or choice.lower() == "bones") and "Bones" in costs:
                    print("You have gained " + options[costs.index("Bones")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[costs.index("Bones")])
                    options.pop(costs.index("Bones"))
                    costs.remove("Bones")
                    break
                elif choice.lower() == "clover":
                    if clover1 == True:
                        clover1 = False
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = []
                        costs = random.sample(["1B", "2B", "3B", "Bones"], 3)
                        costs.sort()
                        if "1B" in costs:
                            options.append(get_cardlist('cost1',1)[0])
                        if "2B" in costs:
                            options.append(get_cardlist('cost2',1)[0])
                        if "3B" in costs:
                            options.append(get_cardlist('cost3',1)[0])
                        if "Bones" in costs:
                            options.append(get_cardlist('costb',1)[0])
                        for n in options:
                            if n.cost[-1] == "B":
                                print(n.cost[:-1]+" Blood")
                            else:
                                print("X Bones")
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
            print("\n")
            print(f"{player2.name}, it is your turn. You will receive an choice of {player1.name}'s leftovers.")
            for n in options:
                if n.cost[-1] == "B":
                    print(n.cost[:-1]+" Blood")
                else:
                    print("X Bones")
            while True:
                choice = input("Please provide your chosen cost. Alternatively, you may use your clover. ")
                if (choice.lower() == "1 blood" or choice == "1") and "1B" in costs:
                    print("You have gained " + options[costs.index("1B")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[costs.index("1B")])
                    break
                elif (choice.lower() == "2 blood" or choice == "2") and "2B" in costs:
                    print("You have gained " + options[costs.index("2B")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[costs.index("2B")])
                    break
                elif (choice.lower() == "3 blood" or choice == "3") and "3B" in costs:
                    print("You have gained " + options[costs.index("3B")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[costs.index("3B")])
                    break
                elif choice.lower() in ["x bones","x","bones"] and "Bones" in costs:
                    print("You have gained " + options[costs.index("Bones")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[costs.index("Bones")])
                    break
                elif choice.lower() == "clover":
                    if clover2 == True:
                        clover2 = False
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = []
                        costs = random.sample(["1B", "2B", "3B", "Bones"], 2)
                        if "1B" in costs:
                            options.append(get_cardlist('cost1',1)[0])
                        if "2B" in costs:
                            options.append(get_cardlist('cost2',1)[0])
                        if "3B" in costs:
                            options.append(get_cardlist('cost3',1)[0])
                        if "Bones" in costs:
                            options.append(get_cardlist('costb',1)[0])
                        for n in options:
                            if n.cost[-1] == "B":
                                print(n.cost[:-1]+" Blood")
                            else:
                                print("X Bones")
                        print("... Were you expecting more?")
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
        elif space == "Tribe Choice":
            clover1 = True
            clover2 = True
            print("You will each receive a choice of 3 cards... but will only get to see their tribes.")
            print("You may also use a clover to reroll, if you so choose.")
            print(f"{player1.name}, here are your options:")
            options = []
            tribes = random.sample(["rept", "sect", "avi", "nine", "hoof"], 3)
            tribes.sort()
            if "avi" in tribes:
                options.append(get_cardlist('avians',1)[0])
            if "hoof" in tribes:
                options.append(get_cardlist('hooved',1)[0])
            if "nine" in tribes:
                options.append(get_cardlist('canines',1)[0])
            if "rept" in tribes:
                options.append(get_cardlist('reptiles',1)[0])
            if "sect" in tribes:
                options.append(get_cardlist('insects',1)[0])
            for n in options:
                print(n.tribe)
            while True:
                if clover1 == True:
                    choice = input("Please provide your chosen tribe. Alternatively, you may use your clover. ")
                else:
                    choice = input("Please provide your chosen tribe. ")
                if choice.lower() == "reptile" and "rept" in tribes:
                    print("You have gained " + options[tribes.index("rept")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[tribes.index("rept")])
                    options.pop(tribes.index("rept"))
                    tribes.remove("rept")
                    break
                elif choice.lower() == "insect" and "sect" in tribes:
                    print("You have gained " + options[tribes.index("sect")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[tribes.index("sect")])
                    options.pop(tribes.index("sect"))
                    tribes.remove("sect")
                    break
                elif choice.lower() == "avian" and "avi" in tribes:
                    print("You have gained " + options[tribes.index("avi")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[tribes.index("avi")])
                    options.pop(tribes.index("avi"))
                    tribes.remove("avi")
                    break
                elif choice.lower() == "canine" and "nine" in tribes:
                    print("You have gained " + options[tribes.index("nine")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[tribes.index("nine")])
                    options.pop(tribes.index("nine"))
                    tribes.remove("nine")
                    break
                elif choice.lower() == "hooved" and "hoof" in tribes:
                    print("You have gained " + options[tribes.index("hoof")].name+".")
                    print("It has now been added to your deck.")
                    player1.cards.append(options[tribes.index("hoof")])
                    options.pop(tribes.index("tribes"))
                    tribes.remove("hoof")
                    break
                elif choice.lower() == "clover":
                    if clover1 == True:
                        clover1 = False
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = []
                        tribes = random.sample(["rept", "sect", "avi", "nine", "hoof"], 3)
                        tribes.sort()
                        if "avi" in tribes:
                            options.append(get_cardlist('avians',1)[0])
                        if "hoof" in tribes:
                            options.append(get_cardlist('hooved',1)[0])
                        if "nine" in tribes:
                            options.append(get_cardlist('canines',1)[0])
                        if "rept" in tribes:
                            options.append(get_cardlist('reptiles',1)[0])
                        if "sect" in tribes:
                            options.append(get_cardlist('insects',1)[0])
                        for n in options:
                            print(n.tribe)
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
            print("\n")
            print(f"{player2.name}, it is your turn. You will receive a choice from {player1.name}'s leftovers.")
            for n in options:
                print(n.tribe)
            while True:
                if clover2 == True:
                    choice = input("Please provide your chosen tribe. Alternatively, you may use your clover. ")
                else:
                    choice = input("Please provide your chosen tribe. ")
                if choice.lower() == "reptile" and "rept" in tribes:
                    print("You have gained " + options[tribes.index("rept")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[tribes.index("rept")])
                    tribes.remove("rept")
                    break
                elif choice.lower() == "insect" and "sect" in tribes:
                    print("You have gained " + options[tribes.index("sect")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[tribes.index("sect")])
                    tribes.remove("sect")
                    break
                elif choice.lower() == "avian" and "avi" in tribes:
                    print("You have gained " + options[tribes.index("avi")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[tribes.index("avi")])
                    tribes.remove("avi")
                    break
                elif choice.lower() == "canine" and "nine" in tribes:
                    print("You have gained " + options[tribes.index("nine")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[tribes.index("nine")])
                    tribes.remove("nine")
                    break
                elif choice.lower() == "hooved" and "hoof" in tribes:
                    print("You have gained " + options[tribes.index("hoof")].name+".")
                    print("It has now been added to your deck.")
                    player2.cards.append(options[tribes.index("hoof")])
                    tribes.remove("hoof")
                    break
                elif choice.lower() == "clover":
                    if clover2 == True:
                        clover2 = False
                        print("The clover was used.")
                        print("Here is your reroll:")
                        options = []
                        tribes = random.sample(["rept", "sect", "avi", "nine", "hoof"], 2)
                        tribes.sort()
                        if "avi" in tribes:
                            options.append(get_cardlist('avians',1)[0])
                        if "hoof" in tribes:
                            options.append(get_cardlist('hooved',1)[0])
                        if "nine" in tribes:
                            options.append(get_cardlist('canines',1)[0])
                        if "rept" in tribes:
                            options.append(get_cardlist('reptiles',1)[0])
                        if "sect" in tribes:
                            options.append(get_cardlist('insects',1)[0])
                        for n in options:
                            print(n.tribe)
                        print("... Were you expecting more?")
                    else:
                        print("You have already used your clover.")
                else:
                    print("That is not a viable option. Try again.")
        elif space == "Trader":
            print("You wish to trade?")
            p1peltsr = []
            p1peltsw = []
            p1peltsg = []
            p2peltsr = []
            p2peltsw = []
            p2peltsg = []
            for pelt in player1.cards:
                if pelt.name == "Rabbit Pelt":
                    p1peltsr.append(pelt)
                elif pelt.name == "Wolf Pelt":
                    p1peltsw.append(pelt)
                elif pelt.name == "Golden Pelt":
                    p1peltsg.append(pelt)
            for pelt in player2.cards:
                if pelt.name == "Rabbit Pelt":
                    p2peltsr.append(pelt)
                elif pelt.name == "Wolf Pelt":
                    p2peltsw.append(pelt)
                elif pelt.name == "Golden Pelt":
                    p2peltsg.append(pelt)
            rab = len(p1peltsr)
            rab2 = len(p2peltsr)
            wol = len(p1peltsw)
            wol2 = len(p2peltsw)
            gol = len(p1peltsg)
            gol2 = len(p2peltsg)
            if rab > 0 or rab2 > 0:
                print("Here are your options for Rabbit Pelts:")
                maxh1 = 0
                for pelt in p1peltsr:
                    if int(pelt.trait[-1]) > maxh1:
                        maxh1 = int(pelt.trait[-1])
                for pelt in p2peltsr:
                    if int(pelt.trait[-1]) > maxh1:
                        maxh1 = int(pelt.trait[-1])
                # Choose from 8 common cards
                options = get_cardlist('common', 8)
                for card in range(8):
                    # Check for fused cards
                    options[card].health *= maxh1
                    options[card].power *= maxh1
                printcards(options)
                while True:
                    # Trading time
                    if rab > 0:
                        print(f"{player1.name}, your turn.")
                        print("You have "+str(rab)+" Rabbit Pelts left.")
                        rabcheck = rab
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player1.cards.append(card)
                                player1.cards.remove(p1peltsr[0])
                                p1peltsr.pop(0)
                                options.remove(card)
                                rab -= 1
                                break
                        if rab == rabcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if rab == 0:
                            print("That was your final Rabbit Pelt.")
                    if rab2 > 0:
                        print(f"{player2.name}, your turn.")
                        print("You have "+str(rab2)+" Rabbit Pelts left.")
                        rabcheck = rab2
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player2.cards.append(card)
                                player2.cards.remove(p2peltsr[0])
                                p2peltsr.pop(0)
                                options.remove(card)
                                rab2 -= 1
                                break
                        if rab2 == rabcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if rab2 == 0:
                            print("That was your final Rabbit Pelt.")
                    if rab2 == 0 and rab == 0:
                        print("You are both out of Rabbit Pelts.")
                        print("... Very well then.")
                        break
                    if len(options) == 0:
                        print("... You have rid me of my stock.")
                        print("... For now, that is.")
                        break
            if wol > 0 or wol2 > 0:
                print("Here are your options for Wolf Pelts:")
                maxh2 = 0
                for pelt in p1peltsw:
                    if int(pelt.trait[-1]) > maxh2:
                        maxh2 = int(pelt.trait[-1])
                for pelt in p2peltsw:
                    if int(pelt.trait[-1]) > maxh2:
                        maxh2 = int(pelt.trait[-1])
                # Choose from 8 common cards
                options = get_cardlist('common', 8)
                for card in range(8):
                    # Add sigils
                    options[card].sigils2 = random.sample(sigilList2, 2)
                    # Check for fused cards
                    options[card].health *= maxh2
                    options[card].power *= maxh2
                printcards(options)
                while True:
                    # Trading time x2
                    if wol > 0:
                        print(f"{player1.name}, your turn.")
                        print("You have "+str(wol)+" Wolf Pelts left.")
                        wolcheck = wol
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player1.cards.append(card)
                                player1.cards.remove(p1peltsw[0])
                                p1peltsw.pop(0)
                                options.remove(card)
                                wol -= 1
                                break
                        if wol == wolcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if wol == 0:
                            print("That was your final Wolf Pelt.")
                    if wol2 > 0:
                        print(f"{player2.name}, your turn.")
                        print("You have "+str(wol2)+" Wolf Pelts left.")
                        wolcheck = wol2
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player2.cards.append(card)
                                player2.cards.remove(p2peltsw[0])
                                p2peltsw.pop(0)
                                options.remove(card)
                                wol2 -= 1
                                break
                        if wol2 == wolcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if wol2 == 0:
                            print("That was your final Wolf Pelt.")
                    if wol2 == 0 and wol == 0:
                        print("You are both out of Wolf Pelts.")
                        print("... Very well then.")
                        break
                    if len(options) == 0:
                        print("... You have rid me of my stock.")
                        print("... For now, that is.")
                        break
            if gol > 0 or gol2 > 0:
                print("Here are your options for Golden Pelts:")
                maxh3 = 0
                for pelt in p1peltsg:
                    if int(pelt.trait[-1]) > maxh3:
                        maxh3 = int(pelt.trait[-1])
                for pelt in p2peltsg:
                    if int(pelt.trait[-1]) > maxh3:
                        maxh3 = int(pelt.trait[-1])
                # Choose from r rare cards
                options = get_cardlist('rare', 4)
                for card in range(4):
                    if options[card].name == "Ijiraq":
                        while options[card].name == "Ijiraq":
                            options[card] = get_cardlist('rare', 1)[0]
                    # Check for fused cards
                    options[card].health *= maxh3
                    options[card].power *= maxh3
                printcards(options)
                while True:
                    # Trading time x3
                    if gol > 0:
                        print(f"{player1.name}, your turn.")
                        print("You have "+str(gol)+" Golden Pelts left.")
                        golcheck = gol
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player1.cards.append(card)
                                player1.cards.remove(p1peltsg[0])
                                p1peltsg.pop(0)
                                options.remove(card)
                                gol -= 1
                                break
                        if gol == golcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if gol == 0:
                            print("That was your final Golden Pelt.")
                    if gol2 > 0:
                        print(f"{player2.name}, your turn.")
                        print("You have "+str(gol2)+" Golden Pelts left.")
                        golcheck = gol2
                        choice = input("Please give the name of your chosen creature. ")
                        for card in options:
                            if choice.lower() == card.name.lower():
                                print("Taken the "+card.name+".")
                                player2.cards.append(card)
                                player2.cards.remove(p2peltsg[0])
                                p2peltsg.pop(0)
                                options.remove(card)
                                gol2 -= 1
                                break
                        if gol2 == golcheck:
                            print("That is not a viable option. Your turn has been skipped.")
                        if gol2 == 0:
                            print("That was your final Golden Pelt.")
                    if gol2 == 0 and gol == 0:
                        print("You are both out of Golden Pelts.")
                        print("... Very well then.")
                        break
                    if len(options) == 0:
                        print("... You have rid me of my stock.")
                        print("... For now, that is.")
                        break
            print("...")
        elif space == "Trapper":
            if mapNum == 1:
                rprice = 2
                wprice = 4
                gprice = 7
            elif mapNum == 2:
                rprice = 2
                wprice = 5
                gprice = 9
            else:
                rprice = 3
                wprice = 6
                gprice = 11
            print(f"{player1.name}, you have: "+str(player1.teeth)+" teeth.")
            print("You get 1 Rabbit Pelt for free.")
            player1.cards.append(create_card("Rabbit Pelt"))
            print("Here're your options:")
            if knifeBought == False:
                print(f"Rabbit Pelt ({str(rprice)} Teeth)")
                print(f"Wolf Pelt ({str(wprice)} Teeth)")
                print(f"Golden Pelt ({str(gprice)} Teeth)")
                print("Skinning Knife (7 Teeth)")
            else:
                print(f"Rabbit Pelt ({str(rprice)} Teeth)")
                print(f"Wolf Pelt ({str(wprice)} Teeth)")
                print(f"Golden Pelt ({str(gprice)} Teeth)")
            printcards([create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt")])
            if player1.teeth >= rprice:
                while True:
                    print(f"You have {str(player1.teeth)} remaining.")
                    print("So? What'll it be? (done to leave) ")
                    buy = input()
                    if buy.lower() == "rabbit pelt" and player1.teeth >= rprice:
                        print("Gained a Rabbit Pelt.")
                        player1.cards.append(create_card("Rabbit Pelt"))
                        player1.teeth -= rprice
                    elif buy.lower() == "wolf pelt" and player1.teeth >= wprice:
                        print("Gained a Wolf Pelt.")
                        player1.cards.append(create_card("Wolf Pelt"))
                        player1.teeth -= wprice
                    elif buy.lower() == "golden pelt" and player1.teeth >= gprice:
                        print("Gained a Golden Pelt.")
                        player1.cards.append(create_card("Golden Pelt"))
                        player1.teeth -= gprice
                    elif buy.lower() == "skinning knife" and player1.teeth >= 7 and knifeBought == False:
                        if len(player1.items) < 3:
                            print("Gained a Skinning Knife.")
                            player1.items.append("Skinning Knife")
                            player1.teeth -= 7
                            knifeBought = True
                        else:
                            print("Looks like your bag's too full.")
                    elif buy.lower() == "skinning knife" and player1.teeth >= 7:
                        print("That's out o' stock, buddy.")
                    elif buy.lower() == "done":
                        break
                    else:
                        print("Whoops! Not enough for that one!")
            else:
                print("...")
                print("No teeth, no trade.")
            print(f"{player2.name}, you have: "+str(player2.teeth)+" teeth.")
            print("You get 1 Rabbit Pelt for free.")
            player2.cards.append(create_card("Rabbit Pelt"))
            print("Your options are:")
            if knifeBought == False:
                print(f"Rabbit Pelt ({str(rprice)} Teeth)")
                print(f"Wolf Pelt ({str(wprice)} Teeth)")
                print(f"Golden Pelt ({str(gprice)} Teeth)")
                print("Skinning Knife (7 Teeth)")
            else:
                print(f"Rabbit Pelt ({str(rprice)} Teeth)")
                print(f"Wolf Pelt ({str(wprice)} Teeth)")
                print(f"Golden Pelt ({str(gprice)} Teeth)")
            printcards([create_card("Rabbit Pelt"), create_card("Wolf Pelt"), create_card("Golden Pelt")])
            if player2.teeth >= 2:
                while True:
                    print("So? What'll it be? (done to leave) ")
                    buy = input()
                    if buy.lower() == "rabbit pelt" and player2.teeth >= rprice:
                        print("Gained a Rabbit Pelt.")
                        player2.cards.append(create_card('Rabbit Pelt'))
                        player2.teeth -= rprice
                    elif buy.lower() == "wolf pelt" and player2.teeth >= wprice:
                        print("Gained a Wolf Pelt.")
                        player2.cards.append(create_card('Wolf Pelt'))
                        player2.teeth -= wprice
                    elif buy.lower() == "golden pelt" and player2.teeth >= gprice:
                        print("Gained a Golden Pelt.")
                        player2.cards.append(create_card('Golden Pelt'))
                        player2.teeth -= gprice
                    elif buy.lower() == "skinning knife" and player2.teeth >= 7 and knifeBought == False:
                        if len(player2.items) < 3:
                            print("Gained the Skinning Knife.")
                            player2.items.append("Skinning Knife")
                            player2.teeth -= 7
                            knifeBought = True
                        else:
                            print("Looks like your bag's too full.")
                    elif buy.lower() == "skinning knife" and player2.teeth >= 7:
                        print("That's out o' stock, buddy.")
                    elif buy.lower() == "done":
                        break
                    else:
                        print("Whoops! Not enough for that one!")
            else:
                print("...")
                print("No teeth, no trade.")
        elif space == "Prospector":
            print("Show me where to strike! One for each o' ya!")
            boulders = []
            bugs = get_cardlist('insects',2)
            for n in range(2):
                while bugs[n].name == "Ring Worm":
                    bugs[n] = get_cardlist('insects',1)[0]
            for n in range(2):
                sigl = random.choice(sigilList)
                bugs[n].sigils2.append(sigl)
                break
            boulders = bugs
            boulders.append(create_card("Golden Pelt"))
            random.shuffle(boulders)
            printcards([create_card("Boulder"), create_card("Boulder"), create_card("Boulder")])
            print(f"{player1.name}, ye go first! Pick a number!")
            while True:
                while True:
                    choice1 = input()
                    try:
                        choice1 = int(choice1)
                        break
                    except ValueError:
                        print("Gimme a number, I said! 1-3!")
                if choice1 <= 3:
                    print("Boulder "+str(choice1)+" broken!")
                    printcards([boulders[choice1-1]])
                    if boulders[choice1-1].name == "Golden Pelt":
                        print("Ye struck gold!")
                    else:
                        print("Bah! Nothin' but varmint!")
                    print("Ye can keep it!")
                    player1.cards.append(boulders[choice1-1])
                    break
                else:
                    print("Gimme a number, I said! 1-3!")
            print(f"{player2.name}, yer up! Pick a number!")
            while True:
                while True:
                    choice2 = input()
                    try:
                        choice2 = int(choice2)
                        break
                    except ValueError:
                        print("Gimme a number, I said! 1-3!")
                if choice2 == choice1:
                    print("That one's broken already! Try 'gain!")
                elif choice2 <= 3:
                    print("Boulder "+str(choice2)+" broken!")
                    print("It's: ")
                    printcards([boulders[choice2-1]])
                    if boulders[choice2-1].name == "Golden Pelt":
                        print("Ye struck gold!")
                    else:
                        print("Bah! Nothin' but varmint!")
                    print("Ye can keep it!")
                    player2.cards.append(boulders[choice2-1])
                    break
                else:
                    print("Gimme a number, I said! 1-3!")
        elif space == "Trial":
            print("A pair of eyes stare from within a dark cave.")
            print("Strangely, they appear to be looking at both of you at once.")
            print("The creature offers an assortment of trials.")
            print(f"{player1.name} may select the trial to be taken.")
            print("Any who pass will receive a reward.")
            print("Here are the possible trials:")
            trialopts = random.sample(trials, 3)
            trialopts2 = []
            for n in trialopts:
                trialopts2.append(n[9:12].lower())
                print(n)
            print("Select a trial.")
            while True:
                choice = input()
                if choice == "1" or choice == "2" or choice == "3":
                    choice = int(choice)
                    trial = trialopts[choice-1]
                    print(trial)
                    trial = trial[9:12]
                    break
                elif choice[0:3].lower() in trialopts2:
                    trial = trialopts[trialopts2.index(choice[0:3].lower())]
                    print(trial)
                    trial = trial[9:12]
                    break
                else:
                    print("That trial is not valid.")
            deck_trial(trial, player1)
            deck_trial(trial, player2)
        elif space == "Copy Card":
            print("You come across... Oh dear.")
            print("GUUUOOOH! TWO CUSTOMERS! MASTER WILL BE TWICE AS PROUD!")
            print("WHAT SHALL I PAINT?")
            print(f"... As usual, you should take turns. {player1.name} may go.")
            print("GIVE ME A CARD SO I CAN PAINT!!!")
            copied = pickcard(player1.cards)
            copycard = player1.cards[copied]
            newcard = goobert(copycard)
            player1.deck.append(newcard)
            print(f"... {player2.name}. You are next.")
            print("GIVE ME A CARD SO I CAN PAINT!!!")
            copied = pickcard(player2.cards)
            copycard = player2.cards[copied]
            newcard = goobert(copycard)
            player2.cards.append(newcard)
            print("... Well. That is over with.")
        # Support
        elif space == "Woodcarver":
            print("You came upon the old Woodcarver who fixed her intense gaze upon you. After an overlong moment of silence, she moved to offer her carvings.")
            options = []
            while len(options) < 3:
                part = random.randint(0,1)
                if part == 0:
                    chosen = random.choice(["Reptile", "Canine", "Hooved", "Avian", "Insect"])
                    if chosen not in options:
                        options.append(chosen)
                        print("Head: "+chosen)
                else:
                    siglopts = []
                    val = random.randint(0,7)
                    if val > 5:
                        val = 5
                    for m in range(val+1):
                        for k in sigilSort[m]:
                            siglopts.append(k)
                    chosen = random.choice(siglopts)
                    if chosen not in options:
                        options.append(chosen)
                        print("Sigil: "+chosen)
            print(f"The options were offered to {player1.name} only.")
            if len(player1.totparts) == 8:
                print("But you could carry no more.")
                print("As recompense, the Woodcarver gives you an Amalgam.")
                player1.cards.append(amalg)
            else:
                while True:
                    n1 = False
                    p1choice = input()
                    if p1choice == "1" or p1choice == "2" or p1choice == "3":
                        print("You have chosen "+options[int(p1choice)-1])
                        print("It was added.")
                        player1.totparts.append(options[int(p1choice)-1])
                        options.pop(int(p1choice)-1)
                        break
                    else:
                        for n in options:
                            if p1choice.lower() == n.lower():
                                n1 = True
                                break
                    if n1 == True:
                        print("You have chosen "+n)
                        print("It was added.")
                        player1.totparts.append(n)
                        options.remove(n)
                        break
                    print("Try again.")
            print("")
            print("Here are your current totem parts:")
            totheads = 0
            totsigils = 0
            for n in player1.totparts:
                if n in ["Reptile", "Canine", "Hooved", "Avian", "Insect"]:
                    print("Head: "+n)
                    totheads+=1
                else:
                    print("Sigil: "+n)
                    totsigils+=1
            if totheads > 0 and totsigils > 0:
                tpartl = []
                for n in player1.totparts:
                    tpartl.append(n.lower())
                print("")
                print("You may now build your totem.")
                print("First, pick which tribe you prefer.")
                while True:
                    p1choiceh = input()
                    if p1choiceh.lower() in tpartl and p1choiceh.lower() in ["reptile", "canine", "hooved", "avian", "insect"]:
                        break
                    else:
                        print("Invalid input.")
                print("Next, pick which sigil you prefer.")
                while True:
                    p1choices = input()
                    if p1choices.lower() in tpartl and p1choices.lower() in sigilListLow:
                        break
                    else:
                        print("Invalid input.")
                print("Your totem is now gives all your "+p1choiceh+" creatures the "+p1choices+" sigil.")
                player1.totem = [p1choiceh,p1choices]
        elif space == "Mycologist":
            print("We are the Mycologists, yes?")
            print("Y-You have... two of the same creature, yes?")
            print("(One for each of us.)")
            mycopts = []
            mycopts2 = []
            for n in range(len(player1.cards)):
                for m in range(len(player1.cards)):
                    if n < m:
                        n1 = player1.cards[n]
                        m1 = player1.cards[m]
                        if n1.name == m1.name and n1.deckspot not in mycopts2 and m1.deckspot not in mycopts2 and n1.name != "Ijiraq":
                            mycopts.append([n1,m1])
                            mycopts2.append(n1.deckspot)
                            mycopts2.append(m1.deckspot)
            if len(mycopts) > 0:
                mycopts2 = []
                for n in mycopts:
                    printcards(n)
                    mycopts2.append(n[0])
                print("(Pick a pair.)")
                mycin = pickcards(mycopts2)
                print("T-This could get messy...")
                print("(Avert your eyes.)")
                n = mycopts[mycin][0]
                m = mycopts[mycin][1]
                sigil1myc = []
                sigil2myc = []
                for a in n.sigils+m.sigils:
                    if a not in sigil1myc:
                        if len(sigil1myc) >= 2:
                            sigil2myc.append(a)
                        else:
                            sigil1myc.append(a)
                for b in n.sigils2+m.sigils2:
                    if b not in sygil1myc and b not in sigil2myc:
                        sigil2myc.append(b)
                if n.trait[0:2] == "pel":
                    if n.name[-4:-1] == "Pel":
                        # Keeps track of how many times the pelt has been fused
                        n.trait = n.trait[0:3]+str(int(n.trait[-1])+1)
                mycCard = Card(n.name, n.power+m.power, n.health+m.health, n.cost, n.tribe, sigil1myc, sigil2myc, n.trait)
                player1.cards.pop(n.deckspot)
                player1.cards.pop(m.deckspot)
                player1.cards.append(mycCard)
                printcards([mycCard])
                print("W-What have we done...?")
                print("(The experiment was complete.)")
            else:
                print("... N-No duplicates?")
                print("(... Take one of ours.)")
                mycCard = random.sample(player1.cards,3)
                for n in range(3):
                    while mycCard[n].name == "Ouroboros":
                        mycCard[n] = random.choice(player1.cards)
                duplic = pickcard(mycCard)
                player1.cards.append(mycCard[duplic])
        elif space == "Bone":
            print("The Bone Lord awaits a sacrifice.")
            print("You are able to tell that the fate of this creature... will not be pleasant.")
            print(f"{player1.name} has been chosen to select a creature.")
            p1cards = []
            for n in player1.cards:
                p1cards.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.sigils2, n.trait))
            for n in range(len(p1cards)):
                if p1cards[n].trait == "ijiraq":
                    disg = random.choice(p1cards)
                    while disg.trait == "ijiraq":
                        disg = random.choice(p1cards)
                    disg.trait = "ijiraq"
                    disg.name = disg.name+"?"
                    p1cards[n] = disg
            sacrifice = pickcard(p1cards)
            sacrifice = p1cards[sacrifice]
            if sacrifice.trait == "goat":
                print("The Bone Lord is greatly pleased with your sacrifice.")
                print("You have received Boon of the Bone Lord.")
                print("You will recieve eight extra bones at the start of each battle.")
                player1.boneStart += 8
            elif sacrifice.trait == "pelt":
                print("Your sacrifice displeases the Bone Lord.")
                print("You will receive nothing in return.")
            else:
                print("Your sacrifice is acceptable.")
                print("You have received Minor Boon of the Bone Lord.")
                print("You will receive one extra bone at the start of each battle.")
                player1.boneStart += 1
            player1.cards.pop(sacrifice.deckspot)
        elif space == "Sigil swap":
            print("You approach a mysterious shrine in the wilderness.")
            print(f"Only {player1.name} is brave enough to step forward.")
            p1opts1 = [n for n in player1.cards if len(n.sigils) > 0 and len(n.sigils2) == 0]
            print("First, you may select which creature shall provide the sigils.")
            opt1ch = p1opts1[pickcard(p1opts1)]
            p1cards = []
            for n in player1.cards:
                p1cards.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.sigils2, n.trait))
            p1opts2 = []
            for n in range(len(p1cards)):
                if p1cards[n].trait == "ijiraq":
                    disg = random.choice(p1cards)
                    while disg.trait == "ijiraq":
                        disg = random.choice(p1cards)
                    disg.trait = "ijiraq"
                    disg.name = disg.name+"?"
                    p1cards[n] = disg
                if len(p1cards[n].sigils2) == 0 and p1cards[n].deckspot != opt1ch.deckspot:
                    z = 0
                    for m in p1cards[n].sigils:
                        if m in opt1ch.sigils:
                            z = 1
                    if z == 0:
                        p1opts2.append(p1cards[n])
            print("Now, you may select which creature the sigils will be transferred to.")
            opt2ch = p1opts2[pickcard(p1opts2)]
            player1.cards[opt2ch.deckspot].sigils2 = opt1ch.sigils
            if len(opt1ch.sigils) == 1:
                print("The "+opt1ch.sigils[0]+" sigil was added to your "+opt2ch.name+".")
            else:
                print("The"+" and ".join(opt1ch.sigils)+" sigils were added to your "+opt2ch.name+".")
            player1.cards.pop(opt1ch.deckspot)
            print("Your "+opt2ch.name+" was consumed.")
        elif space == "Item":
            if len(player1.items) == 3:
                print("... Your bag was full.")
                print("A small creature approached.")
                player1.cards.append(rat)
                print(f"{player1.name} gained a Pack Rat.")
            while len(player1.items) < 3:
                ichoices = random.sample(itemList2, 3)
                print("The options are presented to you.")
                print(f"{player1.name} may choose.")
                print(", ".join(ichoices))
                ichoicel = []
                for n in ichoices:
                    ichoicel.append(n.lower())
                    print(itemDispl[itemList.index(n)])
                while True:
                    print("Number or name will do.")
                    decid = input()
                    if decid == "1" or decid == "2" or decid == "3":
                        decid = int(decid)-1
                        player1.items.append(ichoices[decid])
                        print("Gained the "+ichoices[decid]+".")
                        break
                    elif decid.lower() in ichoicel:
                        decid = decid.lower()
                        newit = ichoices[ichoicel.index(decid)]
                        player1.items.append(newit)
                        print("Gained the "+newit+".")
                        break
                    elif decid[0] == "?":
                        while True:
                            print("What would you like to know about?")
                            for n in ichoices:
                                print(itemDispl[itemList.index(n)])
                            print("You may print X to cancel.")
                            d2 = input()
                            if d2.lower()[0] == "x":
                                break
                            elif d2.lower() in sigilListLow:
                                d2 = d2.lower()
                                print(itemDispl[sigilListLow.index(d2)])
                                print(itemDesc[sigilListLow.index(d2)])
                            else:
                                print("Invalid Input")
                    else:
                        print("Invalid input.")
        elif space == "Campfire":
            # Which type of fire is it?
            if random.randint(0,1) == 0:
                fired = "power"
            else:
                fired = "health"
            # Will the second try work?
            if random.randint(0,1) == 0:
                try2 = True 
            else:
                try2 = False
            if survDead == False:
                # Random intro message
                if random.randint(0,1) == 0:
                    print('The crackling fire lit the starving face of a group of survivors. "We have not food..." one said. "But perhaps... one of your creatures will join us? Enhance its '+fired+'?" said another.')
                else:
                    print('"Warm a creature by fire? Enhance its '+fired+'?" said a hungry survivor.')
            else:
                print("... A lonely campfire sits in the forest.")
                print("Whatever group once sat around the fire... is long gone now.")
                print("Nevertheless, the fire's warmth may assist you.")
                print("It may improve a creature's "+fired+"... if you have the heart to try.")
            # P1 goes
            print(f"{player1.name} steps forward.")
            p1cards = []
            for n in player1.cards:
                p1cards.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.sigils2, n.trait))
            for n in range(len(p1cards)):
                if p1cards[n].trait == "ijiraq":
                    disg = random.choice(p1cards)
                    while disg.trait == "ijiraq":
                        disg = random.choice(p1cards)
                    disg.trait = "ijiraq"
                    disg.name = disg.name+"?"
                    p1cards[n] = disg
            choice = pickcard(p1cards)
            print("You have chosen your "+p1cards[choice].name+".")
            if fired == "power":
                print("Its power has been increased by one.")
                player1.cards[p1cards[choice].deckspot].power+=1
            else:
                print("Its health has been increased by two.")
                player1.cards[p1cards[choice].deckspot].health+=2
            if survDead == False:
                # Second try?
                print("You may now choose to risk spending another moment by the fire... (Y/N)")
                while True:
                    decide = input()
                    if decide.lower()[0] == "y" or decide.lower()[0] == "n":
                        break
                    else:
                        print("Please give a valid option.")
            else:
                decide = "y"
            if decide.lower() == "y":
                if try2 == False and survDead == False:
                    print("The survivors descended upon the creature, devouring it in seconds.")
                    if player1.cards[choice].trait == "kills survivors" or "Touch of Death" in player1.cards[choice].sigils+player1.cards[choice].sigils2:
                        survDead = True
                    player1.cards.pop(p1cards[choice].deckspot)
                else:
                    if fired == "power":
                        player1.cards[p1cards[choice].deckspot].power+=1
                        print("Its power has once again been increased by one.")
                    else:
                        player1.cards[p1cards[choice].deckspot].health+=2
                        print("Its health has once again been increased by two.")
            else:
                print("You suspected the intentions of the survivors were less than pure. With your creature in tow, you retreated into the woods.")
        else:
            print("Space currently under construction. Please wait for an update.")
        mapc.pop(0)
        print("\n")
print("Game over.")
