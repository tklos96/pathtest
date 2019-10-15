#!/usr/bin/env python
import numpy as np
import random

class Game():
    def __init__(self,filename):
        pathArray =  np.loadtxt(filename,skiprows=1,delimiter=',',dtype=str)
        self.turnmod = pathArray[:,0].astype(int)
        self.spacemod = pathArray[:,1].astype(int)
        self.description = pathArray[:,2]
        self.spaces = len(self.turnmod)
        self.landed = np.zeros(self.spaces)
        self.ended = np.zeros(self.spaces)

        self.turn = 0
        self.pos = -1
        self.won = False

        #Note: 0 = first space on board
        #      self.spaces = You Win (not in pathArray)


    def advanceTurn(self):
        self.turn += 1
        roll = random.randint(1,7)
        newPos = self.pos + roll
        if(newPos>=self.spaces):
            if (newPos == self.spaces):
                self.won = True
            return
        else:
            self.landed[newPos] += 1

        self.turn += self.turnmod[newPos]
        self.pos = newPos + self.spacemod[newPos]

        if(self.pos>=self.spaces):
            self.won = True
        else:
            self.ended[self.pos] += 1

        return
     
    def newGame(self):
        self.turn = 0
        self.pos = -1
        self.won = False
        self.landed = np.zeros(self.spaces)
        self.ended = np.zeros(self.spaces)
        return
