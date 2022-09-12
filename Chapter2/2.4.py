from prettytable import PrettyTable as pt
import numpy as np

''' 
    Secante method  - page 54,55 - Algorithm 2.4
    Entry values:
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

def Secante(f, p0, p1, TOL, N):
    tb = pt()
    tb.align = "l"
    tb.field_names = ["n","p"]
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= N:
        p = p1 - ((q1*(p1 - p0))/(q1 - q0))
        tb.add_row([i,p])
        if abs(p - p1) < TOL:
            return (
                    print(tb),
                    print(f'\np={p}')
                )
        
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    return print(f'\nEl método fracasó después de {N} iteraciones')


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
Secante(f, p0, p1, TOL, N)

# Test Case 2
# print("\n\nTest 2")
# f = lambda x: x**3 + 4*x**2 - 10
# p0 = 1.5
# p1 = 1
# TOL = 10**-3
# N = 100
# Secante(f, p0, p1, TOL, N)

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #