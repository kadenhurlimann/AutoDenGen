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
        self.height=0
        self.width=0

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

    def printField(self):
        for x in range(self.height):
                print(self.field[x])

def main():
    level = Gen()
    level.generateField(10,5)
    level.printField()
    #print(level.field)
    print(level.width)
    print(level.height)
    print(len(level.field[0]))
    print(len(level.field))

if __name__ == '__main__':
    main()
