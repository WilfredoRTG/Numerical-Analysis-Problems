from prettytable import PrettyTable as pt

''' 
    Neville iterative interpolation Algorithm - page 91 - Algorithm 3.1
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

def Neville(X, valX, valQ):
    
    for i in range(len(valX)):
        for j in range(i):
            j+=1
            valQ[i][j] = ((X-valX[i-j])*valQ[i][j-1])-((X-valX[i])*valQ[i-1][j-1]) \
                                        /(valX[i] - valX[i-j])
            
    return valQ

# ============================================================================ #
#                 End Neville iterative interpolation Algorithm                #
# ============================================================================ #




# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")

X = 1.5
valX = [1, 1.3, 1.6, 1.9, 2.2]
valQ =  [
            [1.0, 0, 0, 0, 0],
            [1.3, 0, 0, 0, 0],
            [1.6, 0, 0, 0, 0],
            [1.9, 0, 0, 0, 0],
            [2.2, 0, 0, 0, 0]
        ]
valQ = Neville(X, valX, valQ)
for i in range(len(valQ)):
    print(valQ[i])

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #