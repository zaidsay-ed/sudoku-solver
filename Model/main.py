import numpy as nump

# define example to test out code
example1 = [[3,0,0,0,0,0,0,0,6],
            [0,1,6,0,5,0,0,0,4],
            [0,2,0,0,3,0,0,1,5],
            [0,0,0,8,1,5,0,0,0],
            [5,8,4,3,0,7,0,0,0],    #easy
            [9,0,0,0,6,4,0,3,8],
            [2,0,9,0,0,0,8,4,1],
            [0,0,0,0,2,0,6,0,0],
            [0,5,0,0,0,8,7,0,0]]

example2 = [[0,0,0,0,0,0,0,0,0],
            [4,0,0,0,8,0,0,6,9],
            [0,0,8,0,7,3,0,0,5],
            [6,0,1,0,3,5,2,9,0],
            [0,9,0,0,0,0,0,5,0],    #medium
            [0,2,7,1,9,0,4,0,3],
            [2,0,0,5,1,0,9,0,0],
            [1,5,0,0,6,0,0,0,8],
            [0,0,0,0,0,0,0,0,0]]

example3 = [[6,4,0,0,7,0,0,0,0],
            [0,2,0,1,0,3,0,0,8],
            [9,0,3,0,2,0,0,0,0],
            [0,5,0,0,0,4,0,0,1],
            [4,0,1,0,0,0,5,0,6],    #hard
            [3,0,0,6,0,0,0,4,0],
            [0,0,0,0,3,0,4,0,5],
            [2,0,0,4,0,8,0,1,0],
            [0,0,0,0,6,0,0,8,2]]

matrix = example3 #used in solver

"""
let x be example mentioned above

 (define (solved? x)
    (if (have-we-found-result? x)  ;success?
(produce-result x)         ;produce correct value
(solve (x-subs x))))) ;search in the subs of this node

let lox be graphofx

(define (solve lox)
 (cond [(empty? lox) false]
 [else
 (if (not (false? (solved? (first lox))))  ;is first child successful?
(solved? (first lox))                 ;if so produce that
(solve (rest lox)))])))           ;or try rest of children
"""

def solve():
    global matrix
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                for number in range(1,10):
                    if is_solved(row, column, number):
                        matrix[row][column] = number
                        if solve():
                            return True
                        matrix[row][column] = 0
                return False
    return True


def is_solved(row, column, number):
    global matrix
    for i in range(9):            #check if number is given in row
        if matrix[row][i] == number:
            return False
    for i in range(9):            #check if number is given in column
        if matrix[i][column] == number:
            return False
    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(0, 3):           #check if number is given in square
        for j in range(0, 3):
            if matrix[y+i][x+j] == number:
                return False
    return True

if solve():
    print("Sudoku Solved:\n")
    print(nump.matrix(matrix))
else:
    print("No solution exists.")