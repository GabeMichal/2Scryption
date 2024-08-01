import random
from Scrypt_card import *

# Separate turns from another
def breakline():
    for n in range(40):
        print("\n")

# Attack function
def attack(doer, target, n, attacker, m): # doer = attacker.board[m], n = space being attacked, m = space of the card attacking
    try:
        doer.tempPow = int(doer.power)
    except ValueError:
        doer.tempPow = 0
    if target.board[n] == 0:
        for k in range(len(target.board)):
            if target.board[k] != 0:
                # Confusing variables... k1 is the actual card, k is the spot the card is in
                k1 = target.board[k]
                if "Burrower" in k1.sigils+k1.sigils2:
                    if (("Airborne" not in doer.sigils+doer.sigils2 and attacker.harpyActive == False) or "Mighty Leap" in k1.sigils+k1.sigils2):
                        if "Waterborne" not in k1.sigils+k1.sigils2:
                            target.board[n] = k1
                            target.board[k] = 0
                            break
    # Power-changing sigils
    if target.board[m] != 0:
        if "Stinky" in target.board[m].sigils+target.board[m].sigils2 and "Made of Stone" not in doer.sigils+doer.sigils2:
            doer.tempPow -= 1
    if m < 3:
        if attacker.board[m+1] != 0:
            if "Leader" in attacker.board[m+1].sigils+attacker.board[m+1].sigils2:
                doer.tempPow+=1
    if attacker.board[m-1] != 0 and m > 0:
        if "Leader" in attacker.board[m-1].sigils+attacker.board[m-1].sigils2:
            doer.tempPow+=1
    # If there's a card there, attack the card
    if target.board[n] != 0:
        if doer.tempPow >= 0:
            if "Loose Tail" in target.board[n].sigils+target.board[n].sigils2:
                if n != 3:
                    if target.board[n+1] != 0:
                        if "Loose Tail" in target.board[n].sigils:
                            target.board[n].sigils.remove("Loose Tail")
                        else:
                            target.board[n].sigils2.remove("Loose Tail")
                        target.board[n+1] = target.board[n]
                        target.board[n] = create_card("Tail")
                    else:
                        if n != 0:
                            if target.board[n-1] != 0:
                                if "Loose Tail" in target.board[n].sigils:
                                    target.board[n].sigils.remove("Loose Tail")
                                else:
                                    target.board[n].sigils2.remove("Loose Tail")
                                target.board[n-1] = target.board[n]
                                target.board[n] = create_card("Tail")
                else:
                    if target.board[n-1] != 0:
                        if "Loose Tail" in target.board[n].sigils:
                            target.board[n].sigils.remove("Loose Tail")
                        else:
                            target.board[n].sigils2.remove("Loose Tail")
                        target.board[n-1] = target.board[n]
                        target.board[n] = create_card("Tail")
            if (("Airborne" in doer.sigils+doer.sigils2 or attacker.harpyActive == True) and "Mighty Leap" not in target.board[n].sigils+target.board[n].sigils) or "Waterborne" in target.board[n].sigils+target.board[n].sigils2:
                target.receive_damage(doer.power)
            elif "Repulsive" not in target.board[n].sigils+target.board[n].sigils2:
                # Card gets attacked
                if "Bees Within" in target.board[n].sigils or "Bees Within" in target.board[n].sigils2:
                    target.hand.append(bee)
                if "Sharp Quills" in target.board[n].sigils+target.board[n].sigils2:
                    attacker.board[m].health -= 1
                    if attacker.board[m].health <= 0:
                        # Attacking card dies
                        if "Unkillable" in attacker.board[m].sigils+attacker.board[m].sigils2:
                            attacker.hand.append(attacker.board[m])
                            if attacker.board[m].trait == "ouroboros":
                                attacker.hand[-1].power+=1
                                attacker.hand[-1].health+=1
                                attacker.cards[attacker.hand[-1].deckspot].power+=1
                                attacker.cards[attacker.hand[-1].deckspot].health+=1
                        if "Bone King" in attacker.board[m].sigils+attacker.board[m].sigils2:
                            attacker.bones+=3
                        attacker.bones+=1
                        if attacker.board[m].name == "Strange Frog":
                            attacker.board[m] = create_card("Leaping Trap")
                        else:
                            attacker.board[m] = 0
                if "chime" == target.board[n].trait:
                    for chimchek in range(4):
                        if target.board[chimchek].trait == "chimer":
                            attack(target.board[chimchek], attacker, m, target, chimchek)
                if "Touch of Death" in doer.sigils+doer.sigils2 and "Made of Stone" not in target.board[n].sigils+target.board[n].sigils2:
                    target.board[n].health = 0
                if "Armored" in doer.sigils:
                    attacker.board[m].sigils.remove("Armored")
                elif "Armored" in doer.sigils2:
                    attacker.board[m].sigils2.remove("Armored")
                else:
                    target.board[n].health -= doer.power
                if target.board[n].health <= 0:
                    # Card dies
                    if "Unkillable" in target.board[n].sigils+target.board[n].sigils2:
                        target.hand.append(target.board[n])
                        if target.board[n].trait == "ouroboros":
                            target.hand[-1].power+=1
                            target.hand[-1].health+=1
                            target.cards[target.hand[-1].deckspot].power+=1
                            target.cards[target.hand[-1].deckspot].health+=1
                    if "Bone King" in target.board[n].sigils+target.board[n].sigils2:
                        target.bones+=3
                    if "Steel Trap" in target.board[n].sigils+target.board[n].sigils2:
                        if attacker.board[n] != 0:
                            # Card in front dies
                            attacker.hand.append(create_card("Wolf Pelt"))
                            if "Unkillable" in attacker.board[n].sigils+attacker.board[n].sigils2:
                                attacker.hand.append(attacker.board[n])
                                if attacker.board[n].trait == "ouroboros":
                                    attacker.hand[-1].power+=1
                                    attacker.hand[-1].health+=1
                                    attacker.cards[attacker.hand[-1].deckspot].power+=1
                                    attacker.cards[attacker.hand[-1].deckspot].health+=1
                            if "Bone King" in attacker.board[n].sigils+attacker.board[n].sigils2:
                                attacker.bones+=3
                            attacker.bones+=1
                            if attacker.board[n].name == "Strange Frog":
                                attacker.board[n] = create_card("Leaping Trap")
                            else:
                                attacker.board[n] = 0
                    if "Frozen Away" in target.board[n].sigils+target.board[n].sigils2:
                        target.board[n] = create_card("Opossum")
                    elif target.board[n].name == "Strange Frog":
                        target.board[n] = create_card("Leaping Trap")
                    else:
                        target.board[n] = 0
                    target.bones += 1
                    # Corpse Eater check
                    for corp in target.hand:
                        if "Corpse Eater" in corp.sigils:
                            target.board[n] = corp
                            target.hand.remove(corp)
                    if "Blood Lust" in doer.sigils+doer.sigils2:
                        attacker.board[n].power += 1
                        if doer.trait == "hodag":
                            attacker.cards[attacker.board[m].deckspot].power+=1
    else:
        # Otherwise, just attack the guy
        target.receive_damage(doer.power)

