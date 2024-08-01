import pygame
import os

dimension = 2

# List of all sigils
sigilList = ["Rabbit Hole", "Bees Within", "Sprinter", "SprinterL", "Touch of Death", "Fledgling", "Dam Builder", "Hoarder", "Burrower", "Fecundity", "Loose Tail",
          "Corpse Eater", "Bone King", "Waterborne", "Unkillable", "Sharp Quills", "Hefty", "HeftyL", "Ant Spawner", "Guardian", "Airborne", "Many Lives", "Repulsive",
          "Worthy Sacrifice", "Mighty Leap", "Bifurcated Strike", "Trifurcated Strike", "Frozen Away", "Trinket Bearer", "Steel Trap", "Amorphous",
          "Leader", "Bellist", "Stinky", "Brood Parasite", "Rampager", "RampagerL", "Made of Stone", "Double Strike", "Blood Lust",
          "Morsel", "Armored", "Bone Digger", "Scavenger", "Finical Hatchling"]

# Lowercase version
sigilListLow = [n.lower() for n in sigilList]

# Sigils you can get from events (Deck trial, Prospector, etc)
sigilList2 = ["Rabbit Hole", "Bees Within", "Sprinter", "Touch of Death", "Fledgling", "Dam Builder", "Hoarder", "Burrower", "Fecundity", "Loose Tail",
              "Corpse Eater", "Bone King", "Waterborne", "Unkillable", "Sharp Quills", "Hefty", "Ant Spawner", "Guardian", "Airborne", "Many Lives",
              "Worthy Sacrifice", "Mighty Leap", "Bifurcated Strike", "Trifurcated Strike", "Trinket Bearer", "Amorphous",
              "Leader", "Bellist", "Stinky", "Brood Parasite", "Rampager", "Made of Stone", "Double Strike", "Blood Lust",
              "Morsel", "Armored", "Bone Digger", "Scavenger"]

# Sorted sigils for use in woodcarver event
sigilSort = [["Airborne"],
             ["Sprinter", "Burrower", "Waterborne", "Guardian", "Hefty", "Mighty Leap", "Rampager"],
             ["Fledgling", "Loose Tail", "Bone King", "Unkillable", "Sharp Quills", "Worthy Sacrifice", "Stinky", "Made of Stone", "Bone Digger", "Scavenger"],
             ["Rabbit Hole", "Bees Within", "Dam Builder", "Fecundity", "Corpse Eater", "Ant Spawner", "Amorphous", "Leader", "Blood Lust", "Morsel"], 
             ["Touch of Death", "Hoarder", "Many Lives", "Bifurcated Strike", "Bellist", "Brood Parasite", "Double Strike", "Armored"] ,
             ["Trifurcated Strike", "Trinket Bearer"]]

sigilListDesc = ["Rabbit Hole", "Bees Within", "Sprinter", "Touch of Death", "Fledgling", "Dam Builder", "Hoarder", "Burrower", "Fecundity", "Loose Tail",
          "Corpse Eater", "Bone King", "Waterborne", "Unkillable", "Sharp Quills", "Hefty", "Ant Spawner", "Guardian", "Airborne", "Many Lives", "Repulsive",
          "Worthy Sacrifice", "Mighty Leap", "Bifurcated Strike", "Trifurcated Strike", "Frozen Away", "Trinket Bearer", "Steel Trap", "Amorphous",
          "Leader", "Bellist", "Stinky", "Brood Parasite", "Rampager", "Made of Stone", "Double Strike", "Blood Lust",
          "Morsel", "Armored", "Bone Digger", "Scavenger", "Finical Hatchling"]

sigilDesc = [["When a card bearing this sigil is played, a Rabbit is created in your hand."],
             ["Once a card bearing this sigil is struck, a Bee is created in its owner's hand. A Bee is defined as: 1 Power, 1 Health, Airborne."],
             ["At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed on the sigil."],
             ["When a card bearing this sigil damages another creature, that creature perishes."],
             ["A card bearing this sigil will grow into a more powerful form after 1 turn on the board."],
             ["When a card bearing this sigil is played, a Dam is created on each empty adjacent space. A Dam is defined as: 0 Power, 2 Health."],
             ["When a card bearing this sigil is played, its player may search their deck for any card and take it into their hand."],
             ["When an empty space would be struck, a card bearing this sigil will move to that space to receive the strike instead."],
             ["When a card bearing this sigil is played, a copy of it is created in its player's hand."],
             ["When a card bearing this sigil would be struck, a Tail is created in its place and a card bearing this sigil moves to the right."],
             ["If a creature that you own perishes by combat, a card bearing this sigil in your hand is automatically played in its place."],
             ["When a card bearing this sigil dies, 4 Bones are awarded instead of 1."],
             ["A card bearing this sigil submerges itself during its opponent's turn. While submerged, opposing creatures attack its owner directly."],
             ["When a card bearing this sigil perishes, a copy of it is created in its owner's hand."],
             ["Once a card bearing this sigil is struck, the striker is then dealt a single damage point."],
             ["At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed in the sigil, pushing other creatures in the same direction."],
             ["When a card bearing this sigil is played, an ant is created in its player's hand."],
             ["When an opposing creature is placed opposite to an empty space, a card bearing this sigil will move to that empty space."],
             ["A card bearing this sigil will strike an opponent directly, even if there is a creature opposing it."],
             ["When a card bearing this sigil is sacrificed, it does not perish."],
             ["If a creature would attack a card bearing this sigil, it does not."],
             ["Cards bearing this sigil count as 3 Blood rather than 1 Blood when sacrificed."],
             ["A card bearing this sigil will block an opposing creature bearing the Airborne sigil."],
             ["A card bearing this sigil will strike each opposing space to the left and right of the space across from it."],
             ["A card bearing this sigil will strike each opposing space to the left and right of the spaces across from it as well as the space in front of it."],
             ["When a card bearing this sigil perishes, the creature inside is released in its place."],
             ["When a card bearing this sigil is played, its player will receive a random item as long as they have less than 3 items."],
             ["When a card bearing this sigil perishes, the creature opposing it perishes as well. A Pelt is created in the attacker's hand."],
             ["When a card bearing this sigil is drawn, this sigil is replaced with another sigil at random."],
             ["Creatures adjacent to a card bearing this sigil gain 1 Power."],
             ["When a card bearing this sigil is played, a Chime is created on each empty adjacent space. Chimes have 0 Power and 1 Health."],
             ["The creature opposing a card bearing this sigil loses 1 Power."],
             ["When a card bearing this Sigil is played, an Egg is created on the opposing space."],
             ["At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed on the sigil, throwing other creatures behind it."],
             ["A card bearing this sigil is immune to the effects of Touch of Death and Stinky."],
             ["A card bearing this sigil will strike the opposing space an extra time when attacking."],
             ["When a card bearing this Sigil attacks an opposing creature and it perishes, this card gains 1 power."],
             ["When a card bearing this Sigil is sacrificed, it adds its stat values to the card it was sacrificed for."],
             ["The first time a card bearing this sigil would take damage, prevent that damage."],
             ["At the end of the owner's turn, a card bearing this sigil will generate 1 Bone."],
             ["While a card bearing this sigil is alive on the board, opposing creatures also grant Bones upon death."],
             ["A card bearing this sigil hatches when drawn if the owner's deck has creatures with Health and Power values from 1 to 5 and a creature from each tribe."]]

