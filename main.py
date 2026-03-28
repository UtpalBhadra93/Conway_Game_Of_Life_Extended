# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

import pygame
import numpy as np
from rules import *

# ---------------- Config ---------------- #
size = 50       # grid size
scale = 10      # pixel size of each cell
fps = 10        # frames per second
N = 8           # number of states for Cyclic CA

# ---------------- Menu ---------------- #
print("Select Cellular Automata type:")
print("1. HighLife")
print("2. Brian's Brain")
print("3. Seeds")
print("4. Wireworld")
print("5. Langton's Ant")
print("6. Larger-than-Life / Totalistic CA")
print("7. Elementary Cellular Automata (1D)")
print("8. Cyclic Cellular Automata")
choice = int(input("Enter number (1-8): "))

print("Choose initial configuration:")
print("1. Random")
print("2. Load preset pattern (from examples/)")
pattern_choice = int(input("Enter number (1-2): "))

# ---------------- Initialize Matrix ---------------- #
matrix = np.zeros((size, size), dtype=int)
step = 1
ant = None

if pattern_choice == 1:  # Random
    if choice in [1,2,3,6]:  # Binary CAs
        matrix = np.random.choice([0,1], size=(size,size))
    elif choice == 4:  # Wireworld
        matrix = np.zeros((size,size), dtype=int)
        # small visible loop as initial pattern
        matrix[5,5:15] = 3
        matrix[14,5:15] = 3
        matrix[5:15,5] = 3
        matrix[5:15,14] = 3
        matrix[5,7] = 1
        matrix[14,12] = 1
    elif choice == 5:  # Langton's Ant
        matrix = np.zeros((size,size), dtype=int)
        ant = (size//2, size//2, 0)  # x, y, direction
    elif choice == 7:  # Elementary 1D CA
        matrix = np.zeros((size,size), dtype=int)
        matrix[0, size//2] = 1
        step = 1
    elif choice == 8:  # Cyclic CA
        matrix = np.random.randint(0, N, size=(size,size))

elif pattern_choice == 2:  # Load preset
    import os
    if choice == 4:
        matrix = np.load(os.path.join("examples","wireworld_gates.npy"))
    elif choice == 5:
        matrix = np.load(os.path.join("examples","langtons_ant_pattern.npy"))
        ant = (size//2, size//2, 0)
    elif choice == 7:
        matrix = np.load(os.path.join("examples","elementary_pattern.npy"))
        step = 1
    else:
        matrix = np.load(os.path.join("examples","conway_glider.npy"))

# ---------------- Colors ---------------- #
def get_color(val, choice, ant=None, N=8):
    if choice in [1,2,3,6]:  # binary
        return (255,255,255) if val==1 else (0,0,0)
    elif choice==4:  # Wireworld
        cmap = {0:(0,0,0), 1:(0,0,255), 2:(255,0,0), 3:(255,255,0)}
        return cmap[val]
    elif choice==5:  # Langton's Ant
        return (255,0,0) if ant and (val==ant[0] and val==ant[1]) else ((255,255,255) if val==0 else (0,0,0))
    elif choice==7:  # 1D CA
        return (255,255,255) if val==1 else (0,0,0)
    elif choice==8:  # Cyclic CA
        np.random.seed(val)  # ensure same state always same color
        return tuple(np.random.randint(50,255,3))
    return (0,0,0)

# ---------------- Initialize Pygame ---------------- #
pygame.init()
window = pygame.display.set_mode((size*scale, size*scale))
pygame.display.set_caption("Cellular Automata Simulator")
clock = pygame.time.Clock()

# ---------------- Main Loop ---------------- #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update matrix per CA
    if choice==1:
        matrix = update_highlife(matrix)
    elif choice==2:
        matrix = update_brians_brain(matrix)
    elif choice==3:
        matrix = update_seeds(matrix)
    elif choice==4:
        matrix = update_wireworld(matrix)
    elif choice==5:
        matrix, ant = update_langtons_ant(matrix, ant)
    elif choice==6:
        matrix = update_totalistic(matrix)
    elif choice==7:
        if step < matrix.shape[0]:
            matrix = update_elementary_ca(matrix, step)
            step += 1
    elif choice==8:
        matrix = update_cyclic_ca(matrix, N)

    # Draw matrix
    surface = np.zeros((matrix.shape[0], matrix.shape[1], 3), dtype=np.uint8)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if choice==5:
                if ant and i==ant[0] and j==ant[1]:
                    surface[i,j] = (255,0,0)
                else:
                    surface[i,j] = get_color(matrix[i,j], choice, ant)
            else:
                surface[i,j] = get_color(matrix[i,j], choice, N=N)

    surf = pygame.surfarray.make_surface(surface)
    surf = pygame.transform.scale(surf, (matrix.shape[1]*scale, matrix.shape[0]*scale))
    window.blit(surf, (0,0))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()