import numpy as np
from random import randint
gridTable = np.array([[]])
w = 0
h = 0

def initGrid(width, height, cellwid):
    rows, cols = (int(height/cellwid), int(width/cellwid))
    global w
    global h
    w = cols
    h = rows
    arr = [[0 for i in range(cols)] for j in range(rows)]
    global gridTable
    gridTable = np.array(arr)

def clear():
    for y in range(h):
        for x in range(w):
            gridTable[y, x] = 0

def clickGrid(x, y): # counting like pygame
    if(x == w):
        x = w-1
    if(y == h):
        y = h-1
    if(gridTable[y, x]):
        gridTable[y, x] = 0
    else:
        gridTable[y, x] = 1

def glider(x, y):

    if(x > w-3 or y > h-3):
        #too dangerous to put a glider on the edge
        return

    clickGrid(x, y)
    clickGrid(x+1, y)
    clickGrid(x+2, y)
    clickGrid(x+2, y+1)
    clickGrid(x+1, y+2)


def countNeighbors(x, y):
    count = 0
    checkX = x - 1
    checkY = y - 1
    for i in range(3):
        checkX = x - 1
        for j in range(3):
            if(checkX < 0):
                checkX = w + checkX
            if(checkX >= w):
                checkX = checkX-w
            if(checkY < 0):
                checkY = h + checkY
            if(checkY >= h):
                checkY = checkY -h
            if(y == checkY and checkX == x):
                checkX += 1
                continue #don't count self.
            if( gridTable[checkY, checkX] == 1):
                count += 1
            checkX += 1
        checkY += 1
    return count

def initRandom():
    for y in range(h):
        for x in range(w):
            n = randint(0,2)
            if(n==0):
                clickGrid(x, y)


def incGrid():
    global gridTable
    nextGrid = gridTable.copy()
    for y in range(h):
        for x in range(w):
            #count living neighbors
            n = countNeighbors(x, y)
            if( gridTable[y,x] == 1):
                if(n < 2):
                    nextGrid[y, x] = 0
                elif(n > 3):
                    nextGrid[y, x] = 0
            else:
                if(n == 3):
                    nextGrid[y, x] = 1

    gridTable = nextGrid.copy()










