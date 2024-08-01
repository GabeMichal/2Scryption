import random
import pygame
import os

transitions = [["1_1", "1_2","1_3"],
               ["2_1","1n1_1n1(straight)","1n1_1n1(gay)","1n1_1n1(lesbian)","1n1_1n2","1n1_2n1","2_3"],
               ["3_1","1n2_1n1","2n1_1n1","3_2"]]

startspace = [1,1,1,2,2,2,2,2,2,2,3,3,3]

allMaps = []

spaces1 = {"Battle": ["Normal"],
          "New Card": ["Card Choice", "Cost Choice", "Tribe Choice", "Trapper", "Prospector", "Trial"],
          "Support": ["Woodcarver", "Sigil swap", "Item", "Campfire"]}
spaces = {"Battle": ["Normal"],
          "New Card": ["Card Choice", "Cost Choice", "Tribe Choice", "Trapper", "Trader", "Trial"],
          "Support": ["Woodcarver", "Mycologist", "Bone", "Sigil swap", "Item", "Campfire", "Copy Card"]}

class mapSeg:
    def __init__(self, paths):
        self.seg1, self.seg2 = paths.split("_")
        self.ver = ""
        if "straight" in self.seg2:
            self.ver = "straight"
        elif "gay" in self.seg2:
            self.ver = "gay"
        elif "lesbian" in self.seg2:
            self.ver = "lesbian"
        if self.ver != "":
            self.seg2 = self.seg2[0:3]
        self.trees = []
        self.getTrees()

    def getTrees(self):
        if self.seg1 == "1":
            if self.seg2 == "1":
                self.trees.append("x<230")
                self.trees.append("x>250")
            elif self.seg2 == "2":
                self.trees.append("2*(y+300)/3+10<abs(x-240)")
                self.trees.append("2*(y+240)/3+30>abs(x-240)")
            elif self.seg2 == "3":
                self.trees.append("-4*(y+240)/3+170<x<230")
                self.trees.append("250<x<4*(y+240)/3+310")
                self.trees.append("x<-4*(y+300)/3+230")
                self.trees.append("x>4*(y+300)/3+250")
        elif self.seg1 == "1n1":
            if self.seg2 == "1n1":
                self.trees.append("x<190")
                self.trees.append("x>290")
                if self.ver == "straight":
                    self.trees.append("210<x<270")
                elif self.ver == "lesbian":
                    self.trees.append("210<x<270-4*(y+300)/3")
                    self.trees.append("210-4*(y+240)/3<x<270")
                elif self.ver == "gay":
                    self.trees.append("210<x<4*(y+240)/3+270")
                    self.trees.append("4*(y+300)/3+210<x<270")
            elif "2" in self.seg2:
                self.trees.append("-2*(y+300)/3+190>x")
                self.trees.append("x>2*(y+300)/3+290")
                if self.seg2 == "1n2":
                    self.trees.append("-2*(y+300)/3+210<x<-2*(y+300)/3+270")
                    self.trees.append("2*(y+240)/3+30>abs(x-280)")
                else:
                    self.trees.append("2*(y+300)/3+270>x>2*(y+300)/3+210")
                    self.trees.append("2*(y+240)/3+30>abs(x-200)")
        elif self.seg1 == "1n2":
            self.trees.append("2*(y+300)/3+150>x")
            self.trees.append("2*(y+300)/3+230>x>2*(y+300)/3+170")
            self.trees.append("-2*(y+300)/3+30>abs(x-280)")
            self.trees.append("-2*(y+300)/3+330<x")
        elif self.seg1 == "2":
            self.trees.append("-2*(y+300)/3+30>abs(x-240)")
            if self.seg2 == "1":
                self.trees.append("2*(y+300)/3+190>x")
                self.trees.append("-2*(y+300)/3+290<x")
            elif self.seg2 == "3":
                self.trees.append("-2*(y+240)/3+150>x")
                self.trees.append("x>2*(y+240)/3+330")
                self.trees.append("2*(y+240)/3+30>abs(x-200)")
                self.trees.append("2*(y+240)/3+30>abs(x-280)")
        elif self.seg1 == "2n1":
            self.trees.append("2*(y+300)/3+150>x")
            self.trees.append("-2*(y+240)/3+210<x<-2*(y+240)/3+270")
            self.trees.append("-2*(y+300)/3+30>abs(x-200)")
            self.trees.append("-2*(y+300)/3+330<x")
        elif self.seg1 == "3":
            if self.seg2 == "1":
                self.trees.append("4*(y+300)/3+170<x<230")
                self.trees.append("250<x<-4*(y+300)/3+310")
                self.trees.append("x>-4*(y+300)/3+330")
                self.trees.append("x<4*(y+300)/3+150")
            elif self.seg2 == "2":
                self.trees.append("-2*(y+300)/3+30>abs(x-200)")
                self.trees.append("-2*(y+300)/3+30>abs(x-280)")
                self.trees.append("2*(y+300)/3+150>x")
                self.trees.append("-2*(y+240)/3+290<x")
                self.trees.append("2*(y+240)/3+30>abs(x-240)")

    def getColl(self, x, y):
        # Test if a certain coordinate would be in the trees
        if y > 300 or y < 240:
            return True
        for k in self.trees:
            if eval(k, {"x": x, "y": -y}):
                return True

