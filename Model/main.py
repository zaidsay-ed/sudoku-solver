import numpy as num

# define example to test out code


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