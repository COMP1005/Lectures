"""
gridding2.py - extends previous to show the nextgrid ibeing built with each calculation

Usage:
    - again, can comment out for Moore or Von Neumann
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
nextg = np.zeros((size, size))

# timesteps

for t in range(3):
    for r in range(1, size-1):
        for c in range(1, size-1):
            subg = grid[r-1:r+2,c-1:c+2]
            #moore(subg)
            von_neumann(subg)
            nextg[r,c] = 1

            plt.subplot(1,2,1)
            plt.imshow(grid)
            
            plt.subplot(1,2,2)
            plt.imshow(nextg)

            plt.suptitle(f"Timestep: {t} Row: {r} Column: {c}")
            plt.pause(0.5)
            plt.clf()
            
            clear(subg) 
    clear(nextg)