# Fledgling Function
def growup(player, slot):
    growing = player.board[slot]
    if "Fledgling" in growing.sigils:
        growing.sigils.remove("Fledgling")
    else:
        growing.sigils2.remove("Fledgling")
    if growing.name == "Wolf Cub":
        player.board[slot] = create_card("Wolf")
        player.board[slot].power = growing.power+2
        player.board[slot].health = growing.health+1
    elif growing.name == "Elk Fawn":
        player.board[slot] = create_card("Elk")
        player.board[slot].power = growing.power+1
        player.board[slot].health = growing.health+3
    elif growing.name == "Raven Egg":
        player.board[slot] = create_card("Raven")
        player.board[slot].power = growing.power+2
        player.board[slot].health = growing.health+1
    elif growing.name == "Strange Larva":
        player.board[slot] = create_card("Strange Pupa")
        player.board[slot].power = growing.power
        player.board[slot].health = growing.health
    elif growing.name == "Strange Pupa":
        player.board[slot] = create_card("Mothman")
        player.board[slot].power = growing.power+7
        player.board[slot].health = growing.health
    elif growing.name == "Dire Wolf Pup":
        growing.sigils.remove("Bone Digger")
        player.board[slot] = create_card("Dire Wolf")
        player.board[slot].power = growing.power+1
        player.board[slot].health = growing.health+4
    elif growing.name == "Tadpole":
        growing.sigils.remove("Waterborne")
        player.board[slot] = create_card("Bullfrog")
        player.board[slot].power = growing.power+1
        player.board[slot].health = growing.health+1
    elif growing.name == "Flying Ant" or growing.name == "Worker Ant":
        if growing.name == "Flying Ant":
            growing.sigils.remove("Airborne")
        player.board[slot] = create_card("Ant Queen")
        player.board[slot].power = growing.power
        player.board[slot].health = growing.health+2
    elif growing.name == "Elk":
        if "Sprinter" in growing.sigils:
            growing.sigils.remove("Sprinter")
        else:
            growing.sigils.remove("SprinterL")
        player.board[slot] = create_card("Moose Buck")
        player.board[slot].power = growing.power+1
        player.board[slot].health = growing.health+3
    elif growing.name == "Mole":
        player.board[slot] = create_card("Mole Man")
        player.board[slot].power = growing.power
        player.board[slot].health = growing.health+2
    elif growing.name == "Mantis":
        growing.sigils.remove("Bifurcated Strike")
        player.board[slot] = create_card("Mantis God")
        player.board[slot].power = growing.power
        player.board[slot].health = growing.health
    else:
        try:
            player.board[slot].power += 1
        except ValueError:
            player.board[slot].tempPow += 1
        player.board[slot].health += 2
        # Any name changes
        z = player.board[slot].name
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
        player.board[slot].name = z
    player.board[slot].sigils+=growing.sigils
    player.board[slot].sigils+=growing.sigils2
    # Get rid of sigil duplicates
    player.board[slot].sigils = list(set(player.board[slot].sigils))
    player.board[slot].sigils2 = list(set(player.board[slot].sigils2))
    for n in player.board[slot].sigils:
        if n in player.board[slot].sigils2:
            player.board[slot].sigils2.remove(n)

