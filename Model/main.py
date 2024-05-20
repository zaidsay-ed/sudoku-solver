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

example = example1  #used in solver

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
    global example
    for row in range(0,9):
        for column in range(0,9):
            if example[row][column] == 0:
                for number in range(0,10):
                    if is_solved(row, column, number):
                        example[row][column] = number
                        solve()
                        example[row][column] = 0
                return