class Map:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        if number == 4:
            self.trans = ["1_4","4_1"]
            self.spots = [["Start"], random.sample(["totem", "bone", "stones", "item", "fire", "trader"],4), ["LeshyBoss"]]
        else:
            possibleSpots = {"Battle": ["battle", "battleswap"],
                             "New Card": ["choose", "costch", "tribch", "trapper",  "trial"],
                             "Support": ["totem", "stones", "item", "fire"]}
            if number > 1:
                possibleSpots["New Card"].append("trader")
                possibleSpots["Support"].append("myco")
                possibleSpots["Support"].append("goob")
                possibleSpots["Support"].append("bone")
            prospOpt = True
            for n in allMaps:
                if n.name == "Woodlands" and n.number != self.number:
                    prospOpt = False
            if prospOpt == True:
                possibleSpots["New Card"].append("rocky")
            self.trans = []
            self.spots = []
            for n in range(4):
                if n == 0:
                    spaceNum = 1
                    self.spots.append(["start"])
                    self.trans.append("1_1")
                    if number == 1:
                        self.spots.append(["trader"])
                    else:
                        self.spots.append([random.choice(possibleSpots["New Card"])])
                for m in range(3):
                    if n == 0 and m == 0:
                        continue
                    self.trans.append(random.choice(transitions[spaceNum-1]))
                    trans2 = transitions[spaceNum-1].index(self.trans[-1])
                    # Make sure that battle events have few enough spaces
                    while m == 2 and ((spaceNum == 1 and trans2 == 2) or (spaceNum == 2 and trans2 > 2)):
                        self.trans.pop(-1)
                        self.trans.append(random.choice(transitions[spaceNum-1]))
                        trans2 = transitions[spaceNum-1].index(self.trans[-1])
                    if spaceNum == 1:
                        newSpaces = trans2+1
                    elif spaceNum == 2:
                        if trans2 == 0:
                            newSpaces = 1
                        else:
                            newSpaces = int((trans2-1)/3)+2
                    else:
                        if trans2 == 0:
                            newSpaces = 1
                        else:
                            newSpaces = 2
                    if m == 0 and n != 0:
                        library = "New Card"
                    elif m == 1 or (m == 2 and n == 3):
                        library = "Support"
                    else:
                        library = "Battle"
                    if m != 0 or n != 0:
                        self.spots.append(random.sample(possibleSpots[library],newSpaces))
                        spaceNum = newSpaces
            if spaceNum == 1:
                self.trans.append("1_1")
            else:
                self.trans.append(transitions[spaceNum-1][0])
            if name == "Woodlands":
                self.spots.append(["GrimoraBoss"])
            elif name == "Wetlands":
                self.spots.append(["PO3Boss"])
            elif name == "Snow Line":
                self.spots.append(["MagnificusBoss"])
        self.segs = [mapSeg(n) for n in self.trans]

mapOpts = ["Woodlands","Wetlands","Snow Line"]
map1 = random.choice(mapOpts)
mapOpts.remove(map1)
map2 = random.choice(mapOpts)
mapOpts.remove(map2)
map3 = mapOpts[0]
allMaps.append(Map(map1,1))
allMaps.append(Map(map2,2))
allMaps.append(Map(map3,3))
allMaps.append(Map("Final",4))




# We have 3 times that we go New Card, Support, Battle
# The fourth time, it's New Card, Support, Support, Boss
# Pick a transition each time, and add as many spaces are necessary
            
