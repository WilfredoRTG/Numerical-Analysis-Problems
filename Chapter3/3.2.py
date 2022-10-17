from prettytable import PrettyTable as pt

''' 
    Newton Algorithm - page 91 - Algorithm 3.1
    Entry values:
        Value of X = X
        Values of X = valX
        First values of Q = valQ
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                  Neville iterative interpolation Algorithm                   #
# ============================================================================ #

def NewtonDiff(valX, F):
    
    for i in range(len(valX)):
        for j in range(i):
            j+=1 
            a = F[i][j-1] - F[i-1][j-1]
            b = valX[i]-  valX[i-j]
            c = a/b

            F[i][j] = c
            
    return F

# ============================================================================ #
#                 End Neville iterative interpolation Algorithm                #
# ============================================================================ #




# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")

valX = [1, 1.3, 1.6, 1.9, 2.2]
F =  [
            [0.7651977, 0, 0, 0, 0],
            [0.6200860, 0, 0, 0, 0],
            [0.4554022, 0, 0, 0, 0],
            [0.2818186, 0, 0, 0, 0],
            [0.1103623, 0, 0, 0, 0]
        ]
F = NewtonDiff(valX, F)
for i in range(len(F)):
    print(F[i])


# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #