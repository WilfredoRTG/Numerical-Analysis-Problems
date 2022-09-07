from prettytable import PrettyTable as pt

''' 
    Newton Method - page 50,51 - Algorithm 2.3
    Entry values:
        Initial aproximation = p0
        Tolerance = TOL
        Max number of iterations = N
    Ouput:
        Approximation result of p or message of failure
'''

# ============================================================================ #
#                         Newton Method Algorithm                              #
# ============================================================================ #



# ============================================================================ #
#                       End Newton Method Algorithm                            #
# ============================================================================ #





# ============================================================================ #
#                            Test Cases                                        #
# ============================================================================ #

# Test Case 1
print("\n\nTest 1")
# f = lambda x: x**3 + 4*x**2 - 10
g = lambda x: 1/2*(10 - x**3)**(1/2)
p0 = 1.5
TOL = 10**-3
N = 100
# Newton(g, p0, TOL, N)

# Test Case 2
print("\n\nTest 2")
# f = lambda x: x**3 + 4*x**2 - 10
g = lambda x: (10/(4+x))**(1/2)
p0 = 1.5
TOL = 10**-3
N = 100
# Newton(g, p0, TOL, N)

# ============================================================================ #
#                            End Test Cases                                    #
# ============================================================================ #