# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

import numpy as np

def create_surface(matrix, ca_type=None, ant_x=None, ant_y=None):
    """
    Converts a matrix of states into an RGB surface array for Pygame.

    Parameters:
    - matrix: 2D numpy array of CA states
    - ca_type: optional, if 'Langton' will show the ant in red
    - ant_x, ant_y: coordinates of Langton's Ant (if ca_type='Langton')
    
    Returns:
    - surface: 3D numpy array (height, width, 3) RGB
    """
    height, width = matrix.shape
    surface = np.zeros((height, width, 3), dtype=np.uint8)

    if ca_type == "Langton":
        # White = 0, Black = 1, Ant = red
        surface[matrix == 0] = (255, 255, 255)
        surface[matrix == 1] = (0, 0, 0)
        if ant_x is not None and ant_y is not None:
            surface[ant_y % height, ant_x % width] = (255, 0, 0)
    else:
        # For other CA types, assign distinct colors for each state
        unique_states = np.unique(matrix)
        colors_dict = {}
        for i, state in enumerate(unique_states):
            np.random.seed(int(state)+42)  # reproducible colors
            colors_dict[state] = tuple(np.random.randint(0, 256, 3))
            surface[matrix == state] = colors_dict[state]

    return surface


def initialize_matrix(size, ca_type="binary", N=2):
    """
    Initializes a matrix for a given CA type.

    Parameters:
    - size: tuple (rows, cols)
    - ca_type: "binary", "wireworld", "cyclic", etc.
    - N: number of states for cyclic or larger-than-life CA

    Returns:
    - matrix: initialized numpy array
    """
    if ca_type in ["binary", "HighLife", "Brian", "Seeds"]:
        return np.random.randint(0, 2, size=size)
    elif ca_type == "Wireworld":
        return np.zeros(size, dtype=int)
    elif ca_type == "Cyclic":
        return np.random.randint(0, N, size=size)
    else:
        # Default binary
        return np.random.randint(0, 2, size=size)