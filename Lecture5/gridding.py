"""
gridding.py - animates the gridding algorithm via a plot

Usage:
    - comment out call to Moore or Von Neumann to choose neighbourhood
    - could prompt to choose, but leave that as an exercise for the students
"""
import matplotlib.pyplot as plt
import numpy as np

def moore(subgrid):
    subgrid[:,:] = 1
    subgrid[1,1] = 2

def von_neumann(subgrid):
    subgrid[0,1] = 1
    subgrid[2,1] = 1
    subgrid[1,0] = 1
    subgrid[1,2] = 1
    subgrid[1,1] = 2

def clear(subgrid):
    subgrid[:,:] = 0

size = 8
grid = np.zeros((size, size))

# timesteps

for t in range(3):
    for r in range(1, size-1):
        for c in range(1, size-1):
            subg = grid[r-1:r+2,c-1:c+2]
            moore(subg)
            #von_neumann(subg)

            # plotting

            plt.imshow(grid)
            plt.title(f"Timestep: {t} Row: {r} Column: {c}")
            plt.pause(0.5)
            plt.clf()
            
            # reset for next "calculation"
            clear(subg) 

