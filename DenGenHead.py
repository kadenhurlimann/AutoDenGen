import os
from os import system, name
from random import seed
from random import randint
# seed random number generator
# generate some random numbers
#print(randint(0,10), randint(0,10),randint(0,10))
#system('pip install pyenchant')

class Gen():


    def __init__(self):
        self.field = [[]]
        self.height=0
        self.width=0

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
                self.field[x].append((randint(0,1),randint(0,1),randint(0,1),randint(0,1)))
            if height > len(self.field):
                self.field.append([])
        self.height = height
        self.width = width
        return True

    def getTup(self, height, width, index=5):
        if index == 5:
            return self.field[height][width]
        else:
            return self.field[height][width][index]

    def printField(self):
        for x in range(self.height):
                print(self.field[x])
        print(self.width)
        print(self.height)

def main():
    level = Gen()
    print("input width")
    width = int(input())
    print("input height")
    height = int(input())
    level.generateField(height,width)
    level.printField()

    height = int(input())
    width = int(input())
    index = int(input())

    print(level.getTup(height, width, index))

if __name__ == '__main__':
    main()