# Battling function
def battle(style, player1, player2):
    # Amount of rounds in the battle
    if style[:3] == "BOSS":
        phaseNum = 2
    elif style == "Battle":
        phaseNum = 1
    else:
        phaseNum = 3
    
    # Catch up changes to deck
    player1.deck = []
    player2.deck = []
    for n in player1.cards:
        player1.deck.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.sigils2, n.trait))
    for n in player2.cards:
        player1.deck.append(Card(n.name, n.power, n.health, n.cost, n.tribe, n.sigils, n.sigils2, n.trait))
    
    # Trapper check
    if style == "BOSS - Trapper":
        for n in range(len(player1.deck)/2):
            player1.deck.append(create_card("Strange Frog"))
        for n in range(len(player2.deck)/2):
            player2.deck.append(create_card("Strange Frog"))
    random.shuffle(player1.deck)
    random.shuffle(player2.deck)
    
    # Deal starting hands
    player1.draw_card(player1.squirrels)
    player2.draw_card(player2.squirrels)
    for _ in range(3):
        player1.draw_card(player1.deck)
        player2.draw_card(player2.deck)

    # Starting bones
    player1.bones = player1.boneStart
    player2.bones = player2.boneStart

    # Check to see if starvation takes over
    p1out = False
    p2out = False
    
    # Main game loop
    playernum = 0
    players = [player1, player2]
    firstTurn = True
    for phase in range(phaseNum):
        while True:
            if p1out == True and p2out == True and phaseNum == 1:
                print("... That is enough stalling. This battle ends now.")
                if player1.damage > player2.damage:
                    return 10
                elif player2.damage > player1.damage:
                    return 20
                else:
                    return 0
            breakline()
            current_player = players[playernum]
            print(f"{current_player.name}'s Turn")
            print(current_player)
            print(players[1-playernum])
            # Check for any Fledglings still alive
            for m in range(len(current_player.board)):
                if current_player.board[m] != 0:
                    if "Fledgling" in current_player.board[m].sigils+current_player.board[m].sigils2:
                        growup(current_player, m)

            if firstTurn == False:
                while True:
                    if len(current_player.squirrels) == 0 and len(current_player.deck) == 0:
                        print("You have run out of both cards in your deck and squirrels.")
                        print("... I will have to end the game if this continues like this. Consider this a warning.")
                        if current_player == player1:
                            p1out = True
                        else:
                            p2out = True
                        break
                    print("You may now draw from either your deck or a guaranteed squirrel.")
                    draw = input()
                    if draw.lower() == "deck":
                        if len(current_player.deck) > 0:
                            # Draw a card from deck
                            print(f"{current_player.name} draws a card.")
                            current_player.draw_card(current_player.deck)
                            break
                        else:
                            print("Your deck is empty.")
                    elif draw.lower() == "squirrel":
                        if len(current_player.squirrels) > 0:
                            # Draw a squirrel
                            current_player.draw_card(current_player.squirrels)
                            print(f"{current_player.name} draws a squirrel.")
                            break
                        else:
                            print("Your side deck is empty.")
                    elif draw.lower() == "check":
                        print("Your hand:")
                        printcards(current_player.hand)
                        print("")
                        print("Current Board:")
                        print_board(players[1-playernum], current_player)
                        print('')
                    else:
                        print("Please input a proper command.")

            print(f"{current_player.name}'s hand:")
            printcards(current_player.hand)

            print("\n")
            
            #Print the board state
            print("Current Board:")
            print_board(players[1-playernum], current_player)
            
            # Do stuff
            while True:
                act = input("What will you do (Play, Item, Bell, or Check)? ")
                if act.lower() == "play":
                    playing = pickcard(current_player.hand)
                    if playing <= len(current_player.hand)-1:
                        card_to_play = current_player.hand[playing]
                        current_player.play_card(card_to_play, current_player)
                    else:
                        print("You can't play this card for some reason... probably a bug.")
                elif act.lower() == "bell":
                    print("Turn end!")
                    print("\n")
                    break
                elif act.lower() == "check":
                    print("Your hand:")
                    printcards(current_player.hand)
                    print("")
                    print("Current Board:")
                    print_board(players[1-playernum], current_player)
                elif act.lower() == "item":
                    itmtemp = []
                    for n in current_player.items:
                        itmtemp.append(n.lower())
                        print(n)
                    while True:
                        print("Which item will you use?")
                        itmuse = input().lower()
                        if itmuse in itmtemp:
                            break
                        else:
                            print("You do not have that item.")
                    itmuse = current_player.items[itmtemp.index(itmuse)]
                    used = current_player.item_use(itmuse, players[1-players.index(current_player)])
                    if used == 1:
                        current_player.items.remove(itmuse)
                else:
                    print("Not an option. Try again.")
            
            # End the turn after each players goes
            current_player.end_turn(players[1-playernum])
            
            # Switch to the other player
            playernum = 1-playernum

            firstTurn = False

            if abs(player1.damage-player2.damage) >= 5:
                if phaseNum-1 == phase:
                    # Determine the winner; if one person has 5 more damage than another, but only on the last round
                    if player1.damage-player2.damage >= 5:
                        player1.teeth += player1.damage-player2.damage-5
                        print(f"{player1.name} is the winner.")
                        return player1
                    elif player2.damage-player1.damage >= 5:
                        player2.teeth += player2.damage-player1.damage-5
                        print(f"{player2.name} is the winner.")
                        return player2
                else:
                    if style[7:] == "Prospector":
                        print("Thar's gold in them cards!")
                        if player1.damage-player2.damage >= 5:
                            for n in range(4):
                                if player1.board[n] != 0:
                                    # Kill card, create gold nugget
                                    if "Bone King" in player1.board[n].sigils+player1.board[n].sigils2:
                                        player1.bones+=3
                                    if "Unkillable" in player1.board[n].sigils+player1.board[n].sigils2:
                                        player1.hand.append(player1.board[n])
                                        if player1.board[n].trait == "ouroboros":
                                            player1.hand[-1].power+=1
                                            player1.hand[-1].health+=1
                                            player1.cards[player1.hand[-1].deckspot].power+=1
                                            player1.cards[player1.hand[-1].deckspot].health+=1
                                    player1.board[n] = create_card("Gold Nugget")
                                    player1.bones+=1
                            print(f"{player1.name}'s cards have been turned to gold.")
                        else:
                            for n in range(4):
                                if player2.board[n] != 0:
                                    # Kill card, create gold nugget
                                    if "Bone King" in player2.board[n].sigils+player2.board[n].sigils2:
                                        player2.bones+=3
                                    if "Unkillable" in player2.board[n].sigils+player2.board[n].sigils2:
                                        player2.hand.append(player2.board[n])
                                        if player2.board[n].trait == "ouroboros":
                                            player2.hand[-1].power+=1
                                            player2.hand[-1].health+=1
                                            player2.cards[player2.hand[-1].deckspot].power+=1
                                            player2.cards[player2.hand[-1].deckspot].health+=1
                                    player2.board[n] = create_card("Gold Nugget")
                                    player2.bones+=1
                            print(f"{player2.name}'s cards have been turned to gold.")
                    elif style[7:] == "Angler":
                        if player1.damage-player2.damage >= 5:
                            for n in range(4):
                                if player1.board[n] == 0 and player2.board[n] != 0:
                                    # Place bait buckets to block
                                    player1.board[n] = create_card("Bait Bucket")
                        else:
                            for n in range(4):
                                if player1.board[n] != 0 and player2.board[n] == 0:
                                    # Place bait buckets to block
                                    player2.board[n] = create_card("Bait Bucket")
                        print("Go fish.")
                    elif style[7:] == "Trapper":
                        if player1.damage-player2.damage >= 5:
                            # Create random cards in player2's board/hand
                            handcards2 = get_cardlist(common, 4)
                            for n in range(4):
                                handcards2[n].sigils2 = [random.choice(sigilList2)]
                            boardnum2 = player2.board.count(0)
                            boardcards2 = get_cardlist(common, boardnum2)
                            for n in range(boardnum2):
                                boardcards2[n].sigils2 = [random.choice(sigilList2)]
                            # Offer to trade
                            print("You wish to trade?")
                            player1.hand.append(create_card("Rabbit Pelt"))
                            while True:
                                peltcount = 0
                                for n in player1.hand:
                                    if n.trait[0:-1] == "pelt":
                                        peltcount+=1
                                if peltcount == 0:
                                    break
                                else:
                                    chosen = pickcard(handcards2+boardcards2)
                                    if chosen > 3:
                                        # Get a card from the opponent's board
                                        player1.hand.append(boardcards2[chosen-4])
                                        boardcards2.pop(chosen-4)
                                    else:
                                        # Get a card from the opponent's hand
                                        player1.hand.append(handcards2[chosen])
                                        handcards2.pop(chosen)
                                    # Use a pelt
                                    for n in range(len(player1.hand)):
                                        if player1.hand[n].trait[0:-1] == "pelt":
                                            player1.hand.pop(n)
                            for n in handcards2:
                                player2.hand.append(n)
                            for n in boardcards2:
                                for m in range(4):
                                    if player2.board[m] == 0:
                                        player2.board[m] = n
                        else:
                            # Create random cards in player1's board/hand
                            handcards1 = get_cardlist(common, 4)
                            for n in range(4):
                                handcards1[n].sigils2 = [random.choice(sigilList2)]
                            boardnum1 = player1.board.count(0)
                            boardcards1 = get_cardlist(common, boardnum1)
                            for n in range(boardnum1):
                                boardcards1[n].sigils2 = [random.choice(sigilList2)]
                            # Offer to trade
                            print("You wish to trade?")
                            player2.hand.append(create_card("Rabbit Pelt"))
                            while True:
                                peltcount = 0
                                for n in player2.hand:
                                    if n.trait[0:-1] == "pelt":
                                        peltcount+=1
                                if peltcount == 0:
                                    break
                                else:
                                    chosen = pickcard(handcards1+boardcards1)
                                    if chosen > 3:
                                        player2.hand.append(boardcards1[chosen-4])
                                        boardcards1.pop(chosen-4)
                                    else:
                                        player2.hand.append(handcards1[chosen])
                                        handcards1.pop(chosen)
                                    # Use a pelt
                                    for n in range(len(player2.hand)):
                                        if player2.hand[n].trait[0:-1] == "pelt":
                                            player2.hand.pop(n)
                            for n in handcards1:
                                player1.hand.append(n)
                            for n in boardcards1:
                                for m in range(4):
                                    if player1.board[m] == 0:
                                        player1.board[m] = n
                    elif style == "Final Boss":
                        a = 1
                        # Make sure to have 3 phases idk what would be here but ye
