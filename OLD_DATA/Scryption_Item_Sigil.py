import pygame

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

sigilDesc = ["When a card bearing this sigil is played, a Rabbit is created in your hand.",
             "Once a card bearing this sigil is struck, a Bee is created in your hand. A Bee is defined as: 1 Power, 1 Health, Airborne.",
             "At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed in the sigil.",
             "At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed in the sigil.",
             "When a card bearing this sigil damages another creature, that creature perishes.",
             "A card bearing this sigil will grow into a more powerful form after 1 turn on the board.",
             "When a card bearing this sigil is played, a Dam is created on each empty adjacent space. A Dam is defined as: 0 Power, 2 Health.",
             "When a card bearing this sigil is played, you may search your deck for any card and take it into your hand.",
             "When an empty space would be struck, a card bearing this sigil will move to that space to receive the strike instead.",
             "When a card bearing this sigil is played, a copy of it is created in your hand.",
             "When a card bearing this sigil would be struck, a Tail is created in its place and a card bearing this sigil moves to the right.",
             "If a creature that you own perishes by combat, a card bearing this sigil in your hand is automatically played in its place.",
             "When a card bearing this sigil dies, 4 Bones are awarded instead of 1.",
             "A card bearing this sigil submerges itself during its opponent's turn. While submerged, opposing creatures attack its owner directly.",
             "When a card bearing this sigil perishes, a copy of it is created in your hand.",
             "Once a card bearing this sigil is struck, the striker is then dealt a single damage point.",
             "At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed in the sigil. Creatures that are in the way will be pushed in the same direction.",
             "When a card bearing this sigil is played, an ant is created in your hand.",
             "When an opposing creature is placed opposite to an empty space, a card bearing this sigil will move to that empty space.",
             "A card bearing this sigil will strike an opponent directly, even if there is a creature opposing it.",
             "When a card bearing this sigil is sacrificed, it does not perish.",
             "If a creature would attack a card bearing this sigil, it does not.",
             "Cards bearing this sigil count as 3 Blood rather than 1 Blood when sacrificed.",
             "A card bearing this sigil will block an opposing creature bearing the Airborne sigil.",
             "A card bearing this sigil will strike each opposing space to the left and right of the space across from it.",
             "A card bearing this sigil will strike each opposing space to the left and right of the spaces across from it as well as the space in front of it.",
             "When a card bearing this sigil perishes, the creature inside is released in its place.",
             "When a card bearing this sigil is played, you will receive a random item as long as you have less than 3 items.",
             "When a card bearing this sigil perishes, the creature opposing it perishes as well. A Pelt is created in your hand.",
             "When a card bearing this sigil is drawn, this sigil is replaced with another sigil at random.",
             "Creatures adjacent to a card bearing this sigil gain 1 Power.",
             "When a card bearing this sigil is played, a Chime is created on each empty adjacent space. Chimes have 0 Power and 1 Health.",
             "The creature opposing a card bearing this sigil loses 1 Power.",
             "When a card bearing this Sigil is played, an Egg is created on the opposing space.",
             "At the end of the owner's turn, a card bearing this sigil will move in the direction inscribed on the sigil. Creatures in the way will be thrown back behind it.",
             "A card bearing this sigil is immune to the effects of Touch of Death and Stinky.",
             "A card bearing this sigil will strike the opposing space an extra time when attacking.",
             "When a card bearing this Sigil attacks an opposing creature and it perishes, this card gains 1 power.",
             "When a card bearing this Sigil is sacrificed, ⁣it adds its stat values to the card it was sacrificed for.",
             "The first time a card bearing this sigil would take damage, prevent that damage.",
             "At the end of the owner's turn, a card bearing this sigil will generate 1 Bone.",
             "While a card bearing this sigil is alive on the board, opposing creatures also grant Bones upon death.",
             "A card bearing this Sigil hatches when drawn if the numbers 1 to 5 are represented in the Health of creatures in your deck, and in their Power, and if there is a creature of each tribe in your deck."]


