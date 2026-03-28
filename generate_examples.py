# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

#Default grid size
size = 30

# create_examples.py
import numpy as np
import os

folder = "examples"
os.makedirs(folder, exist_ok=True)

# 1. Conway Glider
matrix = np.zeros((size,size), dtype=int)
matrix[1,2]=1; matrix[2,3]=1; matrix[3,1:4]=1
np.save(os.path.join(folder,"conway_glider.npy"), matrix)

# 2. Brian's Brain
matrix = np.zeros((size,size), dtype=int)
matrix[10,10] = 1
np.save(os.path.join(folder,"brians_brain.npy"), matrix)

# 3. Seeds
matrix = np.zeros((size,size), dtype=int)
matrix[10,10]=1; matrix[10,11]=1
np.save(os.path.join(folder,"seeds_pattern.npy"), matrix)

# 4. Wireworld
matrix = np.zeros((size,size), dtype=int)
matrix[5,5:15]=3; matrix[14,5:15]=3; matrix[5:15,5]=3; matrix[5:15,14]=3
matrix[5,7]=1; matrix[14,12]=1
np.save(os.path.join(folder,"wireworld_gates.npy"), matrix)

# 5. Langton's Ant
matrix = np.zeros((size,size), dtype=int)
matrix[5,5:10]=1
ant = (10,10,0)
np.save(os.path.join(folder,"langtons_ant_pattern.npy"), {"matrix":matrix,"ant":ant})

# 6. Totalistic / Larger-than-Life
matrix = np.random.choice([0,1], size=(size,size))
np.save(os.path.join(folder,"totalistic_pattern.npy"), matrix)

# 7. Elementary CA (1D)
matrix = np.zeros((1,size), dtype=int)
matrix[0,10]=1
np.save(os.path.join(folder,"elementary_ca.npy"), matrix)

# 8. Cyclic CA N=8
matrix = np.random.randint(0,8,size=(size,size))
np.save(os.path.join(folder,"cyclic_pattern.npy"), matrix)

print("All example patterns saved to 'examples/' folder!")