pygame.font.init()
for k in range(len(sigilDesc)):
    newList = sigilDesc[k][0].split()
    font = pygame.font.Font("Scrypt_Font.ttf", 10)
    i = 0
    while i+1 < len(newList):
        if font.render(newList[i]+" "+newList[i+1], 0, (0,0,0)).get_width() > 165:
            i += 1
        else:
            newList[i] += " "+newList[i+1]
            newList.pop(i+1)
    sigilDesc[k] = newList


# List of sigil's sprites
sigilSprite = []
sigilSpriteB = []
sigilSpriteO = []
for n in sigilList:
    try:
        sigilSprite.append(pygame.image.load(os.path.join("Scryption_Display", "InSigils", "_".join(n.split())+".png")))
        sigilSpriteB.append(pygame.image.load(os.path.join("Scryption_Display", "InSigilBlue", "_".join(n.split())+".png")))
        sigilSpriteO.append(pygame.image.load(os.path.join("Scryption_Display", "InSigilOrange", "_".join(n.split())+".png")))
    except FileNotFoundError:
        print(n+" not found")


# Items and their descriptions
itemList = ["Boulder in a Bottle", "Squirrel in a Bottle", "Special Dagger", "Scissors", "Pliers", "Hoggy Bank", "Hourglass", "Black Goat in a Bottle",
            "Frozen Opossum in a Bottle", "Fish Hook", "Harpies Birdleg Fan", "Wiseclock", "Magickal Bleach", "Magpies Lens", "Skinning Knife"]
# Lowercase version
itemListLow = [n.lower() for n in itemList]
# Items you can find on the path
itemList2 = ["Boulder in a Bottle", "Squirrel in a Bottle", "Scissors", "Pliers", "Hoggy Bank", "Hourglass", "Black Goat in a Bottle",
            "Frozen Opossum in a Bottle", "Harpies Birdleg Fan", "Wiseclock", "Magickal Bleach", "Magpies Lens"]

itemsDesc = ["A boulder is created in your hand. A boulder is defined as: 0 Power, 5 Health.",
             "A squirrel is created in your hand. A squirrel is defined as: 0 Power, 1 Health.",
             "You will place a weight on the scales. The pain is temporary.",
             "You may cut up one of your opponent's cards. It is destroyed.",
             "You will place a weight on the scales. The pain is temporary.",
             "You will immediately gain 4 Bones.",
             "Your opponent will entirely skip their next turn.",
             "A black goat is created in your hand. A black goat is defined as: 0 Power, 1 Health, Worthy Sacrifice.",
             "A frozen opossum is created in your hand. A frozen opossum is defined as: 0 Power, 5 Health, Frozen Away.",
             "Hook one of your advesary's cards and take it as your own. You must have an empty space on your side to receive it.",
             "Your creatures will attack as though they have the Airborne Sigil this turn.",
             "All creatures on the board will rotate one space clockwise.",
             "All your opponent's cards on the board will lose their sigils.",
             "You will search your deck for any card and take it into your hand.",
             "You may skin one of your opponent's cards. It is destroyed and you draw a pelt card."]

for k in range(len(itemsDesc)):
    newList = itemsDesc[k].split()
    font = pygame.font.Font("Scrypt_Font.ttf", 10)
    i = 0
    while i+1 < len(newList):
        if font.render(newList[i]+" "+newList[i+1], 0, (0,0,0)).get_width() > 165:
            i += 1
        else:
            newList[i] += " "+newList[i+1]
            newList.pop(i+1)
    itemsDesc[k] = newList
pygame.font.quit()

# List of item's sprites
itemSprite = []
for n in itemList:
    try:
        itemSprite.append(pygame.image.load(os.path.join("Scryption_Display", "InItems", "_".join(n.split())+".png")))
    except FileNotFoundError:
        print(n+" not found")

rulebook = sigilDesc+itemsDesc