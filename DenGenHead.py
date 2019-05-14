import os
from os import system, name
from random import seed
from random import randint
# seed random number generator
# generate some random numbers
#print(randint(0,10), randint(0,10),randint(0,10))
#system('pip install pyenchant'

class Gen():


    def __init__(self):
        self.field = [[]]
        self.height=5
        self.width=5

        #accepts height and width of board,
        #creates randomly generated 2 dimensional list of tuples of 4 ints at passed in values as field
        #returns true always
    def generateField(self, height, width):
        for x in range(height):
            for y in range(width):
                #if len(self.field)>=width and len(self.field[0])>=height:
                    #self.height = width
                    #self.width = height
                    #return True
                self.field[x].append((randint(0,100),randint(0,100),randint(0,100),randint(0,100)))
            if height > len(self.field):
                self.field.append([])
        self.height = height
        self.width = width
        return True

    def getTup(self, height, width, index=4):
        if index == 4:
            return self.field[width][height]
        else:
            print(index)
            return self.field[width][height][index]

    def printField(self):
        for x in range(self.height):
                print(self.field[x])
        print(self.width)
        print(self.height)

def main():
    level = Gen()
    print("input width")
    width = int(7)
    print("input height")
    height = int(5)  #height = int(input())
    level.generateField(height,width)
    level.printField()
    print("height")
    height = int(input())-1
    print("width")
    width = int(input())-1
    print("index")
    index = int(input())-1

    print(level.getTup(height, width, index))

if __name__ == '__main__':
    main()
