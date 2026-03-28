# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:59:40 2026

@author: utpal.bhadra

"""

def updateMatrix(matrix, indexX, indexY, value):
    if value != 2: matrix[indexX][indexY] = value #state of the cell remains unchanged
    else:
        try:
            if matrix[indexX-1][indexY] != 0 and matrix[indexX+1][indexY] != 0: #reproduce vertically
                matrix[indexX-1][indexY] = matrix[indexX+1][indexY] = 0
                matrix[indexX][indexY-1] = matrix[indexX][indexY+1] = 1
            elif matrix[indexX][indexY-1] != 0 and matrix[indexX][indexY+1] != 0: # reproduce horizontally
                matrix[indexX-1][indexY] = matrix[indexX+1][indexY] = 1
                matrix[indexX][indexY-1] = matrix[indexX][indexY+1] = 0
        except:
            matrix[indexX][indexY] = matrix[indexX][indexY] #state of the cell remains unchanged
    return matrix

def state(state,matrix,x,y):
    if state == 1:
        updateMatrix(matrix, x, y, 0)
    elif state == 2:
        updateMatrix(matrix, x, y, 2)
    elif state == 3:
        updateMatrix(matrix, x, y, 0)
    elif state == 4:
        updateMatrix(matrix, x, y, 1)
    else:
        updateMatrix(matrix, x, y, matrix[x][y])

'''
if __name__ == "__main__":
    matrix = [[0,1,0,0],
              [0,1,0,0],
              [0,1,0,0]]
    x = 1
    y = 1
    print(updateMatrix(matrix, x, y, 2))
'''