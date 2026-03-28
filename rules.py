# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

import numpy as np

# ---------------- HighLife ----------------
def update_highlife(matrix):
    neighbors = sum(np.roll(np.roll(matrix, i, 0), j, 1)
                    for i in (-1,0,1) for j in (-1,0,1) if (i,j) != (0,0))
    # HighLife rules: B36/S23
    birth = (neighbors==3) | (neighbors==6)
    survive = (neighbors==2) | (neighbors==3)
    new_matrix = np.where(matrix==1, survive, birth).astype(int)
    return new_matrix

# ---------------- Brian's Brain ----------------
# States: 0 = off, 1 = on, 2 = dying
def update_brians_brain(matrix):
    neighbors = sum(np.roll(np.roll((matrix==1).astype(int), i, 0), j, 1)
                    for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0))
    new_matrix = np.zeros_like(matrix)
    new_matrix[matrix==0] = (neighbors[matrix==0]==2).astype(int)
    new_matrix[matrix==1] = 2  # turn on cells to dying
    new_matrix[matrix==2] = 0  # dying cells turn off
    return new_matrix

# ---------------- Seeds ----------------
# Simple CA: birth if exactly 2 neighbors, no survival
def update_seeds(matrix):
    neighbors = sum(np.roll(np.roll(matrix, i, 0), j, 1)
                    for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0))
    new_matrix = ((matrix==0) & (neighbors==2)).astype(int)
    return new_matrix

# ---------------- Wireworld ----------------
# 0=empty, 1=head, 2=tail, 3=conductor
def update_wireworld(matrix):
    new_matrix = matrix.copy()
    head_neighbors = sum(np.roll(np.roll((matrix==1).astype(int), i, 0), j, 1)
                         for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0))
    new_matrix[matrix==1] = 2  # head becomes tail
    new_matrix[matrix==2] = 3  # tail becomes conductor
    cond = (matrix==3)
    new_matrix[cond & ((head_neighbors==1) | (head_neighbors==2))] = 1  # conductor with 1-2 heads becomes head
    new_matrix[cond & ~((head_neighbors==1) | (head_neighbors==2))] = 3
    return new_matrix

# ---------------- Langton's Ant ----------------
# Ant tuple: (x, y, direction), direction: 0=up,1=right,2=down,3=left
def update_langtons_ant(matrix, ant):
    x, y, dir = ant
    # directions: 0=up,1=right,2=down,3=left
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    
    # Turn ant
    if matrix[x,y] == 0:  # white -> turn right
        dir = (dir + 1) % 4
        matrix[x,y] = 1
    else:                  # black -> turn left
        dir = (dir - 1) % 4
        matrix[x,y] = 0
    
    # Move ant
    dx, dy = dirs[dir]
    x = (x + dx) % matrix.shape[0]
    y = (y + dy) % matrix.shape[1]
    
    return matrix, (x, y, dir)  # <-- return updated ant info

# ---------------- Larger-than-Life / Totalistic CA ----------------
# Example: B3/S45678 (can adjust for different rules)
def update_totalistic(matrix):
    neighbors = sum(np.roll(np.roll(matrix, i, 0), j, 1)
                    for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0))
    birth = (neighbors==3)
    survive = (neighbors>=4)
    new_matrix = np.where(matrix==1, survive, birth).astype(int)
    return new_matrix

# ---------------- Elementary 1D CA ----------------
# step = row number to update
def update_elementary_ca(matrix, step, rule_number=110):
    rule_bin = np.array(list(np.binary_repr(rule_number, width=8)), dtype=int)
    prev = matrix[step-1] if step>0 else matrix[0]
    new_row = np.zeros(matrix.shape[1], dtype=int)
    for i in range(matrix.shape[1]):
        left = prev[(i-1)%matrix.shape[1]]
        center = prev[i]
        right = prev[(i+1)%matrix.shape[1]]
        idx = 7 - (left*4 + center*2 + right)
        new_row[i] = rule_bin[idx]
    matrix[step] = new_row
    return matrix

# ---------------- Cyclic Cellular Automata ----------------
# N = number of states
def update_cyclic_ca(matrix, N):
    new_matrix = matrix.copy()
    target = (matrix + 1) % N
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if dx == 0 and dy == 0:
                continue
            neighbor = np.roll(np.roll(matrix, dx, 0), dy, 1)
            # wherever neighbor has the "next" state, the current cell updates
            new_matrix = np.where(neighbor == target, target, new_matrix)
    return new_matrix