Sigils = [
"""
  \/  
  ()  
______ (Rabbit Hole)
""",
"""
  /\  
  --. 
_____. (Bees Within)
""",
"""
  |   
  |-> 
______ (Sprinter)
""",
"""
  |   
<-|   
______ (Sprinter)
""",
"""
   0  
   X  
______ (Touch of Death)
""",
"""
 1|\  
 (__) 
______ (Fledgling)
""",
"""
 __--|
|DM|D|
|__|-_ (Dam Builder)
""",
"""
 /--\ 
 \__/ 
_/____ (Hoarder)
""",
"""
  _O_ 
 <| |>
___A_/ (Burrower)
""",
"""
 __--|
|FD|F|
|__|-_ (Fecundity)
""",
"""
 /--> 
|\\___A
_\___/ (Loose Tail)
""",
"""
  /-C 
  \\0  
______ (Corpse Eater)
""",
"""
 /3 /3
 /3 /3
______ (Bone King)
""",
"""
 A_A  
 \  \ 
wwwwww (Waterborne)
""",
"""
  /0\ 
  \</ 
______ (Unkillable)
""",
"""
   |  
 \/ \/
_|_1_| (Sharp Quills)
""",
"""
 ()   
 |==W 
______ (Hefty)
""",
"""
   () 
 W==| 
______ (Hefty)
""",
"""
  \/  
  /\  
__/\__ (Ant Spawner)
""",
"""
 /,,\ 
 vVVv 
__^-/_ (Guardian)
""",
"""
 \__  
 \  \ 
_\_@/_ (Airborne)
""",
"""
   T  
  (X) 
___V__ (Many Lives)
""",
"""
  __  
 /\ \ 
_\_\/_ (Repulsive)
""",
"""
  B   
   B  
____B_ (Worty Sacrifice)
""",
"""
 \__ _
 \@/V/
___\/_ (Mighty Leap)
""",
"""
 A  A 
  \/  
__/\__ (Bifurcated Strike)
""",
"""
 A AA 
  \/  
__/\__ (Trifurcated Strike)
""",
"""
/===/|
|   ||
|___|/ (Frozen Away)
""",
"""
 /––\ 
 |\/| 
_\__/_ (Trinket Bearer)
""",
"""
  AA  
 A--A 
_\AA/_ (Steel Trap)
""",
"""
 /-\\  
   /  
__o___ (Amorphous)
""",
"""
   1  
 <-P->
______ (Leader)
""",
"""
 __--|
|BL|B|
|__|-_ (Bellist)
""",
"""
   S  
 S__S 
_/__\_ (Stinky)
""",
"""
  __  
 |ww| 
_\__/_ (Brood Parasite)
""",
"""
 <-\\  
 || \\ 
_\_=V_ (Rampager)
""",
"""
  /-> 
 / || 
_V=_/_ (Rampager)
""",
"""
  /--|
 |   |
_o---n (Made of Stone)
""",
"""
  AA  
  ||  
__/\__ (Double Strike)
""",
"""
 ____ 
 VvvV 
_\__/_ (Blood Lust)
""",
"""
  \\n  
 /  \ 
_\__/_ (Morsel)
""",
"""
 A__A 
 |1 | 
__\/__ (Armored)
""",
"""
  |   
 |\/| 
__\/__ (Bone Digger)
""",
"""
 /--\ 
 \^^/ 
_E==3_ (Scavenger)
""",
"""
  __  
 |V | 
_\__/_ (Finicial Hatchling)
"""
    ]

Sigils2 = [
"""
\/ 
()  (Rabbit Hole)
""",
"""
/\ 
--. (Bees Within)
""",
"""
|  
|-> (Sprinter)
""",
"""
  |
<-| (Sprinter)
""",
"""
 0 
 X  (Touch of Death)
""",
"""
1A 
(_) (Fledgling)
""",
"""
D_ 
||| (Dam Builder)
""",
"""
(O)
/   (Hoarder)
""",
"""
 O 
<=> (Burrower)
""",
"""
F_ 
||| (Fecundity)
""",
"""
/> 
\_A (Loose Tail)
""",
"""
/-C
\\0 (Corpse Eater)
""",
"""
/33
/33 (Bone King)
""",
"""
\ \\
www (Waterborne)
""",
"""
/0\\
\</ (Unkillable)
""",
"""
 | 
\\1/ (Sharp Quills)
""",
"""
() 
|=W (Hefty)
""",
"""
 ()
W=| (Hefty)
""",
"""
 \/
 /\\ (Ant Spawner)
""",
"""
vWv
^-/ (Guardian)
""",
"""
\__
\@/ (Airborne)
""",
"""
 T 
(V) (Many Lives)
""",
"""
/\\\\
\_/ (Repulsive)
""",
"""
B  
 BB (Worty Sacrifice)
""",
"""
\^\\
\@) (Mighty Leap)
""",
"""
A A
\ / (Bifurcated Strike)
""",
"""
AAA
\|/ (Trifurcated Strike)
""",
"""
/-|
|_/
(Frozen Away)
""",
"""
/–\\
|V|
___ (Trinket Bearer)
""",
"""
 A 
A+A (Steel Trap)
""",
"""
   
 ?  (Amorphous)
""",
"""
 1 
<P> (Leader)
""",
"""
B_ 
||| (Bellist)
""",
"""
SSS
/-\ (Stinky)
""",
"""
/=\\
\_/ (Brood Parasite)
""",
"""
<-\\
\=W (Rampager)
""",
"""
/->
W=/ (Rampager)
""",
"""
/-|
o-n (Made of Stone)
""",
"""
 AA
 || (Double Strike)
""",
"""
VwV
\_/ (Blood Lust)
""",
"""
/'\\
\_/ (Morsel)
""",
"""
A_A
\\1/ (Armored)
""",
"""
_|_
\V/ (Bone Digger)
""",
"""
/…\\
E=3 (Scavenger)
""",
"""
/V\\
\_/  (Finicial Hatchling)
"""
    ]

# Items and their descriptions
itemList = ["Boulder in a Bottle", "Squirrel in a Bottle", "Special Dagger", "Scissors", "Pliers", "Hoggy Bank", "Hourglass", "Failure", "Black Goat in a Bottle",
            "Frozen Opossum in a Bottle", "Fish Hook", "Harpie's Birdleg Fan", "Wiseclock", "Magickal Bleach", "Magpie's Lens", "Skinning Knife"]
# Lowercase version
itemListLow = [n.lower() for n in itemList]
# Items you can find on the path
itemList2 = ["Boulder in a Bottle", "Squirrel in a Bottle", "Scissors", "Pliers", "Hoggy Bank", "Hourglass", "Black Goat in a Bottle",
            "Frozen Opossum in a Bottle", "Harpie's Birdleg Fan", "Wiseclock", "Magickal Bleach", "Magpie's Lens"]

itemsDesc = ["A boulder is created in your hand. A boulder is defined as: 0 Power, 5 Health.",
             "A squirrel is created in your hand. A squirrel is defined as: 0 Power, 1 Health.",
             "You will place a weight on the scales. The pain is temporary.",
             "You may cut up one of your adversary's cards. It is destroyed.",
             "You will place a weight on the scales. The pain is temporary.",
             "You will immediately gain 4 Bones.",
             "Your adversary will entirely skip their next turn.",
             "Nothing will happen. This bottle of goo has no use.",
             "A black goat is created in your hand. A black goat is defined as: 0 Power, 1 Health, Worthy Sacrifice.",
             "A frozen opossum is created in your hand. A frozen opossum is defined as: 0 Power, 5 Health, Frozen Away.",
             "Hook one of your advesary's cards and take it as your own. You must have an empty space on your side to receive it.",
             "Your creatures will attack as though they have the Airborne Sigil this turn.",
             "All creatures on the board will rotate one space clockwise.",
             "All your opponent's cards on the board will lose their sigils.",
             "You will search your deck for any card and take it into your hand.",
             "You may skin one of your adversary's cards. It is destroyed and you draw a pelt card."]
# Item images
itemDispl = [
"""
/-T-\\
|/-||
|o_n| (Boulder in a Bottle)
""",
"""
/-T-\\
| ^^|
|(__| (Squirrel in a Bottle)
""",
"""
  A  
 -†- 
__V__ (Special Dagger)
""",
"""
 O O 
  X  
_/_\_ (Scissors)
""",
"""
 ( ) 
  X  
_/ \_ (Pliers)
""",
"""
 (_  
 / ^.
_|_B| (Hoggy Bank)
""",
"""
|(-)|
| X |
|(_)| (Hourglass)
""",
"""
/-T-\\
|, '|
|_/\| (Failure)
""",
"""
/-T-\\
|= =|
|_V_| (Black Goat in a Bottle)
""",
"""
/-T-\\
|/-||
||_/| (Frozen Opossum in a Bottle)
""",
"""
   o 
   | 
_^_/_ (Fish Hook)
""",
"""
\\\\V//
 \V/ 
__V__ (Harpie's Birdleg Fan)
""",
"""
 --- 
((o))
_---_ (Wiseclock)
""",
"""
_/'\_
|   |
\___/ (Magickal Bleach)
""",
"""
 /A\\ 
 \V/ 
__|__ (Magpie's Lens)
""",
"""
 /-\\ 
 | | 
__V__ (Skinning Knife)
"""
]
