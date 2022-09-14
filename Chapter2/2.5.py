from prettytable import PrettyTable as pt
import numpy as np

''' 
    False position  - page 57 - Algorithm 2.5
    Entry values:
        function = f
        Initial aproximation 1 = p0
        Initial aproximation 2 = p1
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                        Secante method Algorithm                              #
# ============================================================================ #

def FalsePosition(f, p0, p1, TOL, N):

# Configuration for prettytable
    tb = pt()
    tb.align = "l"
    tb.field_names = ["n","p"]

# Step 1
    i = 2
    q0 = f(p0)
    q1 = f(p1)
# End Step 1

# Step 2
    while i <= N:

    # Step 3
        p = p1 - ((q1*(p1 - p0))/(q1 - q0))
    # End Step 3

    # Add data to table
        tb.add_row([i,p])
    
    # Step 4
        if abs(p - p1) < TOL:
            return (
                    print(tb),
                    print(f'\np={p}')
                )
    # End Step 4

    # Step 5
        i += 1
        q = f(p)
    # End Step 5

    # Step 6
        if q*q1 < 0:
            p0 = p1
            q0 = q1
    # End Step 6

    # Step 7
        p1 = p
        q1 = q
    # End Step 7

# End Step 2

# Step 8
    return print(f'\nEl método fracasó después de {N} iteraciones')
# End Step 8


# ============================================================================ #
#                      Secante method Algorithm                                #
# ============================================================================ #





# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")
f = lambda x : np.cos(x) - x
p0 = 0.5
p1 = np.pi/4
TOL = 10**-3
N = 100
FalsePosition(f, p0, p1, TOL, N)


# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #