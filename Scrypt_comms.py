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

def tailRun(p, m):
    tail = p.board[m].create_card("Tail")
    if p.board[m].name == "Skink":
        p.board[m].portrait = "Skink_notail"
    if m < 3 and p.board[m+1] == 0:
        p.board[m+1] = p.board[m]
        p.board[m] = tail
    elif m > 0 and p.board[m-1] == 0:
        p.board[m-1] = p.board[m]
        p.board[m] = tail

def attack(p1, p2, n, m, damage):
    # p1.board[n] = attacker, attacking space m
    if p2.board[m] == 0:
        for k in range(4):
            if p2.board[k] != 0 and p2.board[k].checkSigil("Burrower") and not passCheck(p1, p2, n, k):
                p2.board[m] = p2.board[k]
                p2.board[k] = 0
                break
    if passCheck(p1, p2, n, m):
        p1.damage += damage
    elif not p2.board[m].checkSigil("Repulsive"):
        if p2.board[m].checkSigil("Loose Tail"):
            tailRun(p2, m)
        if "Armored" in p2.board[m].sigils:
            p2.board[m].sigils.remove("Armored")
        elif "Armored" in p2.board[m].sigils2:
            p2.board[m].sigils.remove("Armored")
        elif "Armored" == p2.board[m].sigilTem:
            p2.board[m].sigilTem = ""
        else:
            p2.board[m].health -= damage
        if p2.board[m].checkSigil("Bees Within"):
            p2.deck.append(p2.board[m].create_card("Bee"))
            p2.draw_card(p2.deck, -1)
        if p1.board[n].checkSigil("Touch of Death") and not p2.board[m].checkSigil("Made of Stone"):
            p2.board[m].health = 0
        if p2.board[m].checkSigil("Sharp Quills") and p1.board[n].health > 0:
            attack(p2,p1,m,n,1)
        if p2.board[m].trait == "chime":
            for k in range(4):
                if p2.board[k] != 0 and p2.board[k].trait == "chimer":
                    attack(p2,p1,k,n,p2.board[k].power+p2.board[k].powChange)
        if p2.board[m].health <= 0:
            # Card dies
            if p2.board[m].checkSigil("Bone King"):
                p2.bones += 3
            if p2.board[m].checkSigil("Unkillable"):
                if p2.board[m].trait == "ouroboros":
                    p2.board[m].power += 1
                    p2.board[m].health += 1
                    if isinstance(p2.board[m].deckspot,int):
                        p2.cards[p2.board[m].deckspot].power += 1
                        p2.cards[p2.board[m].deckspot].health += 1
                p2.board[m].cost = p2.board[m].create_card(p2.board[m].name).cost
                p2.board[m].selected = False
                p2.board[m].marked = False
                p2.deck.append(p2.board[m])
                p2.draw_card(p2.deck, -1)
            if p2.board[m].checkSigil("Steel Trap"):
                if p1.board[3-m] != 0:
                    p1.board[3-m].create_card("Wolf Pelt")
                    p1.board[3-m] = 0
            if p2.board[m].checkSigil("Frozen Away"):
                p2.board[m] = p2.board[m].create_card("Opossum")
            else:
                p2.board[m] = 0
            p2.bones += 1
            for k in range(4):
                if p1.board[k] != 0 and p1.board[k].checkSigil("Scavenger"):
                    p1.bones += 1
                    break
            for k in range(len(p2.hand)):
                if p2.hand[k].checkSigil("Corpse Eater"):
                    p2.play_card(k, m)
                    break
            if p1.board[n].checkSigil("Blood Lust"):
                p1.board[n].power += 1
                if p1.board[n].trait == "hodag":
                    p1.cards[p1.board[n].deckspot].power += 1


def get_comms(p1, p2):
    for n in range(4):
        for i in p2.comms["attack"][n]:
            # Opponent attacks card in space m from space n with an attack of i[1]
            m = 3 - i[0]
            if passCheck(p2, p1, n, m):
                for k in range(4):
                    if p1.board[m] == 0 and not passCheck(p2, p1, n, k) and p1.board[k].checkSigil("Burrower"):
                        # Card burrows from space k to space m
                        p1.board[m] = p1.board[k]
                        p1.board[k] = 0
                        break
            if not p1.board[m].checkSigil("Repulsive"):
                if p1.board[m].checkSigil("Loose Tail"):
                    tailRun(p1, m)
                if not p1.board[m].checkSigil("Armored"):
                    p1.board[m].health -= i[1]
                elif "Armored" in p1.board[m].sigils:
                    p1.board[m].sigils.remove("Armored")
                elif "Armored" in p1.board[m].sigils2:
                    p1.board[m].sigils2.remove("Armored")
                if p1.board[m].checkSigil("Bees Within"):
                    p1.hand.append(p1.board[m].create_card("Bee"))
                if p2.board[n].checkSigil("Touch of Death"):
                    p1.board[m].health = 0
                if p1.board[m].checkSigil("Sharp Quills"):
                    p1.comms["attack"][m].append([n, 1])
                if p1.board[m].health <= 0:
                    # Card dies
                    if p1.board[m].checkSigil("Bone King"):
                        p1.bones += 3
                    if p1.board[m].checkSigil("Unkillable"):
                        if p1.board[m].trait == "ouroboros":
                            p1.board[m].power += 1
                            p1.board[m].health += 1
                            p1.cards[p1.board[m].deckspot].power += 1
                            p1.cards[p1.board[m].deckspot].health += 1
                        p1.hand.append(p1.board[m])
                    p1.board[m] = 0
                    p1.bones += 1
                    p1.comms["death"] += 1
        p2.comms["attack"][n] = []
    if p2.comms["death"] > 0:
        for i in p1.board:
            if i != 0 and i.checkSigil("Scavenger"):
                p1.bones += p2.comms["death"]
                break
        p2.comms["death"] = 0
    if not isinstance(p2.comms["egged"][0], str):
        p1.board[p2.comms["egged"][1]] = p2.comms["egged"][0]
        p2.comms["egged"] = ["",0]
    if p2.comms["playPlace"] >= 0 and p1.board[p2.comms["playPlace"]] == 0:
        for i in range(4):
            if p1.board[i] != 0 and p1.board[i].checkSigil("Guardian"):
                p1.board[p2.comms["playPlace"]] = p1.board[i]
                p1.board[i] = 0
        p2.comms["playPlace"] = -1
    if p2.comms["bleached"]:
        for i in range(4):
            p1.board[i].sigils = []
            p1.board[i].sigils2 = []
        p2.comms["bleached"] = False
    if p2.comms["bell"]:
        p1.myTurn = True
        p1.drawn = False
        p2.comms["bell"] = False
