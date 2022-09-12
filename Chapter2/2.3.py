from prettytable import PrettyTable as pt
import numpy as np

''' 
    Newton method Algorithm  - page 50,51 - Algorithm 2.3
    Entry values:
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

    i = 1
    while i <= N:
        p = p0 - f(p0)/deriv(p0)
        tb.add_row([i,p])
        if abs(p - p0) < TOL:
            return (
                    print(tb),
                    print(f'\np={p}')
                )
        i += 1
        p0 = p
    return print(f'\nEl método fracasó después de {N} iteraciones')

# ============================================================================ #
#                      Newton method Algorithm                                 #
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