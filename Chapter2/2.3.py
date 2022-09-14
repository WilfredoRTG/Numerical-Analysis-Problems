from prettytable import PrettyTable as pt
import numpy as np

''' 
    Newton method Algorithm  - page 50,51 - Algorithm 2.3
    Entry values:
        function = f
        derivative of function = deriv
        Initial aproximation = p0
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                        Newton method Algorithm                               #
# ============================================================================ #

def Newton(f, deriv, p0, TOL, N):

# Configuration for prettytable
    tb = pt()
    tb.align = "l"
    tb.field_names = ["N","p"]
# Step 1
    i = 1
# End Step 1

# Step 2
    while i <= N:

    # Step 3
        p = p0 - f(p0)/deriv(p0)
    # End Step 3

    # Add data to table
        tb.add_row([i,p])
    
    # Step 4
        if abs(p - p0) < TOL:
            return (
                    print(tb),
                    print(f'\np={p}')
                )
    # End Step 4

    # Step 5
        i += 1
    # End Step 5

    # Step 6
        p0 = p
    # End Step 6

# End Step 2

# Step 7
    return print(f'\nEl método fracasó después de {N} iteraciones')
# End Step 7


# ============================================================================ #
#                      End Newton method Algorithm                             #
# ============================================================================ #





# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")
f = lambda x :np.cos (x) - x 
deriv = lambda x: - np.sin(x) - 1
p0 = np.pi/4
TOL = 10**-3
N = 100
Newton(f, deriv, p0, TOL, N)


# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #