"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

from doctest import BLANKLINE_MARKER
import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import date


ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(W, H):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, W*H, p=[0.2, 0.8]).reshape(W,H)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])

    grid[i:i+3, j:j+3] = glider

def isShape(grid, G, W, H):

     gliderCounter = 0
     blockCounter = 0
     beehiveCounter = 0
     loafCounter = 0
     boatCounter = 0
     tubCounter = 0
     blinkerCounter = 0
     toadCounter = 0  
     beaconCounter = 0
     spaceshipCounter = 0 
     total = 0 

     glider = np.array([[0, 0,    0,  0, 0],
                       [0, 0,    0, 255, 0],
                       [0, 255,  0, 255, 0], 
                       [0, 0,  255, 255, 0],
                       [0, 0,    0,   0, 0]])
    
     glider1 = np.array([[0,  0,    0,  0, 0],
                       [0,   0,    255, 0, 0],
                       [0,   0,  0,   255, 0], 
                       [0, 255,  255, 255, 0],
                       [0, 0,    0,   0,  0]])
    
     glider2 = np.array([[0, 0,    0,    0,  0],
                       [0, 255,   0,    255, 0],
                       [0, 0,   255,    255, 0], 
                       [0, 0,   255,    0,   0],
                       [0, 0,    0,     0,   0]])
    
     glider3 = np.array([[0, 0,      0,     0,  0],
                       [0, 255,     0,     0, 0],
                       [0, 0,     255,    255, 0], 
                       [0, 255,   255,    0,   0],
                       [0, 0,    0,     0,   0]])

     loaf   = np.array([[0, 0,      0,     0,   0, 0], 
                       [0, 0,     255,   255,  0, 0],
                       [0, 255,     0,    0, 255, 0], 
                       [0, 0,   255,      0, 255, 0],
                       [0, 0,    0,     255,   0, 0],
                       [0, 0,    0,       0,   0, 0]])
    
     beehive = np.array([[0, 0,      0,     0,  0,0], 
                       [0, 0,     255,   255, 0, 0],
                       [0, 255,     0,   0, 255, 0], 
                       [0, 0,   255,    255, 0, 0 ],
                       [0, 0,    0,     0,   0 ,0 ]])

     block  = np.array([[ 0,    0,      0,  0],
                       [ 0,   255,    255, 0],
                       [ 0,   255,    255, 0], 
                       [ 0,   0,        0, 0]])
    
     tub = np.array([[0,   0,   0,   0, 0],
                    [0,   0, 255,   0, 0], 
                    [0, 255,   0, 255, 0], 
                    [0,   0, 255,   0, 0],
                    [0,   0,   0,   0, 0]])
    
    
     beacon=np.array([[0,    0,   0,     0,   0,  0], 
                    [0,   255, 255,     0,   0, 0], 
                    [0,   255, 255,     0,   0, 0], 
                    [0, 0,   0,     255,   255, 0],
                    [0,   0,   0,   255,   255, 0],
                    [0,    0,   0,     0,   0,  0]])
    
     beacon1=np.array([[0,    0,   0,     0,   0,  0], 
                    [0,   255, 255,     0,   0, 0], 
                    [0,   255, 0,     0,   0, 0], 
                    [0, 0,   0,     0,   255, 0],
                    [0,   0,   0,   255,   255, 0],
                    [0,    0,   0,     0,   0,  0]])
     blinker = np.array([[  0,   0,   0], 
                    [   0, 255,    0], 
                    [   0, 255,    0], 
                    [   0, 255,    0],
                    [   0,   0,    0]])
    
     toad = np.array([[0,  0,   0,     0,   0,   0], 
                    [0,   0,   0,     255,   0, 0], 
                    [0, 255,   0,     0,   255, 0], 
                    [0, 255,   0,     0,   255, 0],
                    [0,   0,   255,   0,   0, 0]])
    
     toad1 = np.array([[0,  0,   0,     0,   0,      0], 
                    [0,   0,   255,     255,   255, 0], 
                    [0, 255,   255,     255,   0,   0], 
                    [0, 0,   0,           0,    0,  0]])
    
     spaceship=np.array([[0,    0,   0,     0,   0,  0,  0], 
                      [0,   255, 0,     0,   255,   0,  0], 
                      [0,   0,  0,     0,      0,  255, 0], 
                      [0, 255,   0,     0,       0, 255, 0],
                      [0,   0,   255,   255,   255, 255,0],
                      [0,    0,   0,     0,   0,  0, 0]])
    
     spaceship1=np.array([[0,    0,   0,     0,   0,  0,  0], 
                         [0,   0,   255, 255,  255, 255,  0], 
                         [0,   255,  0,     0,   0,  255, 0], 
                         [0, 0,   0,     0,    0,    255, 0],
                         [0,   255,   0,   0,  255,   0,  0],
                      [0,    0,   0,     0,   0,  0, 0]])
    
     spaceship2=np.array([[0,   0,   0,   0,   0,   0,   0],
                         [0,   0,   0, 255, 255,   0,   0], 
                         [0, 255, 255,   0, 255, 255,   0], 
                         [0, 255, 255, 255, 255,   0,   0],
                         [0,   0, 255, 255,   0,   0,   0],
                         [0,   0,   0,   0,   0,   0,   0]])
    
     spaceship3 = np.array([[0,   0,   0,   0,   0,   0,   0],
                            [0,   0, 255, 255,   0,   0,   0], 
                            [0, 255, 255, 255, 255,   0,   0], 
                            [0, 255, 255,   0, 255, 255,   0],
                            [0,   0,   0, 255, 255,   0,   0],
                            [0,   0,   0,   0,   0,   0,  0]])
    
     
     output = open("output.txt", "a")
    
     for i in range(W):
         for j in range(H):

             if(np.array_equal(grid[ i:i+5, j:j+5] , glider, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider,3), equal_nan=True))):
                gliderCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+5] , glider1, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider1,3), equal_nan=True))):
                gliderCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+5] , glider2, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider2,3), equal_nan=True))):
                gliderCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+5] , glider3, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(glider3,3), equal_nan=True))):
                gliderCounter +=1
             if(np.array_equal(grid[ i:i+4, j:j+4] , block, equal_nan=True)):
                blockCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+6] , beehive, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(beehive), equal_nan=True))):
                beehiveCounter +=1 
             if(np.array_equal(grid[ i:i+6, j:j+6] , loaf, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf), equal_nan=True)) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf, 2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(loaf,3), equal_nan=True))):
                loafCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+5] , tub, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub, 2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(tub,3), equal_nan=True))):
                tubCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+3] , blinker, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+3] , np.rot90(blinker), equal_nan=True))):
                blinkerCounter +=1
             if(np.array_equal(grid[ i:i+5, j:j+6] , toad, equal_nan=True) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(toad), equal_nan=True)) or (np.array_equal(grid[ i:i+5, j:j+6] , np.rot90(toad,2), equal_nan=True))or (np.array_equal(grid[ i:i+5, j:j+5] , np.rot90(toad,3), equal_nan=True))):
                toadCounter +=1 
             if(np.array_equal(grid[ i:i+4, j:j+6] , toad1, equal_nan=True) or (np.array_equal(grid[ i:i+4, j:j+6] , np.rot90(toad1), equal_nan=True))):
                toadCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+6] , beacon, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon), equal_nan=True))):
                beaconCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+6] , beacon1, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+6] , np.rot90(beacon1,3), equal_nan=True))):
                beaconCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship,3), equal_nan=True))):
                spaceshipCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship1, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship1,3), equal_nan=True))):
                spaceshipCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship2, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship2,3), equal_nan=True))):
                spaceshipCounter +=1
             if(np.array_equal(grid[ i:i+6, j:j+7] , spaceship3, equal_nan=True) or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3,2), equal_nan=True))or (np.array_equal(grid[ i:i+6, j:j+7] , np.rot90(spaceship3,3), equal_nan=True))):
                spaceshipCounter +=1
            

     total = gliderCounter + beehiveCounter + blockCounter  + loafCounter + boatCounter + tubCounter + blinkerCounter + toadCounter + beaconCounter + spaceshipCounter
    
     today = date.today()
     output.write("%s  %s\n" %("Simulation at: ", today))
     output.write("%s  %sx%s\n\n" %("Universe Size: ", W, H))
     output.write("%s  %s\n" %("Iteration: ", G))
     output.write("--------------------------\n")
     output.write("|  \t|  Count  |  Percent  |\n")
     output.write("%s  \t%s\t%s\n" %("Gliders: ", gliderCounter, (100*gliderCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Loafs: ", loafCounter, (100*loafCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Beehives: ", beehiveCounter, (100*beehiveCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Blocks: ", blockCounter, (100*blockCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Tubs: ", tubCounter, (100*tubCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Beacons: ", beaconCounter, (100*beaconCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Blinkers: ", blinkerCounter, (100*blinkerCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Toads: ", toadCounter, (100*toadCounter)/total))
     output.write("%s  \t%s\t%s\n" %("Spaceships: ", spaceshipCounter, (100*spaceshipCounter)/total))
     output.write("%s  %s\n\n\n" %("Total: ", total))
     output.write("--------------------------\n")
    
    
  
def update(frameNum, img, grid, W, H):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life

    for i in range(W):
        for j in range(H):
 
            # compute 8-neighbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1)%H] + grid[i, (j+1)%H] +
                         grid[(i-1)%W, j] + grid[(i+1)%W, j] +
                         grid[(i-1)%W, (j-1)%H] + grid[(i-1)%W, (j+1)%H] +
                         grid[(i+1)%W, (j-1)%H] + grid[(i+1)%W, (j+1)%H])/255)
 
            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    
    updateInterval = 50

    digit_list = []
    file = "input.txt"
    fileObj = open(file, "r")
    lines = fileObj.read().splitlines() 
    for line in lines:
        words = line.split()
        for word in words:
            digit = word.split()
            digit_list.append(digit)
    
    width = int(digit_list[0][0])
    height = int(digit_list[1][0])
    generations = int(digit_list[4][0])

    # set animation update interval

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(width, height)
    # Uncomment lines to see the "glider" demo

    alive_cells_x = []
    alive_cells_y = []
    grid = np.zeros(width*height).reshape(width, height)
    for i in range(6, len(digit_list)): 
        if digit_list[i][0].isnumeric():
            if i == 0 or i % 2 == 0:
                alive_cells_x.append(int(digit_list[i][0]))
            else:
                alive_cells_y.append(int(digit_list[i][0]))
    
    for i, j in zip(alive_cells_x, alive_cells_y):
        
        addGlider(i, j, grid)


    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height, ),
                                  frames = 10,
                                  interval = updateInterval,
                                  save_count = 50)

    plt.show()
    isShape(grid, generations, width, height)
    

# call main
if __name__ == '__main__':
    main()