# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

import numpy as np

def findNeighbour(matrix, x, y, radius=1):
    """
    Returns a flattened list of neighboring cell values for a cell at (x, y)
    using a square window with the specified radius. Handles edges safely.
    """
    x_min = max(x - radius, 0)
    x_max = min(x + radius + 1, matrix.shape[0])
    y_min = max(y - radius, 0)
    y_max = min(y + radius + 1, matrix.shape[1])

    neighbors = matrix[x_min:x_max, y_min:y_max].flatten()
    return neighbors

'''
matrix = [[1,5,6,8],
          [1,2,5,9],
          [7,5,6,2]]
x = 1
y = 1
radius = 1
neighbours = [[1,5,6],
              [1,2,5],
              [7,5,6]]
x = 0
y = 0
radius = 1
neighbours = [[1,5,0],
              [1,2,0],
              [0,0,0]]
'''

'''
if __name__ == "__main__":
    matrix = [[1,5,6,8],
              [1,2,5,9],
              [7,5,6,2]]
    x = 0
    y = 3
    radius = 1
    neighbours = numpy.array(findNeighbour(matrix, x, y, radius))
    #neighbours.reshape(numpy.array(matrix).shape)
    print (neighbours)
'''