import os
from os import system, name
from random import seed
from random import randint
import pygame

# seed random number generator
# generate some random numbers
#print(randint(0,10), randint(0,10),randint(0,10))
#system('pip install pyenchant'

class Gen():


    def __init__(self):
        self.field = [[]]
        self.obX = 1
        self.obY = 1
        self.height=7
        self.width=7
        self.grid = ["<^v>00v"]

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

    def movOb(self, dir):
        if dir == 'w':
            if self.field[self.obY][self.obX][0] == 1:
                self.obX = self.obX-1
                return True

            else:
                return False

        elif dir == 'n':
            if self.field[self.obY][self.obX][1] == 1:
                self.obY = self.obY-1
                return True
            else:
                return False

        elif dir == 'e':
            if self.field[self.obY][self.obX][2] == 1:
                self.obX = self.obX+1
                return True

            else:
                return False

        elif dir == 's':
            if self.field[self.obY][self.obX][3] == 1:
                self.obY = self.obY+1
                return True

            else:
                return False

        else:
            return False


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


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)




    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [255, 255]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()




    level = Gen()
    print("input width")
    width = int(7)
    print("input height")
    height = int(7)  #height = int(input())
    level.generateField(height,width)
    level.printField()
    direction = 'n'
    # while direction != 'k':
    #     screen.fill(BLACK)
    #
    #     # Draw the grid
    #     for column in range(level.height):
    #         for row in range(level.width):
    #             color = WHIT
    #             if grid[row][column] == 1:
    #                 color = GREEN
    #             pygame.draw.rect(screen,
    #                              color,
    #                              [(MARGIN + WIDTH) * column + MARGIN,
    #                               (MARGIN + HEIGHT) * row + MARGIN,
    #                               WIDTH,
    #                               HEIGHT])
    #
    #     # Limit to 60 frames per second
    #     clock.tick(60)
    #
    #     # Go ahead and update the screen with what we've drawn.
    #     pygame.display.flip()



    print(level.getTup(level.obX, level.obY, 4))
    print(level.obX,level.obY)
    print("direction")
    direction = input()
    print(level.movOb(direction))
    print("height")
    height = int(input())-1
    print("width")
    width = int(input())-1
    print("index")
    index = int(input())-1

    print(level.getTup(height, width, index))

if __name__ == '__main__':
    main()
