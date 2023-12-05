
import numpy as np
from array import *

file = open('3-input.txt')
lines = file.readlines()

rows = 140
cols = 140

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

partNumbers = []

starDictionary = {'key' : ['value']}

sumOfGearRatio = 0

def initialize_2d_array_numpy(rows, cols):
    array_2d = np.zeros((rows, cols), dtype=str)
    return array_2d

def fillMatrix(file, array):
    i = 0;
    for line in lines:
        line = line.replace("\n", "")
        ii = 0
        for char in line:
            array[i][ii] = char
            ii = ii + 1
        i = i + 1   
    return np.asmatrix(array)     

def find_number(matrix):
    x = 0
    while x < cols:
        y = 0
        while y < rows:
            if(matrix[x,y] in numbers):
                number = matrix[x,y]
                numberLength = 1
                while True:
                    if(y + numberLength >= rows): break
                    if matrix[x, y + numberLength] in numbers:
                        number = number +  matrix[x, y + numberLength]
                        numberLength = numberLength + 1
                    else:
                        break
                if(check_for_symbol(matrix, x, y, numberLength)) : partNumbers.append(int(number))
                check_for_star(matrix, x, y, numberLength, number)
                y += numberLength
            y += 1
        x += 1

def check_for_symbol(matrix, x, y, numberLength):
    for i in range(0 if x == 0 else -1, 0 if x == rows - 1 else 2):
        for ii in range(-1, numberLength + 1):
            if(i == 0 and ii >= 0 and ii < numberLength or y + ii >= rows or y + ii < 0): continue
            print("current checking: ", matrix[x + i, y + ii])
            if (matrix[x + i, y + ii]) != '.' and (matrix[x + i, y + ii]) not in numbers:
                print("LEGIT")
                return True
    return False

def check_for_star(matrix, x, y, numberLength, number):
    for i in range(0 if x == 0 else -1, 0 if x == rows - 1 else 2):
        for ii in range(-1, numberLength + 1):
            if(i == 0 and ii >= 0 and ii < numberLength or y + ii >= rows or y + ii < 0): continue
            if (matrix[x + i, y + ii]) == '*':
                xPos = str(x + i)
                yPos = str(y + ii)
                starPos = xPos + ',' + yPos
                if(starDictionary.get(starPos) == None):
                    starDictionary.update({starPos : [number]})
                else:
                    starDictionary[starPos].append(number)
                break

array = initialize_2d_array_numpy(rows, cols)
matrix = fillMatrix(file, array)
find_number(matrix)
print('sum part numbers: ', sum(partNumbers))

for key in starDictionary:
    if(len(starDictionary[key]) == 2):
        sumOfGearRatio += int(starDictionary[key][0]) * int(starDictionary[key][1])

print('sum gear ration: ', sumOfGearRatio)